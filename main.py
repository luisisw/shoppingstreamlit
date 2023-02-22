import streamlit as st
import pandas as pd
import numpy as np
from serpapi import GoogleSearch

params = {
  "api_key": "c934fecd4a47ed75bae34f1b6c055c7ba070e6777a737d414c4d8ddaeaba1024",
  "engine": "google_shopping",
  "google_domain": "google.com.br",
  "q": "iphone",
  "hl": "pt",
  "gl": "br",
  "location": "Brazil"
}

search = GoogleSearch(params)
results = search.get_dict()
# print(results)

st.title('Test')
