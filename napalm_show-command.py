from napalm import get_network_driver
from pprint import pprint
# from pprint import pprint

driver_ios = get_network_driver('ios')
sw1 = driver_ios('10.0.0.1', 'user', 'password')
sw1.open()

#Get list of interfaces and IOS version and such
sw1_output = sw1.get_facts()
pprint(sw1_output)

#Get more info of interfaces
sw1_output = sw1.get_interfaces()
pprint(sw1_output)

#Get ARP address table
sw1_output = sw1.get_arp_table()
pprint(sw1_output)

# List of all the things you can retrive by get
# https://napalm.readthedocs.io/en/latest/support/index.html