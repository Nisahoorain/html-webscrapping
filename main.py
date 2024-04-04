#step 0: Environment Setup
import requests
from bs4 import BeautifulSoup


url = "https://i8is.com"


#step 1: Get Html

req = requests.get(url)
content = req.content
# print(content)


#step 2: prase html

contentSoup = BeautifulSoup(content, 'html.parser')
# print(contentSoup)
# print(contentSoup.prettify)



#step 3: tree traversel


#common used type of object:

title = contentSoup.title
# print(title)

# 3.BeautifulSoup
# print(type(contentSoup))

# 1. Tag
# print(type(title))

# 2.NavigableString
# print(type(title.string))


# 4.Comment
# com = "<p><!--  thi is comment --></p>"
# soupcomit = BeautifulSoup(com)
# print(soupcomit)
# print(soupcomit.string)
# print(type(soupcomit.string))


comment = contentSoup.b
# comment = contentSoup.b.string

# print(comment)


para = contentSoup.find_all('p')
# para = contentSoup.find('p').get_text()
# print(para)

# para1 = contentSoup.find('p')['class']
para1 = contentSoup.find_all('p', class_= 'bhf-hidden')
# print(para1)

divs = contentSoup.find_all('div')
# print(divs)

anchor = contentSoup.find_all('a')
# print(anchor)
linkset = set()

for links in anchor:
    if links.get('href') != "#":
        linktext = "https://i8is.com" +links.get('href')
        linkset.add(links)
#         print(linktext)



learncont =  contentSoup.find(class_='bhf-hidden')
# print(learncont)


#.content - a tag childrens are available as a list
#.children - a tag childrens are available as a generator


# for el in learncont.contents:
#     print(el)

# for item in learncont.string:
# for item in learncont.stripped_strings:    
    # print(item)   


# print(learncont.parents)  
# for item in learncont.parents:
#     print(item.name)  


# print(learncont.next_sibling.next_sibling)
# print(learncont.previous_sibling.previous_sibling)



# contentSoup.select('#loginModal')