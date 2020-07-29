**About**

The script executes every 5 minutes and returns gold ask price
scraped from https://www.kitco.com/charts/livegold.html 

**Requirements**

\>= Python 3.6

beautifulsoup4==4.9.1

bs4==0.0.1

certifi==2020.6.20

chardet==3.0.4

idna==2.10

regex==2020.7.14

requests==2.24.0

soupsieve==2.0.1

urllib3==1.25.10

**Setting up and Running**

1. Install virtualenv package: `pip install virtualenv`
2. Create the virtual environment: `virtualenv mypython`
3. Activate the virtual environment: `source mypython/bin/activate`
4. Install requirements.txt: `pip install -r requirements.txt`
5. Running: `python get_gold_price.py`
6. Deactivating virtual environment: `deactivate`

**Data Sources**

- KitCo: https://www.kitco.com/charts/livegold.html - Ask price