#import requests
#import time
#import math
#import os

from poloniex import Poloniex

# Get private API keys
apiKeyFile = open("POLONIEX_API_KEY", "r")
apiKey = apiKeyFile.read()
apiKeyFile.close()

apiSecretFile = open("POLONIEX_SECRET", "r")
apiSecret = apiSecretFile.read()
apiSecretFile.close()

print(apiKey)
print(apiSecret)

# Create private API link
polo = Poloniex(apiKey, apiSecret)

## Testing private API link
balances = polo.returnBalances()
print(balances)
