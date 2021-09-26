#!/usr/local/bin/python
import urllib.request, json

# This is for the assignment. This program asks for a stock symbol
# and returns the price of the stock. The symbol data is parsed from
# AlphaVantage API where it will become a JSON format. It is then parsed
# into a dictionary where it can be retrieved. The returned values are
# also placed into the 'japi.out' file.
# 
# This program is done in a While loop and will break once 'quit'
# is typed. At the same time, a list will write to the 'japi.out' file.
# 
# 
# Please adjust file path for 'japi.out' for correct writing.
# #

def getStockData():
    a_symbol = ""
    a_dict = {}
    lines_to_file = []
    file1 = open(r"D:\College\IFT 458 - Middleware Programming\Module 5\japi.out","w")

    while ( a_symbol.lower() != "quit" ):
        
        try:
            a_symbol = input("Enter \'quit\' to stop program.\nPlease enter a stock symbol: ")

            if (a_symbol.lower() == 'quit'):
                file1.writelines(lines_to_file)
                file1.close()
                break

            alpha_advantageURL = "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+a_symbol+"&apikey=YAY4BSM9TWRJS6OG&datatype=json"
            connection1 = urllib.request.urlopen(alpha_advantageURL)
            responseString = connection1.read().decode()

            a_dict = json.loads(responseString)
            cur_price = round(float(a_dict['Global Quote']['05. price']), 2)
            lines_to_file.append("The current price of \'"+str(a_symbol)+"\' is: $"+str(cur_price)+"\n")
            print ( "\nThe current price of \'"+str(a_symbol)+"\' is: $"+str(cur_price)+"\n" )
            print ("Stock Quotes retrieved successfully!")

        except Exception:
            print ("Please enter a correct stock symbol.")

getStockData()