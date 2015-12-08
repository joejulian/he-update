#!/bin/env python
"""
he-update.py

This utility updates the ipv6 gateway address and the dyndns address if
the address changes using Hurricane Electric's free service.

dyndns changes must be configured in the advanced tab of your tunnel
configuration.

Example config:

    12345:
        hostname: myhost.domain.dom
        username: myuser
        password: mysupersecretpassword

where 12345 is your tunnel id

"""

import requests

conf_path = "/etc/he-update/he-update.yaml"
uri = "ipv4.tunnelbroker.net/nic/update"


def get_ns_ip(hostname):
    import dns.resolver
    lookup = dns.resolver.Resolver()
    ns1 = str(lookup.query('ns1.he.net')[0])
    ns2 = str(lookup.query('ns2.he.net')[0])
    lookup.nameservers = [ns1, ns2]

    myip = str(lookup.query(hostname)[0])
    return myip


def get_public_ip():
    return requests.get('http://ipv4.icanhazip.com').text


def ns_match(hostname):
    return get_public_ip() == get_ns_ip(hostname)


def update_he_gateway(hostname, username, password, tid):
    if ns_match(hostname):
        return 'nochg {}'.format(get_ns_ip(hostname))
    r = requests.get(
        'https://{uri}'.format(
            uri=uri
        ),
        auth=(username, password),
        params={
            'hostname': tid,
            'myip': get_public_ip(),
        }
    )
    return r.text


def execute():
    import yaml
    tunnels = yaml.safe_load(open(conf_path, 'r'))

    max_hostlen = max([len(tunnels[x]['hostname']) for x in tunnels.keys()])

    for tid in tunnels:
        print(("{0: <" + str(max_hostlen) + "}: {1}").format(tunnels[tid]['hostname'],
                                                             update_he_gateway(tid=tid, **tunnels[tid])))

if __name__ == '__main__':
    execute()
