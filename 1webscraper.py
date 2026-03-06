import requests 

#import requests library to send http requests to the websites

from bs4 import BeautifulSoup
#import BeautifulSoup from the bs4 and then parse html

url="https://"

#webpage we want to scrape


headers={
        "User-Agents"="Mozilla/5.0"
}

#it help our request look like it cam ef rom the real browser


response=requests.get(url,headers=headers)
#send a get request to a webpage

print("status code:",response.status_code)

#print https status code  200->success,404 ->papge not found ,403->access forbidden,500->server error


soup=BeautifulSoup(reponse.text,"html.parser")
#convert html text to object easily this help us the search the html easily

title=soup.find("h1")
#find the first html tag usually contain the job title

#check if title elemnt was found

if title:
   job_title=title.text.strip()
   #extract the text inside the <h1> tag and remove extra spaces

   print("job title:",job_title)
   #print the job title
else:


 print("title not found")
 #if title was not found  print message






