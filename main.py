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


if __name__ == '__main__':
    HEADERS = ({'User-Agent':
                    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 '
                    'Safari/537.36', 'Accept-Language': 'en-US'})
    URL = "https://www.amazon.com/Sony-PlayStation-Pro-1TB-Console-4/dp/B07K14XKZH/"
    #Grab weekly ad url
    #Search soup for aria-label
    #Search Lowes listings based on aria-labels
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "lxml")
    #print(soup)
    title = get_title(URL)
    #print(title)
