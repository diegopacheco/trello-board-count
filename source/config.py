# Which boards / lists to count
BOARDS = ['supply tax','icatu - celula','icatu - namedida mobile','ilegra: bradesco - wallet','jd baseline','thomson board - cortellis','visionboards - phase 1','vendita']
LISTS = ['code review']

CONSUMER_KEY = '5c212aec85d915429623d7dc30c7c412'
CONSUMER_SECRET = '456e7f137ad7502d2b069b5c48f6fcf96aa9cee3751ce8d6f6e39a321f1a3c78'

request_token_url = 'https://trello.com/1/OAuthGetRequestToken'
authorize_url = 'https://trello.com/1/OAuthAuthorizeToken'
access_token_url = 'https://trello.com/1/OAuthGetAccessToken'

# encoding setup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
