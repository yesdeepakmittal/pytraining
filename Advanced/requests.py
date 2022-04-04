import requests
data = requests.get('https://pythonprogramming.net/static/downloads/short_reviews/negative.txt')

#Opening the file as txt file even for writing bytes like string
with open('negative.txt','wt') as fp:
  print(data.content,file=fp)

type(data.content)  # O/p bytes

# Converting the bytes like string into the string
data = data.content.decode('utf-8', 'ignore')
