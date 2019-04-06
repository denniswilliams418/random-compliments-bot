# Python script to tweet random compliments

#!/usr/bin/env python
import sys
import random
from twython import Twython

# Compliment list – my implemented list was more extensive and personalized to my girlfriend, so I changed it for Github to be more general
compList = ["is so pretty", "is the nicest person I know", "is so cute like how do you just DO that???", "is super caring", "will be there for you no matter what", "is so compassionate"]

# Since the keys are personalized for your specific Twitter Developer account, I had to delete them
# To implement this script for yourself, insert the respective keys below for your Twitter Develop account
apiKey = 'INSERT YOUR API KEY'
apiSecret = 'INSERT YOUR SECRET KEY'
accessToken = 'INSERT YOUR ACCESS TOKEN'
accessTokenSecret = 'INSERT YOUR SECRET TOKEN'

# Init Twitter API
api = Twython(apiKey, apiSecret, accessToken, accessTokenSecret)

# Generate a random number to choose a compliment from the list of compliments
randomComp = random.randint(0, len(compList)+1)
myTweet = "Liz" + compList[randomComp]  # Liz is my girlfriend's name

api.update_status(status = myTweet)
