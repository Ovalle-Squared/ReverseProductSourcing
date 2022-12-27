from bs4 import BeautifulSoup
import requests

"""def print_hi(name):
    print(f'Hi, {name}') # Press Ctrl+F8 to toggle the breakpoint.
"""


def get_title(soup):
    title = soup.find("span", attrs={"id": 'productTitle'})
    if(title is None):
        return "None"
    else: 
        #print(title)
        title_value = title.string
        #print(title_value)
        title_string = title_value.strip()
        return str(title_string)

def get_price(soup):
    productPrice = soup.find("span", attrs={"id": 'price'})
    if(productPrice is None):
      productPrice = soup.find("span", attrs= {"class": 'a-size-base a-color-price offer-price a-text-normal'})
    if(productPrice is None):
        return "0"
    else:
        productPrice_value = productPrice.string
        productPrice_string = productPrice_value.strip()
        return str(productPrice_string)

#def get_compProductsTitle(storeData)


if __name__ == '__main__':
    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 '
                    'Safari/537.36', 'Accept-Language': 'en-US'})

    ### COMPETITOR'S STOREFRONT ###
    storefrontURL = "https://www.amazon.com/s?me=AMNY61XEYVLRP&marketplaceID=ATVPDKIKX0DER" #eventually improve to take list of URLS
    storefrontWebpage =  requests.get(storefrontURL, headers=HEADERS)
    storefrontSoup = BeautifulSoup(storefrontWebpage.content, "lxml")
    compProductsData = storefrontSoup.find('span', attrs={"data-component-type": 's-search-results'})
    #print(compProductsData)
   
    #title#
    compTitleData = compProductsData.find_all('span', attrs= {"class": 'a-size-medium a-color-base a-text-normal'})
    #print(compTitleData)
    compProductTitles = []
    for title in compTitleData:
        compProductTitles.append(title.string.strip())

    #print product list
        for title in compProductTitles:
            print(product)
    

    #URL#
    compProductURLs = []
    for url in compProductsData.find_all('a', href=True):
        if ("javascript:void" not in url['href']) and ("customerReviews" not in url['href']) and ("gp/" not in url['href']) and ("s?i=merchant" not in url['href']) and ("kindle-dbs" not in url['href']) and ("signin?" not in url['href']):
            result = ("https://www.amazon.com" + url['href'])
            if(result not in compProductURLs):
                compProductURLs.append(result)
     
    #print product url
    for url in compProductURLs:
        print(url)
    
    
    
    #price#

    #productURL = "http://www.amazon.com/2023-National-Park-Foundation-Calendar/dp/1728250021/ref=sr_1_1?m=A3B6E79ULPISFM&marketplaceID=ATVPDKIKX0DER&qid=1672105901&s=merchant-items&sr=1-1"
    productWebpage = requests.get(productURL, headers=HEADERS)
    productSoup = BeautifulSoup(productWebpage.content, "lxml")
    if compProductURLs is not None:
        for productURL in compProductURLs:
            productWebpage = requests.get(productURL, headers=HEADERS)
            productSoup = BeautifulSoup(productWebpage.content, "lxml")
            print(get_title(productSoup) + ", " get_price(productSoup) + ", " + productURL) 
            # + ", " + productURL)


    
    ### AMAZON MARKET ### 
    marketProductURLS = []
    for url in compProductURLs:
        index = url.find("ref=sr")
        marketProductURLS.append(url[:index])
    
    for url in marketProductURLS: 
        productWebpage = requests.get(url, headers=HEADERS)
        productSoup = BeautifulSoup(productWebpage.content, "lxml")
        get_price(productSoup)