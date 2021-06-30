# import required modules
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import requests
import time

# get URL

topic = input("I will attempt to learn word associations by scanning Wikipedia. What is the topic? ")
address = "https://en.wikipedia.org/wiki/"+topic
page = requests.get(address)

# scrape webpage
soup = BeautifulSoup(page.content, 'html.parser')

list(soup.children)

# find all occurance of p in HTML
# includes HTML tags
# print(soup.find_all('p'))

# print('\n\n')

# return only text
# does not include HTML tags
# paragraphCount = len(soup.find_all("p"))
# output = soup.find_all('p')[0].get_text()
# print(output)
# print(" ")

# count = 0
# output = output.split(' ')
# length = len(output)

# print("length ", length)


paragraphCount = len(soup.find_all("p"))

paragraphList = []
# Get all paragraphs
for paragraph in range(paragraphCount-1):
    # print("ITERATION: ", paragraph)
    output = soup.find_all('p')[paragraph].get_text()
    # print(output)
    paragraphList.append(output)

paragraphListLength = len(paragraphList)-1
# print(paragraphListLength)

Done = False

qualities = []


def word_count(output):
    counts = dict()

    for word in output:
        if word in counts:
            counts[word.lower()] += 1
        else:
            counts[word.lower()] = 1

    # try:
    #     del counts['END OF QUALITY']
    #     del counts['the']
    #     del counts['and']
    #     del counts['to']
    #     del counts['of']
    #     del counts['a']
    #     del counts['in']
    #     del counts['on']
    #     del counts['as']
    #     del counts['at']
    #     del counts['that']
    #     del counts['with']
    #     del counts['is']
    #     del counts['from']
    #     del counts['for']

    # except KeyError:
    #     pass

    stop_words = set(stopwords.words('english'))

    for key in list(counts):
        if (key in stop_words):
            try:
                del counts[key]
            except KeyError:
                pass

    sort_counts = sorted(counts.items(), key=lambda x: x[1], reverse=False)

    return sort_counts


for paragraph in paragraphList:
    output = paragraph.split(' ')
    for index in range(len(output)):
        # print("output[i] ", output[index])
        # print("out of loop")
        if (output[index] == 'is'):
            index += 1
            # and output[index][-1] != ',
            while index < len(output) - 1:
                if (output[index][-1] != '.'):
                    qualities.append(output[index])
                    index += 1
                elif (output[index][-1] == '.'):
                    qualities.append(output[index])
                    index += 1
                    qualities.append("END OF QUALITY")
                # print(output[index])

    sort_counts = word_count(qualities)

print("I have learned the following word associations about this topic....")
for i in sort_counts:
    if (i[1] > 4 ):
        print(i[0], i[1])
        time.sleep(1)
