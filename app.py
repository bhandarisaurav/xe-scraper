from flask import Flask, request,render_template , make_response, send_file
import requests
import pandas as pd
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scrape', methods = ['POST'])
def scrape():
    
    def get_url(date):
        url = "https://www.xe.com/currencytables/?from=CAD&date=" + date + "#table-section"
        return url

    df = pd.DataFrame()
    
    start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
    end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
    print(start_date, end_date)

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
    return send_file("currency.csv", as_attachment=True)
    