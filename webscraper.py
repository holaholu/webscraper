import requests as r                  #make sure requests is installed
from bs4 import BeautifulSoup         #make sure bs4 is installed



def scrape(websiteToScrape, tagToScrape,fileName): #function to scrape a webpage of a desired html tag 
    with open(fileName, 'w') as f:       #Creates/opens a new file 
    #Scrape the webpage
      response = r.get(websiteToScrape)
      html_content = response.text
      soup = BeautifulSoup(html_content, 'html.parser')
      list=soup.find_all(tagToScrape)
     
     #Write to the file
      if tagToScrape == 'a':  
        for item in list:
          output = item.get('href')
          f.write(str(output) + '\n') 
          print(output)  
      elif tagToScrape == 'img': 
        for item in list:
         output =item.get('src')
         f.write(str(output) + '\n')  
         print(output) 
      else:
        for item in list:
            output = item
            print(output)
            f.write(str(output) + '\n') 
    return


websiteToScrape = 'https://www.cnn.com/'     #put the url of the website you want to scrape
tagToScrape = 'img' #use "a" for links, "img" for images, "p" for paragraphs, "h1" for headings, 
fileName = 'cnnimages.csv'    #put name of the file you want to create

scrape(websiteToScrape, tagToScrape,fileName)     #This does the magic


