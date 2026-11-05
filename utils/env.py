# Chemin: C:/Users/DIGITAL MARKET/Desktop/Pyhton/projet maxi pandas/utils/env.py
from dotenv import load_dotenv

import os

load_dotenv()

URL=os.getenv("DATA_LOCATION")

