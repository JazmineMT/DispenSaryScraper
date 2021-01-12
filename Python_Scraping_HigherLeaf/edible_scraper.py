from urllib.request import urlopen 
from bs4 import BeautifulSoup

url_to_scrape = "https://store.higherleaf.com/kirkland/edible"

request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()


html_soup = BeautifulSoup(page_html, 'html.parser')

edible_items = html_soup.find_all('a', class_="product-card justify-between items-center ma2 relative")

filename = 'edible_higherLeaf.csv'
f = open(filename, 'w')

headers = 'Id , Brand , Title, Type_THC , Price, Amount, Image Link \n'
count = 0 
f.write(headers)

for edible in edible_items:
    count += 1
    item_id = count 
    brand = edible.find('p', class_= "tc ma0 mt1 f7").text
    title = edible.find('b', class_= "tc mv2 f5").text
    type_THC = edible.find('p', class_= "tc mv1 f7").text
    price = edible.find('p', class_= "tc mv1 f5").text
    amount = edible.find('p', class_= "tc mv1 f6").text
    image = edible.find('img')

    
    f.write(str(item_id) + "," + brand + ","+ title + ',' + price +  "," + type_THC + ","+ amount + "," + str(image['src']) +"\n")
    
    
f.close()