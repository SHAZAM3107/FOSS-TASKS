# importing the module 
import tweepy 

# personal details 
consumer_key="BKsPvnWDUfUNw6BxxiRVCrrMw"
consumer_secret="BSS6iGT0rRcNl4BSd8gPSQstBZXP9Clxl0T6KDwXcMV8ObhYLQ"
access_token="1052552933659697152-JYbeuwUoZRnV4QTVisOPuD7e5qvSlr"
access_token_secret="hrWGvWyJwtGYbWgZK1W2F4hbJvrp8rhpG75PFH1qbOSp8"

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 

# authentication of access token and secret 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 

# update the status 
api.update_status(status=input("enter the tweet below\n"))
print("Done!") 
