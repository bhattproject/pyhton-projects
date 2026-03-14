import threading 
import requests
from collections import Counter
from queue import Queue
import re
import time
imoprt logging


#Configure logging
logging.basicConfig(
level=logging.INFO,
format="%(threadName)s-%(levelname)s-%(message)s"
)

class WebCrawler:
   def __init__(self,urls,keywords):
       self.urls=urls
       self.keywords=keywords
       self.queue=Queue()
       self.results={}
       self.lock=threading.Lock()
       
       for url in urls:
           self.queue.put(url)
   def fetch_page(self,url):
       try:
           response=requests.get(url,timeout=5)
           return response.text.lower()
       except Exception as e:
           logging.error(f"Failed to fetch{url}:{e}")
           return ""
           
           
    def analyze
