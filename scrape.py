from io import FileIO
import requests, time
import pandas as pd
from discord_webhook import DiscordWebhook
import os
#import pypdf 
import tabula

url = 'https://www.syf.gov.sg/syf/slot/u737/AP/Results/2023/BCJ.pdf'
print(os.environ)
school = os.environ['SCHOOL']
whk_url = os.environ['WEBHOOK']
ping = os.environ['PING']  
interval = int(os.environ['INTERVAL'])
def scrape(t : int):
    res = requests.get(url)
    if res.reason == 'Not Found':
        print("Not released")
    else:
        with open('thing.pdf', 'wb+') as f:
            f.write(res.content)
        score = get_score('./thing.pdf')
        wh = DiscordWebhook(url=whk_url, content=score + " " + ping)
        wh.execute()
        
        return()
    time.sleep(t)
    scrape(t)

def get_score(pdf):
    dfs = tabula.read_pdf(
        pdf,
        pages='all',
        encoding="utf-8",
    )    
#    print(df.head())
#    df = pd.concat(dfs)
#    print(dfs[0].head())
    df = dfs[0]
    fdf = df["NAME OF SCHOOL"].str.contains(school)
    ffdf = df[fdf]["CERTIFICATE OF"].iloc[0] #.astype(str)
    print(ffdf)
    return(ffdf)
    
scrape(interval)
