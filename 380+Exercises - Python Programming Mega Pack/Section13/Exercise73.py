#TODO: A list of tickers from the Dow Jones index is given:
# tickers = [
#     'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
#     'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
#     'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
# ]
# Transform this list into a list of two-element tuple objects (index, ticker) and print it to the console.

tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]

new_list = [(index, tickers[index]) for index in range(len(tickers))]
print(new_list)

print(list(enumerate(tickers)))