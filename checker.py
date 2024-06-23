import grequests
import requests
import time
from tqdm import tqdm
from multiprocessing import Pool

def __check__(domain:str) -> tuple[str,int,float]:
    st=time.time()
    try:
        req:requests.Response = requests.get(domain)
    except Exception:
        return domain,500,time.time()-st
    return req.url,req.status_code,time.time()-st

def run_checker(domains:list) -> list:
    results:list
    with Pool() as pool:
        results = tqdm(
            pool.imap_unordered(__check__, domains,chunksize=10),
            total=domains.__len__(),
            mininterval=1
        )
        for domain, result, et in results:
            tqdm.write(f"[{domain}] > GET > {result} | {round(et,3)}s")
    return results