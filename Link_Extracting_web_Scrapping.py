import os
import bs4
import requests
from sys import *

def LinksDisplay(url):
    res = requests.get(url)
    print(type(res))
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    print(type(soup))
    
    links = soup.find_all('a',href = True)
    
    return links

def main():
    print("Application Name :" +argv[0])
    
    if(len(argv) == 2):
        if(argv[1] == "-h") or (argv[1] == "-H"):
            print("This script is used to featch links from wikipidia file")
            exit()
            
        if(argv[1] == "-u") or (argv[1] == "-U"):
            print("Usage : Application Name")
            exit()
            
    url = input("Enter Url : ")
    
    arr = LinksDisplay(url)
    
    print("Links are")
    
    for element in arr:
        if "#" not in element['href']:
            print(element['href'])

if __name__ =="__main__":
    main()
    