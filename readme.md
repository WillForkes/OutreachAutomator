***This project helps automate outreach to businesses via use of Google Maps and OpenAI***

This project is unfinished and not maintained actively.

# Outreach Automation Bot
## Overview
The Outreach Automation Bot is designed to streamline and automate the process of generating and sending prospecting emails for outreach purposes. This tool can be utilized by businesses and individuals to efficiently manage their outreach campaigns, saving time and ensuring consistent communication.

**Features**
- Developer Mode: Enables additional logging and debugging features.
- Prospecting Emails: Utilizes ChatGPT to write personalized prospecting emails.
- Email Automation: Automatically sends the generated prospecting emails.

**Getting Started**
Prerequisites
Ensure you have the following installed on your system:
```
Python 3.x
Required Python packages (can be installed via requirements.txt)
```

**Installation**
Clone the repository:
```
git clone https://github.com/WillForkes/OutreachAutomator.git
cd OutreachAutomator
```

**Install the required packages:**
`pip install -r requirements.txt`

**Usage**
Run the bot using the command-line interface. The script accepts several optional arguments to customize its behavior.

```
python3 bot.py [-d] [-p] [-e]
Arguments
-d, --dev: Enables developer mode. This uses pre-existing data instead of using Google's API to save credits
-p, --prospect: Enables ChatGPT to write prospecting emails.
-e, --email: Enables automatic sending of generated prospecting emails.
```


**Interactive Input**
Upon running the script, you will be prompted to provide the following details:

Business Type: The type of business you are targeting.
Location: The location for your outreach campaign.
Radius: The radius (in meters) within which to search for prospects.

**Contributing**
Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

**Contact**
For any inquiries or support, please reach out to:

Will forkes
Email: wforkes@gmail.com
