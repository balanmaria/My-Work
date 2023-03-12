#TODO: The list of companies from the WIG.GAMES index is given with the closing price and currency:
# gaming = {
#   '11B': [362.5, 'PLN'],
#   'CDR': [74.25, 'USD'],
#   'CIG': [0.85, 'PLN'],
#   'PLW': [79.5, 'USD'],
#   'TEN': [300.0, 'PLN']
# }
# Using the continue statement, create a for loop that will change the closing price from USD to PLN in this dictionary. Take USDPLN = 4.0.
# In response, print the gaming dictionary to the console.

gaming = {
    '11B': [362.5, 'PLN'],
    'CDR': [74.25, 'USD'],
    'CIG': [0.85, 'PLN'],
    'PLW': [79.5, 'USD'],
    'TEN': [300.0, 'PLN']
}

for key in gaming:
    if gaming[key][1] != 'USD':
        continue
    else:
        gaming[key][1] = 'PLN'
        gaming[key][0] = gaming[key][0] * 4.0

print(gaming)

#METODA II

for ticker, info in gaming.items():
    if info[1] == 'PLN':
        continue
    info[0] = info[0] * 4.0
    info[1] = 'PLN'
print(gaming)