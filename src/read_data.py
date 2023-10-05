import os
import pandas as pd
from bs4 import BeautifulSoup as bs

current_dir = os.path.realpath(os.path.dirname(__file__))

df = pd.read_csv(os.path.join(current_dir, "..", "data", "result.csv"))
abandon = df.iloc[4]["html_result"]
soup = bs(abandon, features="html.parser")
with open("test.html", "w") as f:
    f.write(soup.prettify())