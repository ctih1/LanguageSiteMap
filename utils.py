import json
import os

done: dict = {
    "createurl":"0",
    "gotdomains":"0",
    "processing":"0",
    "mademap":"0"
    }

def format(a: str) -> str:
    return a.replace(" ","_").replace("'",'')
def format_config(a:str) -> str:
    return a.replace("True","true").replace("False","false").replace("'",'"')
def generate_urls(url: str) -> dict:
    """_summary_

    Args:
        url (str): 
            The url
            Example:
                https://example.com/%COUNTRY%/abcd

    Returns:
        list: the URL's
    """
    urls: dict = {}
    with open("resources/data.json","r") as f:
        codeinfo: dict = json.load(f)
    for i in range(0,codeinfo.__len__()):
        urls[url.replace("%COUNTRY%",(codeinfo[i].get("Code",None)).lower())]=format(codeinfo[i].get("Country name"))
    return urls

def clear() -> None:
    os.system("cls")

def progress():
    clear()
    print(f"[{done['createurl']}] Create URL list")
    print(f"[{done['gotdomains']}] Gathered domains")
    print(f"[{done['processing']}] Processed data")
    print(f"[{done['mademap']}] Finished map")