# -*- coding: UTF-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import math
import json
import io
import time
import os

with open('./RefreshingData.json',"r",encoding='utf-8') as f:
    thdata=json.load(f)
ids = thdata.keys()
for id in ids:
    if((int(time.time()) - thdata[id]['lastedit']) < 1209600):
        # os.rename("/home/riko/S1PlainTextBackup/"+thdata[id]['category']+'/'+str(id)+'-01待更新.md',"/home/riko/S1PlainTextBackup/"+thdata[id]['category']+'/'+str(id)+'-01'+thdata[id]['newtitle']+'.md')
        thdata[id]["active"] = True
with open('/home/riko/S1PlainTextBackup/RefreshingData.json',"w",encoding='utf-8') as f:
        f.write(json.dumps(thdata,indent=2,ensure_ascii=False))
