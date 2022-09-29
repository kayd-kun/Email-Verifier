import dns.resolver

host_domain = 'gmail.com'

results = dns.resolver.resolve(host_domain, 'MX')

for rdata in results:
    print ('Host', rdata.exchange, 'has preference', rdata.preference)
    #print('MX RECORD: ', exdata.to_text())

