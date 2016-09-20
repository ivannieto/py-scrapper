#!/usr/bin/python
# encoding=utf-8

'''
Python class to get top 25 websites of a given country from the website alexa.com
'''
from pprint import pprint
import re
from bs4 import BeautifulSoup
import json
import requests

class top_websites:
    # Constructor for google_movie_scrapper class

    def __init__(self, country_ISO_code):

        self.country = country_ISO_code

        url = "http://www.alexa.com/topsites/countries/" + country_ISO_code

        req = requests.get(url)
        textohtml = req.text
        # print(textohtml)
        self.soup = BeautifulSoup(textohtml, "lxml")

    # Function which scraps the movies, theaters, address, generes and showtimes.
    # Returns a list of dictionaries.
    def scrap(self, ):
        soup_object = self.soup
        output = []
        counter = 0

        for desc_cont in soup_object.findAll("li", {"class": re.compile("site-listing")}):
            counter += 1
            append_url = "http://www.alexa.com/"
            resp = {}
            resp['top_rank'] = counter
            resp['top_link'] = append_url + desc_cont.find("a").get('href')

            for descr in desc_cont.findAll("div", {"class": re.compile("description")}):
                if descr is not None:
                    xdescr = descr.get_text().decode('utf-8', 'ignore')
                print(type(xdescr))
                resp['description'] = xdescr

            output.append(resp)

        return output

if __name__ == '__main__':
    country_code = "ES"
    obj = top_websites(country_code)
    stored_data = obj.scrap()
    # pprint(stored_data)
    print("Data for: " + country_code)
    JSONdump = json.dumps(stored_data, indent=4, ensure_ascii=False).encode('utf-8')
    print(JSONdump)