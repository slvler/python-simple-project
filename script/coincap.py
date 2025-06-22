import requests

class CoinCap:
    def __init__(self, base_url, api_key):
        self.__base_url = base_url
        self.__api_key = api_key

    def get_asset(self, endpoint):
        url = f"{self.__base_url}/{endpoint}"
        result = requests.get(url, params={"apiKey": self.__api_key})
        try:
            if result.status_code == 200:
                return result.json()
            else:
                print(f"Error: {result.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def get_asset_slug(self, endpoint, slug):
        url = f"{self.__base_url}/{endpoint}/{slug}"
        result = requests.get(url, params={"apiKey": self.__api_key})
        try:
            if result.status_code == 200:
                return result.json()
            else:
                print(f"Error: {result.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None


    def get_asset_slug_market(self, endpoint, slug):
        url = f"{self.__base_url}/{endpoint}/{slug}/markets"
        result = requests.get(url, params={"apiKey": self.__api_key})
        try:
            if result.status_code == 200:
                return result.json()
            else:
                print(f"Error: {result.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def get_asset_slug_history(self, endpoint, slug, params):
        url = f"{self.__base_url}/{endpoint}/{slug}/history"
        prt = dict({'apiKey': self.__api_key})
        prt.update(params)
        result = requests.get(url, params=prt)
        try:
            if result.status_code == 200:
                return result.json()
            else:
                print(f"Error: {result.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None


    def get_exchanges(self, endpoint, params):
        url = f"{self.__base_url}/{endpoint}"
        prt = dict({"apiKey": self.__api_key})
        prt.update(params)
        result = requests.get(url, params=prt)
        try:
            if result.status_code == 200:
                return result.json()
            else:
                print(f"Error: {result.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

    def get_exchange_slug(self, endpoint, slug):
        url = f"{self.__base_url}/{endpoint}/{slug}"

        prt = dict({"apiKey": self.__api_key})
        result = requests.get(url, params=prt)

        try:
            if result.status_code == 200:
                return result.json()
            else:
                print(f"Error: {result.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None


    def get_market(self, endpoint, params):
        url = f"{self.__base_url}/{endpoint}"
        prt = dict({"apiKey": self.__api_key})
        prt.update(params)
        result = requests.get(url, params=prt)

        try:
            if result.status_code == 200:
                return result.json()
            else:
                print(f"Error: {result.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None


    def get_rates(self, endpoint, params):
        url = f"{self.__base_url}/{endpoint}"
        prt = dict({"apiKey": self.__api_key})
        prt.update(params)
        result = requests.get(url, params=prt)

        try:
            if result.status_code == 200:
                return result.json()
            else:
                print(f"Error: {result.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None


    def get_rates_slug(self, endpoint, slug):
        url = f"{self.__base_url}/{endpoint}/{slug}"
        prt = dict({"apiKey": self.__api_key})
        result = requests.get(url, params=prt)

        try:
            if result.status_code == 200:
                return result.json()
            else:
                print(f"Error: {result.status_code}")
                return None
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None

#rest.coincap.io/v3/assets?apiKey=YourApiKey (New Api)

ccoin = CoinCap("https://rest.coincap.io","api_key")
#result = ccoin.get_asset("v3/assets")
#result = ccoin.get_asset_slug("v3/assets", "bitcoin")
#result = ccoin.get_asset_slug_market("v3/assets", "bitcoin")
#result = ccoin.get_asset_slug_history("v3/assets", "bitcoin", {'interval': 'm5', 'start': '', 'end': ''})
#result = ccoin.get_exchanges("v3/exchanges", {"limit": "10", "offset":"0"})
#result = ccoin.get_exchange_slug('v3/exchanges','binanceus')
# result = ccoin.get_market('v3/markets',
#                           {
#                               'exchangeId':'binanceus',
#                               'baseSymbol':':',
#                               'baseId':':',
#                               'quoteSymbol':':',
#                               'quoteId':':',
#                               'assetSymbol':':',
#                               'assetId':':',
#                               'limit':':',
#                               'offset':':',
#                           })
#result = ccoin.get_rates('v3/rates', {'ids': 'bitcoin'})
#result = ccoin.get_rates_slug('v3/rates', 'bitcoin')
#print(result)