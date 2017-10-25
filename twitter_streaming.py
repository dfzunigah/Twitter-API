#Import the neccesary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "your_acess_token_here"
access_token_secret = "your_acess_token_secret_here"
consumer_key = "your_consumer_key_here"
consumer_secret = "your_consumer_secret_here"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':

    #This handles Twitter authentificaction and the conection to Twitter Streaming API
    l = StdOutListener()
    auth =  OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords you give (i.e. 'enterpreneur', '#ThisIsaHashtag')
    stream.filter(track= ['your_keyword_here'])
