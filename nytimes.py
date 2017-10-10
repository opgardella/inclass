import requests
from bs4 import BeautifulSoup

#need to be careful with the site you choose
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "lxml")

print("New York Times Headlines:")

#LOOK AT THIS FOR PROJECT 2
#use inspect element in browser to see "story-heading"
#find all returns a list!!!
for story_heading in soup.find_all(class_="story-heading"):
	if story_heading.a: #if heading has an attribute where theres a link (links are a)
		print(story_heading.a.text.replace("\n", " ").strip()) #print it out, \n is newline
	else:
		print(story_heading.contents[0].strip())


##image example
#img tag
#attribute I want is the alt
# .get('alt', 'No alternative text provided!') second value can be whatever I want
