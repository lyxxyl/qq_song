#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import math
import qq_song

#获取每个字母的全部歌手
def get_singmod(ident):
    base_url='https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI15549021314478395&g_tk=606485906&loginUin=248819350&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22singerList%22%3A%7B%22module%22%3A%22Music.SingerListServer%22%2C%22method%22%3A%22get_singer_list%22%2C%22param%22%3A%7B%22area%22%3A-100%2C%22sex%22%3A-100%2C%22genre%22%3A-100%2C%22index%22%3A{0}%2C%22sin%22%3A{1}%2C%22cur_page%22%3A{2}%7D%7D%7D'
    #根据字母构造url
    start_url=base_url.format(ident,0,1)
    #获取每个字母下歌手的总数
    response=requests.get(start_url).text
    total=json.loads(response)['singerList']['data'].get('total')
    #获取每个字母的总页数
    page_count=math.ceil(total/80)
    all_singmod=[]
    for i in range(1,page_count+1):
        #根据页码数和字母构造多个url
        url=base_url.format(ident,80*(i-1),i)
        response_singmod=requests.get(url).text
        #获取每个字母全部歌手的标识
        data_list=json.loads(response_singmod)['singerList']['data']['singerlist']
        for data in data_list:
            all_singmod.append(data.get('singer_mid'))
    return all_singmod

if __name__ == '__main__':
    ident=1
    singmods=get_singmod(ident)
    print(singmods[0])

