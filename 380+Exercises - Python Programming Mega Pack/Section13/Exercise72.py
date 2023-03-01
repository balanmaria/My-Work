#TODO: The following dictionary is given:
# stocks = {
#     'MSFT.US': {'Microsoft Corp': 184},
#     'AAPL.US': {'Apple Inc': 310},
#     'MMM.US': {'3M Co': 148}
# }
# Add a fourth pair to this dictionary with the key 'V.US' and the value: {'Visa Inc': 185}. Print the values of the stocks dictionary to the console.

stocks = {
    'MSFT.US': {'Microsoft Corp': 184},
    'AAPL.US': {'Apple Inc': 310},
    'MMM.US': {'3M Co': 148}
}

stocks['V.US'] = {'Visa Inc': 185}
print(stocks.values())