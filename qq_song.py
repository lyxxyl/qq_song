#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import urllib
#构造一个请求头
headers={'User-Agent':'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'}
#根据歌曲的不同标识，下载歌曲
def load_music(song_sign):
    sign='C400'+song_sign
    #获取vkey的值
    response=requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&jsonpCallback=MusicJsonCallback&cid=205361747&songmid={0}&filename={1}.m4a&guid=6612300644'.format(song_sign,sign)).text
    response=json.loads(response)
    vkey=response['data']['items'][0].get('vkey')
    if vkey:
        #构造歌曲的下载url
        base_url='http://dl.stream.qqmusic.qq.com/{0}.m4a?vkey={1}&guid=6612300644&uin=0&fromtag=66'.format(sign,vkey)
        #base_url='http://dl.stream.qqmusic.qq.com/{0}.m4a?guid={1}&vkey={2}&uin={3}&fromtag={4}'
        #song_url=base_url.format(sign,guid,vkey,uin,fromtag)
        try:
            urllib.request.urlretrieve(base_url,'D:/music/{0}.m4a'.format(song_sign))
        except Exception as e:
            print(song_sign,e)
        finally:
            print('{0} load success!'.format(song_sign))

if __name__ == '__main__':
    #歌曲的唯一标识
    song_sign='004ZyTpj2oL3IU'
    load_music(song_sign)
