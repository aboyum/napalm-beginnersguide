from napalm import get_network_driver
import json

driver_ios = get_network_driver('ios')
sw1 = driver_ios('10.0.0.1', 'user', 'cisco')
sw1.open()
