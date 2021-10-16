import questionGenerator
import tweepy
# import schedule
# import time

auth = tweepy.OAuthHandler("apiKey",
                           "apiKey")

auth.set_access_token("apiKey",
                      "apiKey")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


def tweet():
    newTweetText = "#stackOverflowQuestionBot\n " + \
        questionGenerator.generateQuestion()
    api.update_status(newTweetText)
    print(newTweetText)


tweet()
