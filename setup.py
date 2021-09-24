import questionGenerator
import tweepy
import schedule
import time

auth = tweepy.OAuthHandler("OTtzalHeqI08xE4I78REKJk9O",
                           "PUdJUYcsbuh74uI4xgaQzPDUT77Qgvw85Hs3dwSEKBkBXGOTkW")

auth.set_access_token("2338774166-Z3sGOyb7XrYw3eHVBascQpSd9jB4K4EbuAbBxDA",
                      "3aKb5XJHCkNsOtGYAnlkwRrsqzu1u1LmFuvB4aLCaJWTc")

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


schedule.every(6).hours.do(tweet)

while True:
    schedule.run_pending()
    time.sleep(1)
