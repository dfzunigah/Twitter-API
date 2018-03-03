#This script allows you getting the profile of all users followed by an account

#Tweepy API auhentification
import tweepy

TWEEPY_CONSUMER_KEY = '###'
TWEEPY_CONSUMER_SECRET = '###'
TWEEPY_ACCESS_TOKEN = '###'
TWEEPY_ACCESS_TOKEN_SECRET = '###'

auth = tweepy.OAuthHandler(TWEEPY_CONSUMER_KEY, TWEEPY_CONSUMER_SECRET)
auth.set_access_token(TWEEPY_ACCESS_TOKEN, TWEEPY_ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

#Get a list of all users id followed by the account "account_here_please"
account = "account_here_please"
friends_id = api.friends_ids(account)

#Search the user related to the id then prints its screen name in a file
for user_id in friends_id:
    user = api.get_user(user_id)
    with open("twitter.txt","a") as file:
        file.write(user.screen_name)
        file.write("\n")
