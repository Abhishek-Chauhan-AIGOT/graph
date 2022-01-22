from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.ad import Ad
from facebook_business.api import FacebookAdsApi

access_token = 'EAAKcvKOwbCIBAOwqnCuwyQkOAdBIbnZBWOQHq8RXA9aFsSZAH8S2SYs0AnEfMLdQloY2nI47kSxYOu0JNZAmGmg6bwCZBKewzAOhRjBDGv4wQxPqstOZB7D5fl91gT3JZBQJVbb2FlSeEgCl3kgqDZA7pYYKZB7t0n3C4epxxZARtca9VQar7hn53NgunNpCGqjWZCZCKIH7nZBnuQZDZD'
app_secret = 'app-secret'
app_id = '735283967454242'
id = 'ad-account-id'
FacebookAdsApi.init(access_token=access_token)

fields = [
]
params = {
  'name': 'My Python Ad',
  'adset_id': 'ad-set-id',
  'creative': {'creative_id': 'creative-id'},
  'status': 'PAUSED',
}

print(AdAccount(id).create_ad(fields=fields,params=params,))


