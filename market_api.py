# coding: utf-8

import time
import datetime as dt
import pandas as pd

try:
    import DataAPI
except:
    print 'DataAPI package not loaded ...'


def MktIdxdGet(ticker, tradeDate='20160701'):
    pre_close = DataAPI.MktIdxdGet(tradeDate=tradeDate.replace('-', ''), ticker=ticker[:6], field=u"closeIndex").closeIndex.loc[0]

    return pre_close


def MktBarRTIntraDayGet(ticker):    
    df = DataAPI.MktBarRTIntraDayGet(securityID=ticker)

    return df


def MktIdxdGetDemo(ticker, tradeDate='20160701'):
    pre_close = pd.DataFrame.from_csv('000001-20160701.csv').closeIndex.loc[0]

    return pre_close


def MktBarRTIntraDayGetDemo(ticker):    
    df = pd.DataFrame.from_csv("000001-20160702.csv")
    return df