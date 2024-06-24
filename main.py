import random
import time
import sys
import os
import json

from maps.gmaps import GoogleMapsAPI
from scraper.scraper import WebsiteScraper
from data_parser.parser import DataParser
from ai.ai import OpenAI

# openai
# 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

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def start_bot(businessType, location, radius=1000, dev=False, prospect=False, email=False):
    GMAPS_API_KEY = None
    if 'GMAPS_API_KEY' in os.environ:
        GMAPS_API_KEY = os.environ['GMAPS_API_KEY']
    else:
        print("No Google Maps API key found")
        GMAPS_API_KEY = input("Enter Google Maps API key: ")

    gmaps = GoogleMapsAPI(GMAPS_API_KEY)
    
    OPENAI_API_KEY = None
    if 'OPENAI_API_KEY' in os.environ:
        OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
    else:
        print("No OpenAI API key found")
        OPENAI_API_KEY = input("Enter OpenAI API key: ")
        
    ai = OpenAI(OPENAI_API_KEY)

    businesses = json.load(open("output/businesses.json", "r")) if dev else gmaps.search_businesses(businessType, f"{businessType} in {location}", radius)
    print(f"Found {len(businesses)} businesses")

    # * Attempt to get more contact info (email/social media) if there is a website
    for business in businesses:
        if business.get('website') != None:
            scraper = WebsiteScraper()

            # * Load website address and try find email on page
            if(scraper.load(business['website']) == False):
                continue

            scraper.find_email_address()
            scraper.find_social_medias()

            # * If email not found, try find contact page 
            if(scraper.email_address == None and scraper.email_protected == False):
                scraper.find_contact_page()

                # * If contact page found, load contact page and try find email on page
                if(scraper.contact_page_url != None):
                    scraper.load(scraper.contact_page_url)
                    scraper.find_email_address()

            if(scraper.email_address != None):
                business['email'] = scraper.email_address
            
            if(len(scraper.social_media_urls) > 0):
                business['social_media_urls'] = scraper.social_media_urls
    
    # * Use Chat GPT to write prospecting emails
    # ! NOT TESTED
    if(prospect):
        for business in businesses:
            business['prospecting_email_template'] = ai.getCompletion("Website services", business['name'], business['type'], location, business['keywords'])

    # * Save to file
    if(dev):
        json.dump(businesses, open("output/businesses.json", "w"), indent=4)

    # * Convert to spreadsheet
    dparser = DataParser(businesses)
    dparser.cleanBusinessData()
    dparser.dumpJson()


