# SOURCE

import os
from tradingEconomics import *


def main():
	df_currencies_to_csv(assets)


def df_currencies_to_csv(assets):
	"""
	param assets list of csv to be imported to csv file for future sqlite ingestion
	"""
	df_currencies = data_currencies[assets]
	
	os.makedirs('data/te_assets', exist_ok=True)
	df_currencies.to_csv('data/te_assets/te_currencies.csv')


"""
def df_stocks_to_csv(assets):
	df_stocks = data_stocks[assets]
	
	os.makedirs('data/te_assets', exist_ok=True)
	df_stocks.to_csv('data/te_assets/te_stocks.csv')
"""
	

if __name__ in "__main__":
	assets = 'currencies'
	# TODO iterate through the assets, refactor or do one at a time for future ease of import and debugging
	# TODO setup .env file for pathing, user name and pw.
	# data_currencies = teMarkets(["currencies"])
	# data_stocks = teMarkets(["stocks"])
	# data_commodities = teMarkets(["commodities"])
	# data_bonds = teMarkets(["bonds"])
	# data_crypto = teMarkets(["crypto"])
	main()