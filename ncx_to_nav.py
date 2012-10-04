#!/opt/local/Library/Frameworks/Python.framework/Versions/3.2/python

import os, shutil, zipfile, errno, re, io, codecs, sys
from bs4 import BeautifulSoup

def main():
    ncx_path = 'files/toc.ncx'
    opf_path = 'files/content.opf'
    ncx_soup = load_file(ncx_path)
    opf_soup = load_file(opf_path)
    nav_map = get_nav_map_f(ncx_soup)
    nav_points = get_nav_points(nav_map)
    nav_upper = nav_to_upper(ncx_soup)
    

def load_file(file_loc):
    a_content_file = codecs.open(file_loc, mode='r', encoding = 'UTF-8')
    text = a_content_file.read()
    a_content_file.close()
    output = BeautifulSoup(''.join(text))
    return output

def nav_to_upper(ncx_soup):
    for item in ncx_soup:
        item = re.sub('navmap', 'navMap', str(item))
        item = re.sub('navpoint', 'navPoint', str(item))
        item = re.sub('navlabel', 'navLabel', str(item))

def get_nav_map_f(ncx):
    nav_map = ncx.find('navmap')
    return nav_map

def get_nav_points(nav_map):
    nav_points = nav_map.findAll('navpoint')
    nav_ord = []
    for each in nav_points:
        map_num = re.findall('<navpoint', str(each))
        if len(map_num) > 1:
            map_num.insert(0, len(map_num)-1)
        nav_ord.append(map_num)
    print(nav_ord)
    
    return nav_points
    
if __name__ == "__main__": main()