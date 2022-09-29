import smtplib
from dns import resolver

import socket
import socks # PySocks

from smtplib import SMTP

class SocksSMTP(SMTP):

    def __init__(self,
            host='',
            port=0,
            local_hostname=None,
            timeout=socket._GLOBAL_DEFAULT_TIMEOUT,
            source_address=None,
            proxy_type=None,
            proxy_addr=None,
            proxy_port=None,
            proxy_rdns=True,
            proxy_username=None,
            proxy_password=None,
            socket_options=None):

        self.proxy_type=proxy_type
        self.proxy_addr=proxy_addr
        self.proxy_port=proxy_port
        self.proxy_rdns=proxy_rdns
        self.proxy_username=proxy_username
        self.proxy_password=proxy_password
        self.socket_options=socket_options
        # if proxy_type is provided then change the socket to socksocket
        # else behave like a normal SMTP class.
        if self.proxy_type:
            self._get_socket = self.socks_get_socket

        super(SocksSMTP, self).__init__(host, port, local_hostname, timeout, source_address)

    def socks_get_socket(self, host, port, timeout):
        if self.debuglevel>0:
            self._print_debug('connect: to', (host, port), self.source_address)
        return socks.create_connection((host, port),
                timeout=timeout,
                source_address=self.source_address,
                proxy_type=self.proxy_type,
                proxy_addr=self.proxy_addr,
                proxy_port=self.proxy_port,
                proxy_rdns=self.proxy_rdns,
                proxy_username=self.proxy_username,
                proxy_password=self.proxy_password,
                socket_options=self.socket_options)


# ============================
#      LOOKUP HOSTNAME 
# ============================
host_name = 'rub.edu.bt'

try:
    mx_record = resolver.query(host_name, 'MX')
    exchanges = [exchange.to_text().split() for exchange in mx_record ]

except(resolver.NoAnswer, resolver.NXDOMAIN, resolver.NoNameservers):
    exchanges = []

# print(exchanges[0][0]) - preference
# print(exchanges[0][1]) - domain

# ==============================
#  COMMUNICATE WITH SMTP SERVER 
# ==============================

from smtplib import SMTP

# SocksSMTP = SocksSMTP(smtplib.SMTP)

testMail = '02190138.cst@rub.edu.bt'

try:
    with SocksSMTP(exchanges[0][1]) as smtp:
        host_exist = True
        smtp.helo()
        smtp.mail('my-mail@gmail.com')
        resp = smtp.rcpt(testMail)

        if resp[0] == 250:
            print('Email Exists')
        elif resp[0] == 550:
            print('Email doesn\'t exist')
        else:
            print(resp[0])

except smtplib.SMTPServerDisconnected as err:
    print('SMTP connection error')
    print(err)

