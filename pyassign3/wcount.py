#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Liumingjin"
__pkuid__  = "1700011758"
__email__  = "jzj170325@pku.edu.cn"
"""

import sys
import urllib
from urllib.request import urlopen
import re
print(sys.argv)
f=urllib.request.urlopen('http://www.gutenberg.org/cache/epub/19033/pg19033.txt')
g=f.read()
lines=str(g.lower())
def wcount(lines, topn):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    patt = re.compile(r"[^A-Za-z0-9]")
    spacePatt = re.compile(r"\s+")
    lines = re.sub(patt," ",lines)
    lines = re.sub(spacePatt," ",lines)
    print(lines) 
    words = lines.split()
    wordDic = {}
    for wd in words:
        if wd not in wordDic:
            wordDic[wd] = 1
        else:    
            wordDic[wd] += 1
    lst = zip(wordDic.values(),wordDic.keys())
    lst = sorted(lst,reverse=True)
    for (freq, wd) in lst[:topn]:
        print(wd, freq)
wcount(lines,10)
if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
       



