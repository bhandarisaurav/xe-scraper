# xe.com curency data scraper

### This is a simple flask app that scrapes xe.com for currency data and return the csv file.

#### Deployed on render.com: [xe-scraper.onrender.com](https://xe-scraper.onrender.com/)

#### How to run the app:
1. Clone the repo
2. Install the requirements
3. Run the app

```bash
https://github.com/bhandarisaurav/xe-scraper.git
cd xe-scraper
pip install -r requirements.txt
# gunicorn --workers=number_of_workers app:app
gunicorn --workers=2 app:app
```