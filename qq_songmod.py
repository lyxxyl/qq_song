#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import re
import json
import math
import qq_song

#获取每个歌手的全部歌曲的标识，并下载
def get_songmod(singermod):
    #获取url
    base_url='https://u.y.qq.com/cgi-bin/musicu.fcg?-=getUCGI6536838773372087&g_tk=930886421&loginUin=248819350&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0&data=%7B%22comm%22%3A%7B%22ct%22%3A24%2C%22cv%22%3A0%7D%2C%22singer%22%3A%7B%22method%22%3A%22get_singer_detail_info%22%2C%22param%22%3A%7B%22sort%22%3A5%2C%22singermid%22%3A%22{0}%22%2C%22sin%22%3A{1}%2C%22num%22%3A{2}%7D%2C%22module%22%3A%22music.web_singer_info_svr%22%7D%7D'
    #构造url,获取每个歌手歌曲的总数
    total_url=base_url.format(singermod,0,10)
    total_response=requests.get(total_url).text
    total=json.loads(total_response)['singer']['data'].get('total_song')
    #songmods_list=[]
    #获取歌曲总共页数
    pager_num=math.ceil(total/10)
    for i in range(pager_num):
        #根据页码数和歌手标识构造多个url
        songs_url=base_url.format(singermod,i*10,10)
        songs_response=requests.get(songs_url).text
        #获取歌曲的标识
        songs_data=json.loads(songs_response)['singer']['data']['songlist']
        for song in songs_data:
            qq_song.load_music(song.get('mid'))
            #songmods_list.append(song.get('mid'))

    #return songmods_list
#
# if __name__ == '__main__':
#     singermod='001cnFzG2sq87c'
#     songmods=get_songmod(singermod)
#     print(songmods)