import requests
from bs4 import BeautifulSoup
import os
import pickle

def create_lektor_publication(record_dict):
    foldername = record_dict['title'].replace(" ","-")
    try: os.mkdir(f'./content/publications/{foldername}')
    except: pass
    with open(f'./content/publications/{foldername}/contents.lr',"w") as outf:
        for idx, (key, val) in enumerate(record_dict.items()):
            outf.write(f"{key}:{val}")
            if(idx < len(record_dict.items())):
                outf.write(f"\n")
                outf.write(f"---")
                outf.write(f"\n")

def get_publications_from_zenodo():
    records = []
    with open("zenodo_pubs.html") as inpf:
        html_doc = inpf.read()
        
    soup = BeautifulSoup(html_doc, 'html.parser')
    records_html = soup.find_all("div",{"class":"record-elem"})

    for record_html in records_html:
        title = record_html.find("h4").find("a").text
        description = record_html.find("p",{"class":"hidden-xs"}).text
        full_url = record_html.find("a",{"class":"btn btn-default"}).get("href")
        id = full_url.split("/")[-1]
        d = eval(requests.get(f"https://zenodo.org/api/records/{id}")
                        .content.decode("utf-8").replace("true","True").replace("false","False"))
        print(title)
        record = {
                "pub_date": d['created'].split("T")[0],
                "title": d['metadata']['title'],
                "summary": description,#d['metadata']['description'],
                "author": ", ".join([author_d['name'] for author_d in d['metadata']['creators']]),
                "zenodo": full_url
        }
        records.append(record)
    return records

if not os.path.exists("zenodo_publications.pickle"):
    records = get_publications_from_zenodo()
    with open("zenodo_publications.pickle","wb") as outf:
        pickle.dump(records, outf, protocol=pickle.HIGHEST_PROTOCOL)
else:
    with open("zenodo_publications.pickle","rb") as inpf:
        records = pickle.load(inpf)

for record in records:
    create_lektor_publication(record)
