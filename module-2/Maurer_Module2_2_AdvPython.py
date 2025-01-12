# Nathan Maurer
# December 8, 2024
# Module 8_2
# Create a dictionary and call key and value

def main():
    ticker = create_dict()

    # user input ticker symbol
    ticker_price = str(input('What ticker symbol would you like to view?'))

    # specifies order of key:value
    display_ticker(ticker, ticker_price)

def create_dict():
    
    # creates dictionary 'ticker'
    ticker = {"ALBT":6.33, "SOUN":14.17, "JFBR":3.16, "NVDA":144.51,
              "ZBAO":4.00, "ADD":4.63, "AMC":4.85, "RGTI":3.31,
              "BBAI":3.18, "QBTS":4.06, "TSLA":377.38}
    
    return ticker

def display_ticker(ticker, ticker_price):

    # if/else print depending on whether user input exists in dictionary as a 'key'
    if ticker_price in ticker:
        print(ticker_price,ticker[ticker_price])
    elif ticker_price not in ticker:
        print ("Ticker is not found")

if __name__ == '__main__':
    main()
