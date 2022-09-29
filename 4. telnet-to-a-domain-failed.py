import telnetlib

host = b'gmail-smtp-in.l.google.com'

tn = telnetlib.Telnet(host=host,port=25)
#tn.open(host)

tn.read_until(b'gsmtp')

tn.write(b'helo hi\n')

tn.read_until(b'service')

tn.write(b'close\n')

print(tn.read_all().decode('ascii'))
