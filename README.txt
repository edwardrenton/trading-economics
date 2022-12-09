Trading Economics Scraper
===========================
Retrieves market data from www.tradingeconomics.com, given an input target
dataset. Note the data is extracted from the website's HTML, not the actual
API, so may be prone to breaking. Actual API is behind a paywall.

Inputs
* list of strings representing the target datasets, eg. ['bonds', 'stocks']
* strings must be one of the following options:
  - 'bonds'
  - 'commodities'
  - 'crypto'
  - 'currencies'
  - 'stocks'

Returns a dictionary where the keys are equal to the input strings and the
values are either a dataframe object if successful or a string of the error
code/message if not.

Note
* When calling bonds, the data is for government 10Y notes.
* Duplicates are removed.