# -*- coding: UTF-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import math
import json
import io
import time
import os
import re
def parse_title(title):
    titles = re.sub(r'<.+?>','',str(title))
    titles = re.sub(r'[\]\[]','',titles)
    titles = re.sub(r'\|','｜',titles)
    titles = re.sub(r'/','／',titles)
    titles = re.sub(r'\\','＼',titles)
    titles = re.sub(r':','：',titles)
    titles = re.sub(r'\*','＊',titles)
    titles = re.sub(r'\?','？',titles)
    titles = re.sub(r'"','＂',titles)
    titles = re.sub(r'<','＜',titles)
    titles = re.sub(r'>','＞',titles)
    titles = re.sub(r'\.\.\.','…',titles)
    titles = re.sub(r'\n',' ',titles)
    titles = '['+titles+']'
    return titles

with open('./RefreshingData.json',"r",encoding='utf-8') as f:
    thdata=json.load(f)
ids = thdata.keys()
for id in ids:
    if((int(time.time()) - thdata[id]['lastedit']) < 1209600):
        thdata[id]['active'] = True
    # if("]" not in thdata[id]["title"]):
    #     new_title = parse_title(thdata[id]["title"])
    #     if(thdata[id]["totalreply"] != 0):
    #         os.rename("/home/riko/S1PlainTextBackup/"+thdata[id]['category']+'/'+str(id)+'-01'+thdata[id]['title']+'.md',"/home/riko/S1PlainTextBackup/"+thdata[id]['category']+'/'+str(id)+'-01'+new_title+'.md')
    #     thdata[id]["title"] = new_title
with open('/home/riko/S1PlainTextBackup/RefreshingData.json',"w",encoding='utf-8') as f:
        f.write(json.dumps(thdata,indent=2,ensure_ascii=False))
