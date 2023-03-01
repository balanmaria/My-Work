#TODO: The following dictionary is given:
# stats = {'site': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}
# Delete the 'traffic' key pair from this dictionary and print it to the console.

stats = {'site': 'e-smartdata.org', 'traffic': 100, 'type': 'organic'}
stats.pop('traffic')
print(stats)

del stats['traffic']
print(stats)