import json
import os
def read_json():
    path=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(path,'../data/post.json')
    with open(file_path,"r",encoding="utf-8") as f:
        data = json.load(f)
        return data

def read_update_data():
    path=os.path.dirname(os.path.abspath(__file__))
    file_path=os.path.join(path,'../data/post.json')
    with open(file_path,"r",encoding="utf-8") as f:
        data = json.load(f)
        return data