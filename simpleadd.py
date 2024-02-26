# -*- coding: UTF-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
import math
import json
import io
import time
import os,shutil
import re

rootdir="/home/riko/S1PlainTextBackup/"

def thread_dict(thdir,thdict):
    with open(thdir,'r',encoding='UTF-8-sig') as f:
        lines = f.readlines()
        a = ''
        for line in lines:
            a += line
        b = a.split("*****")
    for i in b[1::]:
        if(re.findall(r'#####\s(\d+)#',i)[0]):
            thdict[re.findall(r'\n#####\s(\d+)#',i)[0]] = i

def thread_merge(oridir,desdir):
    ori = {}
    des = {}
    thread_dict(oridir,ori)
    if os.path.exists(desdir):
        thread_dict(desdir,des)
    result = ''
    for i in sorted(list(set(ori.keys())-set(des.keys()))):
        result = result +  ("*****") + ori[i]
    with open (desdir,'a',encoding='UTF-8-sig')as f:
        f.write(result)
    os.remove(oridir)

for dir_prefix in ["外野/","手游专楼/","游戏区/","漫区/","虚拟主播区专楼/"]:
    subdir = rootdir + dir_prefix
    for item in os.listdir(subdir):
        if not str(item).endswith(".md"):
            name_list = str(item).split("[")
            #找到有未挪入文件夹的01存档文件
            old_path = subdir+name_list[0]+"-01["+name_list[1]+".md"
            if(os.path.exists(old_path)):
                print(old_path)
                new_path = subdir+item+"/"+name_list[0]+"-01["+name_list[1]+".md"
                #如果里面已经有个01了，merge
                if(os.path.exists(new_path)):
                    thread_merge(old_path,new_path)
                else:
                    os.rename(old_path,new_path)

            # print(os.path.exists(subdir+name_list[0]+"-01["+name_list[1]+".md"))
            # print(os.path.isfile(os.path.abspath(item)))

# def parse_title(title):
#     titles = re.sub(r'<.+?>','',str(title))
#     titles = re.sub(r'[\]\[]','',titles)
#     titles = re.sub(r'\|','｜',titles)
#     titles = re.sub(r'/','／',titles)
#     titles = re.sub(r'\\','＼',titles)
#     titles = re.sub(r':','：',titles)
#     titles = re.sub(r'\*','＊',titles)
#     titles = re.sub(r'\?','？',titles)
#     titles = re.sub(r'"','＂',titles)
#     titles = re.sub(r'<','＜',titles)
#     titles = re.sub(r'>','＞',titles)
#     titles = re.sub(r'\.\.\.','…',titles)
#     titles = re.sub(r'\n',' ',titles)
#     titles = '['+titles+']'
#     return titles

# with open('./RefreshingData.json',"r",encoding='utf-8') as f:
#     thdata=json.load(f)
# ids = thdata.keys()
# for id in ids:
#     if((int(time.time()) - thdata[id]['lastedit']) < 1209600):
#         thdata[id]['active'] = True
#     # if("]" not in thdata[id]["title"]):
#     #     new_title = parse_title(thdata[id]["title"])
#     #     if(thdata[id]["totalreply"] != 0):
#     #         os.rename("/home/riko/S1PlainTextBackup/"+thdata[id]['category']+'/'+str(id)+'-01'+thdata[id]['title']+'.md',"/home/riko/S1PlainTextBackup/"+thdata[id]['category']+'/'+str(id)+'-01'+new_title+'.md')
#     #     thdata[id]["title"] = new_title
# with open('/home/riko/S1PlainTextBackup/RefreshingData.json',"w",encoding='utf-8') as f:
#         f.write(json.dumps(thdata,indent=2,ensure_ascii=False))