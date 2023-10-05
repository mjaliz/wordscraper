import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

current_dir = os.path.realpath(os.path.dirname(__file__))

def set_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

df = pd.read_csv(os.path.join(current_dir, "..", "data","cleaned_rows.csv"))

# List of words to look up
word_list = list(df["0"])  # Add your list of words here

# Create an empty dictionary to store the results
result_dict = {}
result_dict["word"] = []
result_dict["html_result"] = []

# Set up the Selenium WebDriver (make sure to specify the path to your webdriver executable)
driver = webdriver.Chrome(options=set_chrome_options())


# Loop through the word list and perform lookups
try:
    for i, word in enumerate(word_list):
        # Construct the URL of the dictionary website (replace with the actual URL)
        # Replace with the actual URL
        print(f"Getting word number {i} : {word}")
        url = f'https://dictionary.cambridge.org/dictionary/essential-american-english/{word}'
        driver.get(url)

        # Wait for the page to load (you may need to adjust the waiting time)
        driver.implicitly_wait(10)

        # Get the HTML content of the result
        html_result = driver.page_source

        # Store the word and HTML result in the dictionary
        result_dict["word"].append(word)
        result_dict["html_result"].append(html_result)
finally:
    # Close the WebDriver
    driver.close()
    result_df = pd.DataFrame(result_dict)
    result_df.to_csv(os.path.join(current_dir, "..", "data", "result.csv"))




