import os

def setup():
    try:
        import urllib.request
    except ImportError:
        print("You do not have urllib! Installing it now!")
        os.system("python -m pip install urllib5")
    
    try:
        import requests
    except ImportError:
        print("You do not have requests! Installing it now!")
        os.system("python -m pip install requests")

