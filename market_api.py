# coding: utf-8

import time
import datetime as dt

try:
    import DataAPI
except:
    print 'DataAPI package not loaded ...'


def MktIdxdGet(ticker, tradeDate='20160701'):
    try:
        pre_close = DataAPI.MktIdxdGet(tradeDate=tradeDate.replace('-', ''), ticker=ticker[:6], field=u"closeIndex").closeIndex.loc[0]
    except:
        pre_close = pd.DataFrame.from_csv('000001-20160701.csv').closeIndex.loc[0]

    return pre_close


def MktBarRTIntraDayGet(ticker):    
    try:    
        df = DataAPI.MktBarRTIntraDayGet(securityID=ticker)
    except:
        df = pd.DataFrame.from_csv("000001-20160702.csv")
        now = dt.datetime.now()
        bar_time = '{}:{}'.format(now.hour, now.minute)
        while bar_time not in df.barTime:
            time.sleep(65)
            now = dt.datetime.now()
            bar_time = '{}:{}'.format(now.hour, now.minute)
        
        df = df[df.barTime < bar_time]

    return df
