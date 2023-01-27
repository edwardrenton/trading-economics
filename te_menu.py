import tradingEconomics
from tradingEconomics import *
import te_datacleaner


def main():
	tradingEconomics.teMarkets()
	te_datacleaner.main()


if __name__ in "__main__":
	data_currencies = teMarkets(["currencies"])
	data_stocks = teMarkets(["stocks"])
	data_commodities = teMarkets(["commodities"])
	data_bonds = teMarkets(["bonds"])
	data_crypto = teMarkets(["crypto"])
