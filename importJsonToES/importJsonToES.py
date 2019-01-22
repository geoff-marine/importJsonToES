
import json, os
from pathlib import Path
import requests
import io

path_to_folder = Path("C:\elasticsearch")
file_to_open = path_to_folder / "EUFleetRegistry.json"


with io.open(file_to_open, encoding="utf-8-sig") as json_file:  
     jsonData = json.load(json_file, strict = False)

for p in jsonData:
    r = requests.post('http://localhost:9200/vessel/_doc?pretty', json = p)   
