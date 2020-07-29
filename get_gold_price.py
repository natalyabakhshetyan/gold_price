import requests
from bs4 import BeautifulSoup
import time


# the function returns gold ask price
def get_gold_price():

    #get page and create soup object
    page = requests.get("https://www.kitco.com/charts/livegold.html")
    soup = BeautifulSoup(page.content, "html.parser")

    # getting price string
    ask_price = soup.find('div', {'id': 'sp-container'}).\
        find('div', {'class': 'data-blk ask'}).text

    # formatting price string to extract number only and converting to float
    ask_price_float = float(ask_price.replace(',', '').replace('Ask', ''))
    return ask_price_float

def main():
    # execute get_gold_price() every 5 minutes
    while True:
        get_gold_price()
        time.sleep(300)

if __name__ == '__main__':
    main()



