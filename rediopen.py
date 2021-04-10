#!/usr/bin/python3
import random
import argparse
import requests
import sys
import re
import os
import time
from requests.exceptions import ConnectionError
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor, as_completed

def logo():
   x='''
8888888b.   .d8888b.       888  d888   .d8888b.            .d8888b.
888   Y88b d88P  Y88b      888 d8888  d88P  Y88b          d88P  Y88b
888    888      .d88P      888   888  888    888               .d88P
888   d88P     8888"   .d88888   888  888    888 88888b.      8888"  88888b.
8888888P"       "Y8b. d88" 888   888  888    888 888 "88b      "Y8b. 888 "88b
888 T88b   888    888 888  888   888  888    888 888  888 888    888 888  888
888  T88b  Y88b  d88P Y88b 888   888  Y88b  d88P 888 d88P Y88b  d88P 888  888
888   T88b  "Y8888P"   "Y88888 8888888 "Y8888P"  88888P"   "Y8888P"  888  888
                                                 888
                                                 888
                                                 888

Twitter:@b4walid
Address:sec4ever

'''
   return x
def user_agent():
   users_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/88.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/78.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.3809.132 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 YaBrowser/17.4.3.195.10 Mobile/14A346 Safari/E7FBAF','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763','Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148','Mozilla/5.0 (Linux; Android 7.1.1; SM-T555 Build/NMF26X wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Safari/537.36']
   return(random.choice(users_agent))
#user_agent()

def payload():
   payloads = ['']

def detect(urls):
         try:
            response = requests.get(urls,headers=cookies, verify=True,timeout=3)
         except requests.exceptions.Timeout as e:
            print(colored('Connection Timeout!','red',attrs=['bold']))
           # break
         except requests.ConnectionError:
            print(colored('Connection Error','red',attrs=['bold']))

         if '200' in str(response):
            print (colored("["+str(response.status_code)+"] "+urls,"green",attrs=["bold"]))
         else:
            print (colored("["+str(response.status_code)+"] "+urls,"blue",attrs=["bold"]))

         if response.history:
            print(colored("Open Redirection Detected ==> "+urls,"red","on_yellow"))
         for resp in response.history:
            print(colored("["+str(resp.status_code)+"] "+response.url,"yellow",attrs=["bold"]))
            if response.url[0:22]=='https://www.google.com':
               file = open('found.txt','a')
               file.write(resp.url+', '+response.url+'\n')
               file.close()
         #time.sleep(60)
'''
def progress(i):
    count = 36
    incre = int(50.0 / count * i)
    sys.stdout.write(colored('\r' +' '*incre ,'red','on_yellow')+' '*(50-incre)+str(2*incre)+'%') if i != count-1 else sys.stdout.write(colored('\r' + ' '*20 + 'COMPLETE!' + ' '*21,'red',attrs=['blink']) + str(100)+'%')
    sys.stdout.flush()
    sys.stdout.write('\n')
'''

if __name__ == "__main__":
   print(logo())
   parser = argparse.ArgumentParser(description='Detect Open Redirection')
   parser.add_argument('-u', '--url', help='main url')
   parser.add_argument('-f', '--file', help='file of payloads')
   parser.add_argument('-t', '--thread', help='number of thread')
   parser.add_argument('-c', '--cookies', help='select your cookies')
   parser.add_argument('-w', '--wordlist', help='list of main url')
   parser.add_argument('-l', '--list', help='list of url with parameter')
   args = parser.parse_args()
   j=0
   payloads=[]
   url = args.url
   lists = args.list
   file = args.file
   wordlist = args.wordlist
   nthread = 10
   cookies = {"User-agent": user_agent()}
   #wordlist = args.wordlist
   if len(sys.argv)<4:
       parser.print_help(sys.stderr)
       sys.exit(1)
   if args.thread:
      nthread = int(args.thread)
   if url and file:
  #    scr = curses.initscr()
 #     scr.addstr(0, 0, logo())
  #    scr.addstr(15, 20, "test")
   #   scr.refresh()
      print(logo())
      print(colored('[Host]:'+url,'yellow',attrs=['blink']))
      with open(file,'r') as r:
         for l in r.readlines():
            j+=1
            payloads.append(url+l.strip())
      threadpool = ThreadPoolExecutor(max_workers=nthread)
      futures = (threadpool.submit(detect,payload) for payload in payloads)
      for i, result in enumerate(as_completed(futures)):
          if(result.result()):
             print(result)
      #detect(url,file)
   if args.cookies:
      cookies = {"Cookie":args.cookies}
   if wordlist and file:
      with open(wordlist,'r') as r:
         for m in r.readlines():
            print(colored('[Host]:'+m,'yellow',attrs=['blink'])) 
            payloads=[]
            with open(file,'r') as r:
               for l in r.readlines():
                  payloads.append(m.strip()+l.strip())
            threadpool = ThreadPoolExecutor(max_workers=nthread)
            futures = (threadpool.submit(detect,payload) for payload in payloads)
            for i, result in enumerate(as_completed(futures)):
               if(result.result()):
                  print(result)
   if lists and file:
      urls=[]
      with open(lists,'r') as r:
         for l in r.readlines():
            urls.append(l.strip())
            #parameter(l.strip())
      threadpool = ThreadPoolExecutor(max_workers=nthread)
      futures = (threadpool.submit(detect,url) for url in urls)
      for i, result in enumerate(as_completed(futures)):
         sys.stdout.write(i)
         if result.result():
            print(result.result())
