from napalm import get_network_driver
import json

driver_ios = get_network_driver('ios')
sw1 = driver_ios('10.0.3.119', 'user', 'password')
sw1.open()

print ('Accessing')
sw1.load_merge_candidate(filename='newconfig.cfg')

diffs = sw1.compare_config()
if len(diffs) > 0:
    print(diffs)
    sw1.commit_config()
else:
    print('No changes required!')
    sw1.discard_config
sw2.close()

# Documentation about config changes:
# https://napalm.readthedocs.io/en/latest/support/index.html