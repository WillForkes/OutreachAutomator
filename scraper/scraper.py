import requests
import re
import cloudscraper


class WebsiteScraper:
    def __init__(self):
        self.website_url = None
        self.website_content = None
        self.email_address = None
        self.contact_page_url = None
        self.social_media_urls = []
        self.email_protected = False

    def load(self, website_url):
        self.website_url = website_url

        # retry count
        retry = 0

        while retry < 3:
            try:
                scraper = cloudscraper.create_scraper()
                response = scraper.get(website_url)
                response_decoded = response.content.decode('utf-8')

                if(response_decoded == ''):
                    retry += 1
                    continue

                self.website_content = response_decoded
                return True
            except:
                retry += 1
        
        return False
        
        # open('output/website.html', 'w').write(self.website_content)

    def find_email_address(self):
        if("[email&#160;protected]" in self.website_content):
            self.email_protected = True
            return

        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_addresses = re.findall(email_regex, self.website_content)

        if len(email_addresses) > 0:
            self.email_address = email_addresses[0]

    def find_social_medias(self):
        social_media_regex = r'facebook|twitter|instagram|linkedin'
        links_regex = r'href=[\'"]?([^\'" >]+)'
        links = re.findall(links_regex, self.website_content)
        for link in links:
            if re.search(social_media_regex, link, re.IGNORECASE):
                self.social_media_urls.append(link)
        
        # remove duplicates
        self.social_media_urls = [x for x in self.social_media_urls if self.social_media_urls.count(x) == 1]

    def find_contact_page(self):
        contact_page_regex = r'contact|support'
        links_regex = r'href=[\'"]?([^\'" >]+)'
        links = re.findall(links_regex, self.website_content)

        for link in links:
            if re.search(contact_page_regex, link, re.IGNORECASE):
                if link.startswith('/'):
                    link = self.website_url + link
                self.contact_page_url = link
                break
