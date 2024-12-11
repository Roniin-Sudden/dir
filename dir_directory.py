from sys import *
from datetime import date
import os
import time
import requests
import threading



def search(url, wordlists):

    try:
        local_archive = open(archive_name, 'a', encoding='utf-8')
        with open(wordlists,'r') as file:
            path_links = []
            for line in file:
                word = line.replace('\n','')
                response = requests.get(url+word)            
                if response.status_code == 200:
                    print(f"found: {url+word}")
                    path_links.append(f"found: {url+word}\n")
            for line in sorted(set(path_links)):
                local_archive.write(line)
        print(f'{os.system('cls || clear')}\nExecute successful.\nSites saved in {date.today()}.txt in {os.getcwd()}')
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('\nQuiting...'
              'Successful break program\n')
...


if __name__ == "__main__":
    os.system('cls || clear')
    print('STARTING WEB SCANNER....\n')   
    archive_name = f"{date.today()}.txt" 
    if archive_name not in os.listdir(os.getcwd()):
        with open(archive_name, 'w', encoding='utf-8') as file:
            file.write(f"at {date.today()}!!\n\n\n")
            print("ARCHIVE CREATED, WEB SCANNER IS UP!!!\n")
            time.sleep(3)


    match len(argv):
        
        case 3:
                  
            threading.Thread(target=search(argv[1], argv[2])).start()
        
        case 4: 
                  
            threading.Thread(target=search(argv[1], argv[2])).start()
            threading.Thread(target=search(argv[1], argv[3])).start()

        case 5: 
                  
            threading.Thread(target=search(argv[1], argv[2])).start()
            threading.Thread(target=search(argv[1], argv[3])).start()
            threading.Thread(target=search(argv[1], argv[4])).start()

        case 6: 
                  
            threading.Thread(target=search(argv[1], argv[2])).start()
            threading.Thread(target=search(argv[1], argv[3])).start()
            threading.Thread(target=search(argv[1], argv[4])).start()
            threading.Thread(target=search(argv[1], argv[5])).start()
               
        case 7: 
                  
            threading.Thread(target=search(argv[1], argv[2])).start()
            threading.Thread(target=search(argv[1], argv[3])).start()
            threading.Thread(target=search(argv[1], argv[4])).start()
            threading.Thread(target=search(argv[1], argv[5])).start()
        
        case _:
            print('Usage: python3 dir_directory.py <https://url/> <wordlist.txt>'
                  'This script can scan with five wordlist at the same time')
            