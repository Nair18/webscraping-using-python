# code is to scrape the information regarding the graphics card from a webpage
#using python lib beautifulsoup which is helpful in pulling out data from xml and html files

from urllib import urlopen as ureq
from bs4 import BeautifulSoup as soup
#get the url of the webpage to be scraped...
my_url = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20cards"
#download the webpage using ureq..
uclient = ureq(my_url)
# open the uclient file and read and save it in an object page_html
page_html = uclient.read()

# parse the html webpage using bs4 package of python
page_soup = soup(page_html,"html.parser")
# now from the parsed file i want to scrape the information of all the graphics card available
#so for i visit the url and the inspect element on the graphics - card 
#i find that they inside the div tag having the class name item-container
#so i use findAll() of beautifulsoup module to find all div tags having class="item-container"
#and save in the form of a list in containers, to see how many graphics i have in the object use len(containers)
#and it displays the number of graphics cards.
containers = page_soup.findAll("div",{"class":"item-container"})
#now iterate through the list and scrap the required details -(comp-name,product-name,price)
for container in containers:
#among all informations of graphics card i want the 'company name' of graphics card then cost
	brand = container.div.div.a.img["title"]
# find all the a tags having class = item-title where the description of the graphics card is mentioned
#it will return a singleton list
	title_container = container.findAll("a",{"class":"item-title"})
#from that singleton list i extract the text which is the description
	product_desc = title_container[0].text
#next thing i want to scrap is price which is written in <li> with class=price-current
#it will return a singleton list in that navigate to strong tag and sup tag one by one
#then lastly convert it to text and save it in an object price1 and price2

	price = container.findAll("li",{"class":"price-current"})
	price1 = price[0].strong.text
	price2 = price[0].sup.text
#lastly print all the objects in to the console..... 
	print("brand: " + brand)
	print("product_name: " + product_desc)
	print("price: $"+ price1 + "" + price2)
	print("==========================================================================================");

