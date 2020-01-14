from napalm import get_network_driver
import json

driver_ios = get_network_driver('ios')
sw1 = driver_ios('10.0.0.1', 'user', 'cisco')
sw1.open()

#Get list of interfaces and IOS version and such
sw1_output = sw1.get_facts()
print json.dumps(sw1_output, indent=4))

#Get more info of interfaces
sw1_output = sw1.get_interfaces()
print json.dumps(sw1_output, indent=4))

#Get ARP address table
sw1_output = sw1.get_arp_table()
print json.dumps(sw1_output, indent=4))

# List of all the things you can retrive by get
# https://napalm.readthedocs.io/en/latest/support/index.html