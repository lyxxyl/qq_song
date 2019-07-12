#!/usr/bin/python3
# -*- coding: utf-8 -*-
from multiprocessing import Process
import qq_song,qq_singermod,qq_songmod
import math
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor

#创建一个线程池，最大线程数为10，处理每个字母下歌手全部歌曲的下载
def main(ident):
    singermod=qq_singermod.get_singmod(ident)
    thread_num=10
    with ThreadPoolExecutor(max_workers=thread_num) as t:
        for i in singermod:
            t.submit(qq_songmod.get_songmod,i)

if __name__ == '__main__':
    #创建一个进程池，最大进程数为26
    with ProcessPoolExecutor(max_workers=26) as p:
        for i in range(1,27):
            p.submit(main,i)



