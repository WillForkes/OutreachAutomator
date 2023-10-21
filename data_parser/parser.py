import pandas as pd
import json

class DataParser:
    def __init__(self, businesses):
        self.businesses = businesses
    
    def cleanBusinessData(self):
        tooutput = []
        for business in self.businesses:
            # strip uncessary data such as the geolocation coordinates or opening hours. Only keep the data we need such as place_id, name, address, etc.
            
            # # format arrays into strings with commas
            # business["types"] = ",".join(business["types"])
            # if "social_media_urls" in business:
            #     business["social_media_urls"] = ", ".join(business["social_media_urls"])
            #     business["social_media_urls"] = business["social_media_urls"].replace("https://", "")

            stripped_business = {
                "place_id": business["place_id"],
                "name": business["name"],
                "address": business["formatted_address"],
                "business_status": business["business_status"],
                "types": business["types"],
                "rating": business["rating"],
                "user_ratings_total": business["user_ratings_total"],
                "website": (business["website"] if "website" in business and business["website"] is not None else ""),
                "phone": (business["phone"] if "phone" in business and business["phone"] is not None else ""),
                "email": (business["email"] if "email" in business and business["email"] is not None else ""),
                "social_media_urls": (business["social_media_urls"] if "social_media_urls" in business and business["social_media_urls"] != "" else ""),
            }
            tooutput.append(stripped_business)
        
        self.businesses = tooutput

    def convertToSpreadsheet(self):
        # convert to dataframe
        df = pd.DataFrame(self.businesses)

        file_name = "output/data.xlsx"
        sheet_name = "Business Data"

        with pd.ExcelWriter(file_name, engine="xlsxwriter") as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    def dumpJson(self):
        json.dump(self.businesses, open("output/businesses_parsed.json", "w"), indent=4)
