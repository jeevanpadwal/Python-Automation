from bs4 import *
import requests 
import os

def folder_create(images):
    try:
        
        folder_name = input("Enter folder name :- ")
        os.mkdir(folder_name)
        
    except:
        print("folder exist with that name")
        folder_create()
        
    download_images(images, folder_name)
    
def download_images(images, folder_name):
    count = 0
    
    print(f"Total {len(images)} Image Found!")
    
    if len(images) != 0:
        for i, image in enumerate(images):
            
            try:
                image_link = image["data-srcset"]
                
            except:
                try:
                    image_link = image["data-src"]
                    
                except:
                    try:
                        
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
                            
                        except:
                            pass
            try:
                r = requests.get(image_link).content
                
                try:
                    r = str(r,'utf-8')
                    
                except UnicodeDecodeError:
                    with open(f"{folder_name}/images{i+1}.jpg","wb+")as f:
                        f.writer(r)
                        
                    count +=1
            
            except:
                pass
                    
                    
        if count == len(images):
            print("All images Downloaded!")
        
        else:
            print(f"Total{count} Images Downloaded Out of {len(images)}")
            
def main():
    
    print("Application Name : Auto Image Downloder")
    
    url = input("Enter URl From where you want to download images :- ")
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    
    images = soup.findAll('img')
    
    folder_create(images)
    
if __name__ == "__main__":
        main()
                
                
                    
    