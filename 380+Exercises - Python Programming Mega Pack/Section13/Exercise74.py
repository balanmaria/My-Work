#TODO: A list of tickers from the Dow Jones index is given:
# tickers = [
#     'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
#     'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
#     'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
# ]
# Transform this list into a dictionary (index, ticker) and print it to the console.

tickers = [
    'AAPL.US', 'AXP.US', 'BA.US', 'CAT.US',
    'CSCO.US', 'CVX.US', 'DIS.US', 'DOW.US',
    'GS.US', 'HD.US', 'IBM.US', 'INTC.US'
]

print(dict(enumerate(tickers)))