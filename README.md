# AutoBlueTeam
Automating the red-teaming of prompt defenses.

# ChatGPT Automation Script

This script automates the process of sending messages to the ChatGPT interface and retrieving responses using Selenium WebDriver. It is designed to import cookies to maintain session, submit text input, and fetch the generated reply from ChatGPT.

## Description

The script is part of a larger project aimed at enhancing user interactions with OpenAI's ChatGPT. It uses Python with Selenium to programmatically control a web browser, simulating the behavior of a human interacting with the ChatGPT interface.

## Getting Started

### Dependencies

- Python 3.9 or above
- Selenium WebDriver
- ChromeDriver (compatible with your Chrome version)
- `webdriver-manager` Python package

### Installing

- Clone the repository to your local machine.
- Install the required Python packages using `pip`.

```bash

pip install selenium webdriver-manager

Setting up Cookies

    Ensure you have a valid openaicookies.json file containing the necessary session cookies.

Running the Script

Navigate to the script's directory and run the script using Python.

bash

python main.py
