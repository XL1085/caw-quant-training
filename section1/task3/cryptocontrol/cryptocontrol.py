
from crypto_news_api import CryptoControlAPI
import requests
import pandas as pd
import json


with open('./key.json') as f:
    api_key = json.load(f)


api = CryptoControlAPI(api_key['key'])
proxyApi = CryptoControlAPI(api_key['key'], "http://cryptocontrol_proxy/api/v1/public")

# Enable the sentiment datapoints
api.enableSentiment()

# All the news data are in News.csv
# Get top news
news = api.getTopNews()
df = pd.DataFrame(data=news)
df['type']='Top News'
df.to_csv("./News.csv", encoding='utf-8', index=0)

# get latest russian news
ru = api.getLatestNews("ru")
dfr = pd.DataFrame(data=ru)
dfr['type']='Russian News'
dfr.to_csv("./News.csv", encoding='utf-8', mode='a', header=0, index=0)

# get top bitcoin news
bitcoin = api.getTopNewsByCoin("bitcoin")
dfb = pd.DataFrame(data=bitcoin)
dfb['type']='bitcoin'
dfb.to_csv("./News.csv", encoding='utf-8', mode='a', header=0, index=0)

# get top EOS tweets
eos = api.getTopTweetsByCoin("eos")
dfe=pd.DataFrame(data=eos)
dfe.to_csv("./eos.csv", encoding='utf-8')

# get top Ripple reddit posts
ripple = api.getLatestRedditPostsByCoin("ripple")
dfr = pd.DataFrame(data=ripple)
dfr.to_csv("./ripple.csv", encoding='utf-8')

# get reddit/tweets/articles in a single combined feed for NEO
neo = api.getTopFeedByCoin("neo")
dfn = pd.DataFrame(data=neo)
dfn.to_csv("./neo.csv", encoding='utf-8')

# get latest reddit/tweets/articles (seperated) for Litecoin
litecoin = api.getLatestItemsByCoin("litecoin")
dfl = pd.DataFrame(data=litecoin)
dfl.to_csv("./litecoin.csv", encoding='utf-8')

# get details (subreddits, twitter handles, description, links) for ethereum
ethereum = api.getCoinDetails("ethereum")
dft = pd.DataFrame.from_dict(data=ethereum, orient='index')
dft.to_csv("./ethereum.csv", encoding='utf-8')