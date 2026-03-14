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
           
           
    def analyze_text(self,text):



    def worker(self):





     def run(self,num_threads=4):
        threads=[]
        
        for i in range(num_threads):


           




        
class ResultExporter:



def main():
    urls=[
                 "https://example.com",
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.bbc.com"
       ]
     keywords=["python", "data", "code", "programming"]
     crawler=WebCrawler(urls,keywords)
     print("\n Starting crawler...\n")
     results=crawler.run(num_threads=4)
     print("\nAnalysis Results\n")

     for url,data in results.items():
             print(url)
             for k,v in data.items():
                     print(f" {k}:{v}")
              print()
     exporter=ResultExporter(results)
     exporter.export_to_file()

if __name__=="__main__":
   main()
