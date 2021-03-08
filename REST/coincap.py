import http.client
import mimetypes

conn = http.client.HTTPSConnection("api.coincap.io")
payload = ''
headers = {}

def timeToUNIX(timeStamp):
  import time
  import datetime

  return time.mktime(datetime.datetime.strftime(timeStamp, "%Y/%m/%d-%H:%M:%S"))

   

# @auhtor: mangose10
#
# input(s):
# @interval - time between candlestick data. 'm1', 'm5', 'm15', 'm30', 'h1', 'h2', 'h4', 'h8', 'h12', 'd1', 'w1'
# @baseID - queried stock
# @quoteId (optional) - currency of stock
# @start (optional) - start time of query range in 'yy/mm/dd-hh:mm:ss' format
# @end (optional) - end time of query range in 'yyyy/mm/dd-hh:mm:ss' format
#
# output:
# json object - 'data' array containing 'high', 'low', 'open', 'close', 'volume', 'period'
def getCandles(interval, baseId, exchange="poloniex", quoteId="USD", start=0, end=0):

  if (start > end):
    return {'status' : 'Invalid time range.'}

  reqString = "/v2/candles?exchange="+exchange+"&interval="+interval+"&baseId="+baseId+"&quoteId="+quoteId
  reqString += "&start="+start if start > 0 else ""
  reqString += "&end="+end if end > 0 else ""

  conn.request("GET", reqString)

  res = conn.getresponse()
  data = res.read()
  return (data.decode("utf-8"))

def getMarkets():


  conn.request("GET", "/v2/markets", payload, headers)

  res = conn.getresponse()
  data = res.read()
  return (data.decode("utf-8"))

def getExchanges(id="none"):

  reqString = "/v2/exchanges"
  reqString += "/"+id if id=="none" else ""

  conn.request("GET", reqString, payload, headers)
  res = conn.getresponse()
  data = res.read()
  return (data.decode("utf-8"))

def getRates():
  return ("")