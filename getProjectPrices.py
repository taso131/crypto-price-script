from locale import currency
import requests
import re

coingeckoUrl = "https://api.coingecko.com/api/v3"
coingeckoavailableApiCalls = {
	'ping' : '/ping',
	'cryptocoins' : '/coins/list',
	'coinprice' : '/simple/price',
	'comparisoncoins' : '/simple/supported_vs_currencies'
}
coingeckoHeaders = {
	'accept' : 'application/json',
	'ids' : 'rubic',
	'vs_currencies' : 'eur'
}


def CoinGeckoCheckStatusCode():
	pingRequestReply = requests.get(coingeckoUrl + coingeckoavailableApiCalls['ping'])
	HttpCodeOk = 200
	if pingRequestReply.status_code == HttpCodeOk:
		print('CoinGecko is online and replies:')
		print(pingRequestReply.text)
	else:
		print('CoinGecko is offline. No Response.\nCode:' + str(pingRequestReply))
		exit()

def CoinGeckoGetCoinGeckoComparisonCurrencies():
	comparisonCoinsRequest = requests.get(coingeckoUrl + coingeckoavailableApiCalls['comparisoncoins'], params=coingeckoHeaders['accept'])
	coinNameRegEx = r'\"(.{3,4})\"'
	comparisonCoinsMatching = re.findall(coinNameRegEx, comparisonCoinsRequest.text)
	for i in range(0, len(comparisonCoinsMatching), 5):
		print(comparisonCoinsMatching[i : i + 5])

def CoinGeckoGetCoinGeckoAvailableCoins():
	availableCoinRequestReply = requests.get(coingeckoUrl + coingeckoavailableApiCalls['cryptocoins'], params=coingeckoHeaders['accept'])
	print(availableCoinRequestReply.text)

def CoinGeckoPrintRubicCoinPrice():
	coinPrice = requests.get(coingeckoUrl + coingeckoavailableApiCalls['coinprice'], params=coingeckoHeaders)
	print(coinPrice.text)

if __name__ == '__main__':
	print("CryptoPrice Custom Tracker v0.1. \n")
	CoinGeckoCheckStatusCode()
	print("\n")
	#CoinGeckoGetCoinGeckoAvailableCoins()
	#CoinGeckoGetCoinGeckoComparisonCurrencies()
	print("Prices are:")
	CoinGeckoPrintRubicCoinPrice()


