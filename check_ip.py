#!/usr/bin/env python3

import public_ip, asyncio, notify

current_ip = public_ip.get('current')
new_ip = public_ip.get('new')

do_ips_match = public_ip.compare(current_ip, new_ip)

if public_ip.has_changed() == True:
    notify.email(new_ip)
    public_ip.set(new_ip)
else:
    print('No change')
    

