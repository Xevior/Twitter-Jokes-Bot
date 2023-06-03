import tweepy
import requests
import re



# Twitter API credentials
api_key= ""
api_secret= ""
bearer_token= r""
access_token= ""
access_token_secret= ""

client= tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
# Create an API object
auth = tweepy.OAuthHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


limit = 1
api_url = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(limit)
response = requests.get(api_url, headers={'X-Api-Key': 'API-Ninja API key'})
if response.status_code == requests.codes.ok:
    mike = response.text
    # Extract the joke from the API response
    joke = re.findall(r'"joke": "([^"]+)"', mike)

    # Remove symbols from the joke
    joke = re.sub(r'[^\w\s]', '', joke[0])
    
else:
    print("Error:", response.status_code, response.text)
# Function to print a joke
# Function to tweet a joke
def tweet_joke():

    client.create_tweet(text=joke)
    print("Tweeted:", joke)

# Tweet a joke
tweet_joke()