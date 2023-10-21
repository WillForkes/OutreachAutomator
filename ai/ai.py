import openai

class OpenAI():
    def __init__(self, api_key):
        self.api_key = api_key

    def getCompletion(self, purpose, businessName, businessType, businessLocation, businessKeywords):
        openai.api_key = self.api_key

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant designed for helping writing cold emails for prospecting new clients to offer {purpose}. You should list the benefits of this service and ask for a quick over the phone meeting. Your message should be specific and targeted. Keep the message relatively short. Your tone should also should be friendly, relaxed and semi-professional, in other words don't try too hard."},
                {"role": "user", "content": "I want you to write me an email to a potential client."},
                {"role": "assistant", "content": "Sure! Please provide some information about the business."},
                {"role": "user", "content": f"Business Name: {businessName}, Business keywords: {businessKeywords}, Business type: {businessType}, Location: {businessLocation}."},
            ]
        )

        return response.choices[0].text