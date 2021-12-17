import sys
sys.path.insert(0,'..')  # Set the current directory to the parent so we can import stuff

import BotReq.bot as botController
from BotReq.util.enum import ENUM
import BotReq.util.image as image
import BotReq.util.jsonManipulate as jm


# Set the body and the url for our request
bot = botController.BotReq({},"https://dog.ceo/api/breeds/image/random") 

# Set the request type to get
bot.setRequest(ENUM.GET) 

# We want to print out the result
# ReturnOutPut returns the 
bot.RetrunResponse(True)

# loop 5 times, because we want to download 5 random dog images
for i in range(5):
    # Run the GET Request
    response = bot.runRequest() 

    # The response looks like this
    # {"message":"ImageUrl"","status":"success"}
    # We want to extract the message aka the Url
    json = jm.getValue(response,"message") 

    # Download the image save it inside the folder DogImages with the name dog[#].png
    image.downloadImage(json,"./DogImages/dog"+str(i)+".png")

    # Print the url from the image
    print(json)


