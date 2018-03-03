#Daniel Zuñiga - 03/03/18 @ National University of Colombia

#This is a script to follow Twitter accounts automatically
#1. Create a file called "follows.txt" in the same folder of this script
#2. Each line of that file must contain the screen name of the account you want to follow

#Warning! - You can get your account blocked if you follow too many people all at once
#           I recommend to use these script each 8-10 minutes and follow 5 accounts per call

#PSD: You can automate this script by using "cron" in Linux, "Windows Task Scheduler" in Windows or AppleScript in Mac

#Tweepy authentication setup#
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
CONSUMER_KEY = '###'
CONSUMER_SECRET = '###'
ACCESS_KEY = '###'
ACCESS_SECRET = '###'
auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
api = tweepy.API(auth)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Open the file and selects the first 5 accounts then overwrites the file
#You can change the number of accounts per call you're gonna follow by changing
#  the value of the "accounts_tb_followed".
accounts_tb_followed = 5
lines = open('follows.txt').readlines()
open('follows.txt', 'w').writelines(lines[accounts_tb_followed:])
lines = lines[:accounts_tb_followed]

#Follows the account if you aren't following it
if (len(lines) > 0):
    flag = 0
    while (flag < accounts_tb_followed):
        to_follow = lines[flag]
        status = api.show_friendship(source_screen_name="researchboi",target_screen_name=to_follow)
        following_them = status[0].following
        if (following_them == False):
            try:
                api.create_friendship(screen_name = to_follow)
                print("Now following: " + to_follow)
            except tweepy.TweepError as e:
                print(e)
        flag += 1
