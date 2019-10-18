from newsapi import NewsApiClient
import secret

# Init
newsapi = NewsApiClient(api_key=secret.api_key)

# /v2/top-headlines
top_headlines = newsapi.get_sources()
print(top_headlines)
