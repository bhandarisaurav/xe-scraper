import requests
import pandas as pd
from datetime import datetime, timedelta

def get_url(date):
    url = "https://www.xe.com/currencytables/?from=CAD&date=" + date + "#table-section"
    return url

df = pd.DataFrame()

start_date = datetime(2023, 11, 1)
end_date = datetime(2024, 5, 5)

delta = timedelta(days=1)

current_date = start_date
while current_date <= end_date:
    date = current_date.strftime('%Y-%m-%d')
    current_date += delta
    
    html = requests.get(get_url(date)).content
    df_list = pd.read_html(html)[0]
    df_list['Date'] = date
    df_list['Units per CAD'] = df_list['Units per CAD'].apply(lambda x: round(x, 7))
    df_list['CAD per unit'] = df_list['CAD per unit'].apply(lambda x: round(x, 7))
    
    df = pd.concat([df, df_list], ignore_index=True)
    print(date)
    
df.to_csv('currency.csv', index=False)