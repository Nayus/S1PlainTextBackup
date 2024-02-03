# -*- coding: UTF-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import os
import json
import io
import time

with open('./RefreshingData.json',"r",encoding='utf-8') as f:
    thdata=json.load(f)
ids = thdata.keys()
for id in ids:
    if()
with open(rootdir+'RefreshingData.json',"w",encoding='utf-8') as f:
        f.write(json.dumps(thdata,indent=2,ensure_ascii=False))
