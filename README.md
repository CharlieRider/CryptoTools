# CryptoTools
a few cryptools


## account_manager
Holds your account linkups

exchanges set up:

    gdax

exchanges to be set up:
    
    binance
    (taking requests)
    

### GdaxAccount
    GdaxAccount(key,pp,sk)

parameters:
    
    key = account key found on gdax
    pp = pass phrase from gdax
    sk = 64 char secret from account api linking
    
#### Example
```python
import pandas as pd
from gdaxaccount import GdaxAccount

key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
pp = 'xxxxxxxxxxx'
sk = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# Connect Account
gA = GdaxAccount(key,pp,sk)

# Get Current Holdings
gA.get_holdings()

# Get All Trades
df = gA.generate_master()
```
