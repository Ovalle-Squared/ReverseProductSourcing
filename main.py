from bs4 import BeautifulSoup
import requests

"""def print_hi(name):
    print(f'Hi, {name}') # Press Ctrl+F8 to toggle the breakpoint.
"""


def get_title(url):
    title = soup.find("span", attrs={"id": 'productTitle'})
    #print(title)
    title_value = title.string
    #print(title_value)
    title_string = title_value.strip()
    return str(title_string)

#def get_compProductsTitle(storeData)


if __name__ == '__main__':
    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 '
                    'Safari/537.36', 'Accept-Language': 'en-US'})
    ### COMPETITOR'S STOREFRONT ###
    storefrontURL = "https://www.amazon.com/s?me=A3B6E79ULPISFM&marketplaceID=ATVPDKIKX0DER" #eventually improve to take list of URLS
    storefrontWebpage =  requests.get(storefrontURL, headers=HEADERS)
    storefrontSoup = BeautifulSoup(storefrontWebpage.content, "lxml")
    compProducts = storefrontSoup.find('span', attrs={"data-component-type": 's-search-results'})
   
    #title#
    compTitleData = compProducts.find_all('span', attrs= {"class": 'a-size-medium a-color-base a-text-normal'})
    #print(compTitleData)
    compProductTitles = []
    for item in compTitleData:
        compProductTitles.append(item.string.strip())

    """#print product list
        for product in compProductTitles:
            print(product)
    """

    #price#
    

    """productURLS_value = productURLs.string
    productURLs_string = productURLS_value.strip()
   """
    
    """### SEARCH PRODUCT ON AMAZON ### 
    productURL = "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
    #Grab weekly ad url
    #Search soup for aria-label
    #Search Lowes listings based on aria-labels
    webpage = requests.get(productURL, headers=HEADERS)
    productSoup = BeautifulSoup(webpage.content, "lxml")
    #print(soup)
    productTitle = get_title(productURL)
    #print(productTitle)
    """
