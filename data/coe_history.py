import requests
import json
import pandas as pd
from langchain_community.document_loaders import DataFrameLoader

response = requests.get(
    "https://api-open.data.gov.sg/v1/public/api/datasets/d_69b3380ad7e51aff3a7dcc84eba52b8a/initiate-download",
    headers={"Content-Type":"application/json"},
    json={}
)
API_data = response.json()
Data_URL=API_data['data']['url']
#COE_data = pd.read_csv(Data_URL)

#print(COE_data)
#print(type(COE_data))

'''
records = COE_data['result']['records']
COE_data_df = pd.DataFrame(records)
#print(COE_data_df)

df_loader = DataFrameLoader(COE_data_df, page_content_column="premium")
df_document=df_loader.load()
print(df_document)
'''