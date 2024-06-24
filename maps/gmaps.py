import requests
import googlemaps
import json
from urllib.parse import urlparse, urlunparse

class GoogleMapsAPI:
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
        self.client = googlemaps.Client(key=self.api_key)

    def search_businesses(self, business_type, query, radius):
        params = {
            'key': self.api_key,
            'query': query,
            'radius': radius,
            'type': business_type
        }

        results = []

        # Used to get all results as there is a limit of 20 results per request
        while True:
            response = requests.get(self.base_url, params=params)
            data = response.json()

            if 'results' in data:
                results.extend(data['results'])

            if 'next_page_token' in data:
                params['pagetoken'] = data['next_page_token']
            else:
                break

        new_results = []
        for business in results:
            businessDetails = self.get_business_details(business['place_id'])
            business['website'] = businessDetails['website']
            business['phone'] = businessDetails['phone']
            new_results.append(business)

        return new_results

    def get_business_details(self, place_id):
        params = {
            'key': self.api_key,
            'place_id': place_id,
            'fields': 'website,formatted_phone_number'
        }
        response = requests.get('https://maps.googleapis.com/maps/api/place/details/json', params=params)
        result = response.json()['result']
        
        if(result.get('website') != None):
            parsed_url = urlparse(result['website'])
            new_url = urlunparse((parsed_url.scheme, parsed_url.netloc, '', '', '', ''))
            result['website'] = new_url

        return {"website": result['website'], "phone": result['formatted_phone_number']}

    