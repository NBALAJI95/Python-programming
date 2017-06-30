import requests
from bs4 import BeautifulSoup
import os

def main():
    url = "https://en.wikipedia.org/wiki/Android_(operating_system)"
    source_code = requests.get(url)
    plain_text = source_code.text
    # Parsing the html file
    soup = BeautifulSoup(plain_text, "html.parser")
    # Finding all div tags
    result_list = soup.findAll('div')

    # In the list of div tags, we are extracing h1
    for div in result_list:
        h1 = div.find('h1')
        if h1 != None:
            # Printing only text associated with h1
            print(h1.text)

    # Doing the same procedure for body
    result_list1 = soup.findAll('body')
    for b in result_list1:
        print(b.text)

if __name__=='__main__':
    main()