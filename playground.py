import pandas as pd
import requests

baseUrl = "https://tradingeconomics.com/"

# Define user-agent header to trick website into thinking we're a genuine user
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

def teMarkets(datasets):
    """
        Retrieves market data from www.tradingeconomics.com, given an input target dataset.
        Note the data is extracted from the website's HTML, not the actual API, so may be prone to breaking.

        Inputs
        * list of strings representing the target market datasets, eg. ['bonds', 'stocks']
        * strings must be one of the following options:
            - 'bonds'
            - 'commodities'
            - 'crypto'
            - 'currencies'
            - 'stocks'

        Returns a dictionary where the keys are equal to the input strings and the values are either a
        dataframe object if successful or a string of the error code/message if not.

        Note
        * When calling bonds, the data is for government 10Y notes.
        * Duplicates are removed.
    """

    # Initialise the return dictionary
    returnDict = {}

    # Initialise a session object
    session = requests.Session()

    # If statements which append to the return dictionary if True
    if "bonds" in datasets:
        url = "{}{}".format(baseUrl, "bonds")
        request = requests.get(url, headers=headers)
        if request.status_code == 200:
            try:
                tables = pd.read_html(request.text)
                for index, table in enumerate(tables):
                    region = table.columns[1]
                    table = table.rename(columns={table.columns[0]:"Region", region: "Bond"})
                    table["Bond"] = table["Bond"].apply(lambda x: "{} 10Y".format(x))
                    table["Region"] = [region for i in range(len(table))]
                    
                    if index == 0:
                        bondsDf = table
                    else:
                        bondsDf = pd.concat([bondsDf, table])
                bondsDf = bondsDf.drop_duplicates(subset="Bond", keep='last', ignore_index=True)
                returnDict["bonds"] = bondsDf

            except:
                returnDict["bonds"] = "Successful request but error loading data..."
        else:
            returnDict["bonds"] = "Request error: {}".format(request.status_code)

    if "commodities" in datasets:
        url = "{}{}".format(baseUrl, "commodities")
        request = requests.get(url, headers=headers)
        if request.status_code == 200:
            try:
                tables = pd.read_html(request.text)
                for index, table in enumerate(tables):
                    category = table.columns[0]
                    table["Category"] = [category for i in range(len(table))]
                    table = table.rename(columns={category: "Commodity"})
                    
                    if index == 0:
                        commodityDf = table
                    else:
                        commodityDf = pd.concat([commodityDf, table])
                commodityDf = commodityDf.drop_duplicates(subset="Commodity", keep="last", ignore_index=True)
                returnDict["commodities"] = commodityDf
            except:
                returnDict["commodities"] = "Successful request but error loading data"
        else:
            returnDict["commodities"] = "Request error: {}".format(request.status_code)

    if "crypto" in datasets:
        url = "{}{}".format(baseUrl, "crypto")
        request = session.get(url, headers=headers)
        if request.status_code == 200:
            try:
                tables = pd.read_html(request.text)
                for index, table in enumerate(tables):
                    category = table.columns[0]
                    table["Category"] = [category for i in range(len(table))]
                    table = table.rename(columns={table.columns[0]: "Product"})

                    if index == 0:
                        cryptoDf = table
                    else:
                        cryptoDf = pd.concat([cryptoDf, table], ignore_index=True)
                returnDict["crypto"] = cryptoDf
            except:
                returnDict["crypto"] = "Sucessful request but error loading data..."
        else:
            returnDict["crypto"] = "Request error: {}".format(request.status_code)

    if "currencies" in datasets:
        url = "{}{}".format(baseUrl, "currencies")
        request = requests.get(url, headers=headers)
        if request.status_code == 200:
            try:
                tables = pd.read_html(request.text)
                for index, table in enumerate(tables):
                    region = table.columns[1]
                    table = table.rename(columns={table.columns[0]: "Region", table.columns[1]: "CurrencyPair"})
                    table.Region = [region for i in range(len(table))]

                    if index == 0:
                        currencyDf = table
                    else:
                        currencyDf = pd.concat([currencyDf, table])
                currencyDf = currencyDf.drop_duplicates(subset="CurrencyPair", keep='last', ignore_index=True)
                returnDict["currencies"] = currencyDf
            except:
                returnDict["currencies"] = "Successful request but error loading data..."
        else:
            returnDict["currencies"] = "Request error: {}".format(request.status_code)
 
    if "stocks" in datasets:
        url = "{}{}".format(baseUrl, "stocks")
        request = requests.get(url, headers=headers)
        if request.status_code == 200:
            try:
                tables = pd.read_html(request.text)
                for index, table in enumerate(tables):
                    region = table.columns[1]
                    table = table.rename(columns={table.columns[0]: "Region", table.columns[1]: "Index"})
                    table.Region = [region for i in range(len(table))]

                    if index == 0:
                        stocksDf = table
                    else:
                        stocksDf = pd.concat([stocksDf, table])
                stocksDf = stocksDf.drop_duplicates(subset="Index", keep='last', ignore_index=True)
                returnDict["stocks"] = stocksDf
            except:
                returnDict["stocks"] = "Successful request but error loading data..."
        else:
            returnDict["stocks"] = "Request error: {}".format(request.status_code)
    return returnDict

# EXAMPLE
if __name__ == "__main__":
    data = tradingEconomics(["crypto"])
    print(data["crypto"]["crypto"])
