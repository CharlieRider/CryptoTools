# -*- coding: utf-8 -*-
"""
Testing account grabbing for gdaxaccount

"""

import pandas as pd
from gdaxaccount import GdaxAccount


key='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
pp = 'xxxxxxxxxxx'
sk = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

gA = GdaxAccount(key,pp,sk)
gA.get_holdings()

df = gA.generate_master()
print("Grabbed Account Successfully, inside df variable")