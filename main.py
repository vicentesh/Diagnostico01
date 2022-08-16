import json

def mostRetweeted():

    tweets = []
    for line in open('farmers-protest-tweets-2021-03-5.json', 'r'):
        tweets.append(json.loads(line))

    print(tweets[0])

def mostActiveUsers():
    print("funcion 2")

def mostTweetsDay():
    print("funcion 3")

def trendingTopics():
    print("funcion 4")

# main function
def main():
    mostRetweeted()
    mostActiveUsers()
    mostTweetsDay()
    trendingTopics()

if __name__ == '__main__':
    main()
