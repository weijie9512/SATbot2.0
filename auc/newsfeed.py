from newsapi import NewsApiClient
from pandas.io.json import json_normalize
import pandas as pd


api_key = "188b1d9e2e794b0e98cb08db39f8d2e5"
newsapi = NewsApiClient(api_key=api_key)
