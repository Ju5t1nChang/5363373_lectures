import os
import pandas as pd

import config as cfg

def read_prc_csv(tic):
    tic_pth = os.path.join(cfg.DATADIR, f'{tic.lower()}_prc.csv')

    prc = pd.read_csv(tic_pth)
    prc.loc[:, 'Date'] = pd.to_datetime(prc['Date'], format='%Y-%m-%d')
    df = prc.set_index('Date')

    df.columns = [column.lower().replace(" ", "_") for column in df.columns]

    return df

def mk_prc_df(tickers, prc_col='adj_close'):
    tickers = [tic.lower() for tic in tickers]
    for n in range(len(tickers)):
        cnts = read_prc_csv(tickers[n])[prc_col]
        if n == 0:
            data = cnts
        else:
            df = pd.concat([data, cnts], axis=1)
    df.columns = tickers
    return df


"""Uncompleted"""
def mk_ret_df(prc_df):
    return

tickers = ['AAPL', 'TSLA']
prc_df = mk_prc_df(tickers, prc_col='adj_close')


