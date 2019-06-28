from bs4 import BeautifulSoup
import requests

# List of item names to search on eBay
# name_list = ["Ramen", "Monster Hunter World", "Adhesive page markers", "Calculator", "arduino", "gtx 1070",
#              "bluetooth headphones", "coffee machine", "sweet tea", "Python textbook"]

name_list = ["Fuel pump EP240PIN", "Fuel pump E240PIN", "Fuel pump E240P", "Fuel pump AMJ3240PIN", "Fuel pump GEP240PIN", "Fuel pump EP240", "Fuel pump FP-E240", "Fuel pump 56-IS-240WR"]


# Returns a list of urls that search eBay for an item
def make_urls(names):
    # eBay url that can be modified to search for a specific item on eBay
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR11.TRC2.A0.H0.XIp.TRS1&_nkw="
    # List of urls created
    urls = []

    for name in names:
        # Adds the name of item being searched to the end of the eBay url and appends it to the urls list
        # In order for it to work the spaces need to be replaced with a +
        urls.append(url + name.replace(" ", "+"))

    # Returns the list of completed urls
    return urls


# Scrapes and prints the url, name, and price of the first item result listed on eBay
def ebay_scrape(urls):
    for url in urls:
        # Downloads the eBay page for processing
        res = requests.get(url)
        # Raises an exception error if there's an error downloading the website
        res.raise_for_status()
        # Creates a BeautifulSoup object for HTML parsing
        soup = BeautifulSoup(res.text, 'html.parser')
        # Scrapes the item link
        #link = soup.find("a", {"class": "s-item__link"}). #need to figure out how to grab the href
        # Scrapes the first listed item's name
        name = soup.find("h3", {"class": "s-item__title"}).get_text(separator=u" ")
        name = soup.find("h3", {"class": "s-item__title"}).get_text(strip=True)

        # Scrapes the first listed item's price
        price = soup.find("span", {"class": "s-item__price"}).get_text()

        # Prints the url, listed item name, and the price of the item
        print(url)
        print("Item Name: " + name)
        print("Price: " + price + "\n")


# Runs the code
# 1. Make the eBay url list
# 2. Use the returned url list to search eBay and scrape and print information on each item
ebay_scrape(make_urls(name_list))