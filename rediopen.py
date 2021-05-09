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
'''
   y='''                     Detect Open Redirection
                 Coded By Boureba Walid @b4walid

'''
   print(colored(x,'red',attrs=['blink']))
   print(colored(y,'yellow',attrs=['bold']))


def user_agent():
   users_agent = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/88.0','Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:24.0) Gecko/20100101 Firefox/78.0','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.3809.132 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 10_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 YaBrowser/17.4.3.195.10 Mobile/14A346 Safari/E7FBAF','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763','Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148','Mozilla/5.0 (Linux; Android 7.1.1; SM-T555 Build/NMF26X wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Safari/537.36']
   return(random.choice(users_agent))


def detect(urls):
         try:
            response = requests.get(urls,headers=cookies, verify=True,timeout=3)
         except requests.exceptions.Timeout as e:
            print(colored('Connection Timeout!','red',attrs=['bold']))
            return None
         except requests.ConnectionError:
            print(colored('Connection Error','red',attrs=['bold']))
            return None
         except:
            print(colored('Connection Error !!!!!!!!!!','magenta',attrs=['bold']))
            return None
         if '200' in str(response):
            print (colored("["+str(response.status_code)+"] "+urls,"green",attrs=["bold"]))
         else:
            print (colored("["+str(response.status_code)+"] "+urls,"blue",attrs=["bold"]))

         if response.history:
            for resp in response.history:
               if response.url[0:22]=='https://www.google.com':
                  print(colored("Open Redirection Detected ==> "+urls,"red","on_yellow"))
                  print(colored("["+str(resp.status_code)+"] "+response.url,"yellow",attrs=["bold"]))
                  file = open('vuln/'+urls.split('/')[2]+'.txt','a')
                  file.write(resp.url+' ==> '+response.url+'\n')
                  file.close()
                  count.append('b4')
                  #return True


def parameter(url,file):
   if '?' in url or '&' in url or '=' in url:
      if '?' in url:
         link1 = url.split('?')
         parameter = link1[1]
      else:
         parameter = url
      link2 = parameter.split('&')
      for param in link2:
         if '=' in param:
            if quick:
               payloads = quick_payloads()
               for p in payloads:
                  pld = payload(param,p)
                  if pld:
                     urlp = url.replace(param,pld)
                     if detect(urlp):
                        return None
            elif file:
               with open(file,'r') as r:
                  for l in r.readlines():
                     payloads = l.strip()
                     pld = payload(param,payloads)
                     if pld:
                        urlp = url.replace(param,pld)
                        if detect(urlp):
                           return None


def payload(parameter, payloads):
   parameterx = list_parameters()
   p = parameter.replace('','b4xcvksdfj')
   p = parameter.split('=')
   if without:
      p[1] = 'b4xcvksdfj'
      parameter = '='.join(p)
      p = parameter.split('=')
      payload = parameter.replace(p[1],payloads)
      return payload
   if p[0] in parameterx:
      p[1] = 'b4xcvksdfj'
      parameter = '='.join(p)
      p = parameter.split('=')
      payload = parameter.replace(p[1],payloads)
      return payload

def list_parameters():
   parameterx = ['next','url','target','rurl','dest','destination','redir','redirect_to','redirect_uri','redirect_url','redirect','view','image_url','go','returnTo','return_to','checkout_url','continue','return_path','to']
   return parameterx

def quick_payloads():
   payloads=['//google.com','\/\/www.google.com','///google.com','@google.com']
   return payloads

def one_parameter(url,payloads):
   if '?' in url or '&' in url or '=' in url:
      if '?' in url:
         link1 = url.split('?') #www.google.com,id=1&page=1
         parameter = link1[1]
      else:
         parameter = url
      link2 = parameter.split('&') #id=1,page=1
      for param in link2:
         if '=' in param:
                  pld = payload(param,payloads)
                  if pld:
                     urlp = url.replace(param,pld)
                     if detect(urlp):
                        return None


if __name__ == "__main__":
   global without, count, quick
   count = []
   os.system('clear')
   logo()
   if not os.path.isdir('vuln'):
      os.system('mkdir vuln')
   parser = argparse.ArgumentParser(description='Detect Open Redirection')
   parser.add_argument('-u', '--url', help='main url')
   parser.add_argument('-f', '--file', help='file of payloads')
   parser.add_argument('-t', '--thread', help='number of thread')
   parser.add_argument('-c', '--cookies', help='select your cookies')
   parser.add_argument('-w', '--wordlist', help='list of main url')
   parser.add_argument('-l', '--list', help='list of url with parameter')
   parser.add_argument('--quick', nargs='?',const=8, help='fast scan of url but with few payload')
   parser.add_argument('--without', nargs='?',const=8, help='scan all parameters')
   args = parser.parse_args()
   payloads=[]
   url = args.url
   lists = args.list
   file = args.file
   wordlist = args.wordlist
   quick = args.quick
   nthread = 15
   cookies = {"User-agent": user_agent()}
   without = args.without
   if len(sys.argv)<4:
       parser.print_help(sys.stderr)
       sys.exit(1)

   if args.thread:
      nthread = int(args.thread)

   if url:
      if 'http://' not in url and 'https://' not in url:
         url = 'http://'+url
      if url[-1] != '/':
         url = url+'/'
      print(colored('[Host]:'+url,'yellow',attrs=['blink']))
      if quick:
         payloads = quick_payloads()
      elif file:
         if os.path.exists(file):
            with open(file,'r') as r:
               for l in r.readlines():
                  payloads.append(l.strip())
         else:
            print(colored('File not exist check it!!','red',attrs=['bold']))
      else:
         parser.print_help(sys.stderr)
         exit()
      threadpool = ThreadPoolExecutor(max_workers=nthread)
      if '?' in url or '=' in url:
         futures = (threadpool.submit(one_parameter,url,payload) for payload in payloads)
         for i, result in enumerate(as_completed(futures)):
            if result.result():
               print(result.result())
      else:
         futures = (threadpool.submit(detect,url+payload) for payload in payloads)
         for i, result in enumerate(as_completed(futures)):
            if(result.result()):
               print(result)

   if args.cookies:
      cookies = {"Cookie":args.cookies}

   if wordlist:
      if os.path.exists(wordlist):
         with open(wordlist,'r') as r:
            for url in r.readlines(): 
               if 'http://' not in url.strip() and 'https://' not in url.strip():
                  url = 'http://'+url.strip()
               if url[-1] != '/':
                  url = url.strip()+'/'
               print(colored('[Host]:'+url,'yellow',attrs=['blink'])) 
               payloads=[]
               if quick:
                  p=[]
                  payloads = quick_payloads()
                  for payload in payloads:
                     p.append(url+payload)
                  payloads = p
               elif file:
                  if os.path.exists(file): 
                     with open(file,'r') as r:
                        for l in r.readlines():
                           payloads.append(url+l.strip())
                  else:
                     print(colored('File not exist check it!!','red',attrs=['bold']))
               else:
                  parser.print_help(sys.stderr)
                  exit()
               threadpool = ThreadPoolExecutor(max_workers=nthread)
               futures = (threadpool.submit(detect,payload) for payload in payloads)
               for i, result in enumerate(as_completed(futures)):
                  if(result.result()):
                     print(result)

      else:
         print(colored('File not exist check it!!','red',attrs=['bold']))

      threadpool = ThreadPoolExecutor(max_workers=nthread)
      futures = (threadpool.submit(detect,payload) for payload in payloads)
      for i, result in enumerate(as_completed(futures)):
         if(result.result()):
            print(result)


   if lists:
      if os.path.exists(lists):
         urls=[]
         with open(lists,'r') as r:
            for l in r.readlines():
               urls.append(l.strip())
         threadpool = ThreadPoolExecutor(max_workers=nthread)
         if file or quick:
            if file:
               if not os.path.exists(file):
                  print(colored('File not exist check it!!','red',attrs=['bold']))
                  parser.print_help(sys.stderr)
                  exit()
            futures = (threadpool.submit(parameter,url,file) for url in urls)
            for i, result in enumerate(as_completed(futures)):
               if result.result():
                  print(result.result())
         else:
            parser.print_help(sys.stderr)
            exit()
      else:
         print(colored('File not exist check it!!','red',attrs=['bold']))
   print(colored('['+str(len(count))+'] Open Redirection Detected','green',attrs=['bold']))
