# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 18:48:42 2017

@author: chrzq
"""

import gdax
import pandas as pd

class GdaxAccount(object):
    def __init__(self, key, pp, sk):
        """
        """
        self.key = key
        self.pp = pp
        self.sk = sk
        self.client = None

    def connect_account(self):
        """
        """
        self.client = gdax.AuthenticatedClient(self.key, self.sk, self.pp)

    def get_holdings(self):
        """
        """
        if not(self.client):
            self.connect_account()
            print("I connected")

        lAccts = self.client.get_accounts()
        dfAcct = pd.DataFrame(lAccts)
        for c in ['balance', 'available', 'hold']:
            dfAcct[c] = pd.to_numeric(dfAcct[c])
        self.holdings = dfAcct
        self.acctIdMap = self.holdings.set_index('currency')['id'].to_dict()


    def _accthist_to_df(self, lRet):
        lMaster = []
        for lSubRet in lRet:
            for dEntry in lSubRet:
                dPEntry = {}
                dDetails = dEntry.pop('details')
                dPEntry = {**dEntry, **dDetails}
                lMaster.append(dPEntry)
        return pd.DataFrame(lMaster)
    
    
    def generate_master(self):
        """
        """
        if type(self.acctIdMap) == None:
            self.get_holdings()
        df = pd.DataFrame()
        for k in self.acctIdMap.keys():
            lAcctRet = self.client.get_account_history(self.acctIdMap[k])
            dfIn = self._accthist_to_df(lAcctRet)
            dfIn['wallet'] = k
            df = df.append(dfIn)
        numeric_cols = ['amount', 'balance', 'id', 'trade_id']
        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
        df['created_at'] = pd.to_datetime(df['created_at'])
        df.set_index('created_at', inplace=True)
        return df

        

        



