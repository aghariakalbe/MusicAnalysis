# from bs4 import BeautifulSoup as soup  # HTML data structure
# from urllib.request import urlopen as uReq  # Web client
# import json


# # URl to web scrap from.
# # in this example we web scrap graphics cards from Newegg.com
# page_url = "https://tabs.ultimate-guitar.com/tab/ed-sheeran/perfect-chords-1956589"

# # opens the connection and downloads html page from url
# uClient = uReq(page_url)
# data = json.load(uClient)
# # parses html into a soup data structure to traverse html
# # as if it were a json data type.
# page_soup = soup(uClient.read(), "html.parser")
# uClient.close()

# finds each product from the store page
# bowlgames = page_soup.findAll("span",{"class":"_3rlxz"})
# print(bowlgames)
# name the output file to write to local disk
""" out_filename = "ult.csv"
# header of csv file to be written
headers = "bowl,home,away,home score,away score \n" """

# opens file, and writes headers
# f = open(out_filename, "w")
 #f.write(headers)
# file1 = open("MyFile.txt","a")
# file1.write(str(page_soup))
# file1.close
# loops over each product and grabs attributes about
# each product
'''for bowlgame in bowlgames:
    # Finds all link tags "a" from within the first div.
    make_rating_sp = bowlgame.div.select("a")

    # Grabs the title from the image title attribute
    # Then does proper casing using .title()
    brand = make_rating_sp[0].img["title"].title()

    # Grabs the text within the second "(a)" tag from within
    # the list of queries.
    product_name = bowlgame.div.select("a")[2].text

    # Grabs the product shipping information by searching
    # all lists with the class "price-ship".
    # Then cleans the text of white space with strip()
    # Cleans the strip of "Shipping $" if it exists to just get number
    shipping = bowlgame.findAll("li", {"class": "price-ship"})[0].text.strip().replace("$", "").replace(" Shipping", "")

    # prints the dataset to console
    print("brand: " + brand + "\n")
    print("product_name: " + product_name + "\n")
    print("shipping: " + shipping + "\n")

    # writes the dataset to file
    f.write(brand + ", " + product_name.replace(",", "|") + ", " + shipping + "\n")

f.close()  # Close the file'''
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



url = 'https://tabs.ultimate-guitar.com/tab/jason-mraz/im-yours-chords-373896'

BrowserOptions = Options()
BrowserOptions.add_argument("--headless")
Browser = webdriver.Chrome(executable_path=r'C:\Users\aghar\Downloads\chromedriver_win32\chromedriver.exe',options=BrowserOptions)
Browser.get(url)

html_source_code = Browser.execute_script("return document.body.innerHTML;")

soup = BeautifulSoup(html_source_code, 'html.parser')
links = soup.findAll("span",class_= "_3PpPJ OrSDI")
print(links)
for item in links:
    print("Chords: ", item.text)