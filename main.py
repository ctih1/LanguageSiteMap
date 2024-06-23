from checker import run_checker
from mapchart import Map
from multiprocessing import Pool
from tqdm import tqdm
import json
from utils import *
import logger
import os
import time

if(__name__=="__main__"):

    #domain: str = str(input("Enter your domain. For example: https://www.example.com/%COUNTRY%. "))
    domain = "https://www.google.%COUNTRY%/"
    copy=True
    #copy: bool = bool(input("Do you want to copy the result into your clipboard? True/False "))
    start_time = time.time()

    def parse_working_countries(urls: dict) -> list:
        valids: list = []
        for domain in urls:
            domain: dict = domain
            if list(domain.values())[0] == 1:
                valids.append(format(url_and_country[list(domain.keys())[0]]))
        return valids

    def parse_redirect_countries(urls: dict) -> list:
        redirects: list = []
        for domain in urls:
            domain: dict = domain
            if list(domain.values())[0] == 0:
                redirects.append(format(url_and_country[list(domain.keys())[0]]))
        return redirects

    map = Map()


    url_and_country: dict = generate_urls(domain) # {"domain":country}
    checked:list = run_checker(url_and_country)
    succes_countries:list = parse_working_countries(checked)
    redirect_countries: list = parse_redirect_countries(checked)

    map_text = str(map.create([
        {"color":"#33ff33","countries":succes_countries, "title":"Success"},
        {"color":"#ffff33","countries":redirect_countries, "title":"Redirects"},
        {"color":"#ff3333","countries":list(set(list(url_and_country.values())) - set(succes_countries) - set(redirect_countries)), "title":"Nope"}
    ]))

    with open("result.txt","w") as f:
        f.write(map_text)

    if(copy): os.system(f"echo {map_text} | clip")
    print("Saved map as result.txt")
    print(f"Done in {time.time()-start_time} seconds")

