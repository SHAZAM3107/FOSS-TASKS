# importing the module 
import tweepy 

# storing credentials in token.py and accessing them by importing.
import token


# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(token.consumer_key, token.consumer_secret) 

# authentication of access token and secret 
auth.set_access_token(token.access_token, token.access_token_secret) 
api = tweepy.API(auth) 

# update the status 
api.update_status(status=input("enter the tweet below\n"))
print("Your message is tweeted!!") 
