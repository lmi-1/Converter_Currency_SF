# import requests
# import json
#
# base_key = "USD"
# quote_key = "RUB"
# amount = 100
#
# r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base_key}&&tsyms={quote_key}")
# resp = json.loads(r.content)
# new_price = resp[quote_key] * amount
#
# print(new_price)

a, b = [1]