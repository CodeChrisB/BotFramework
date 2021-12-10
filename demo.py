# Import the BotReq Framework
import BotReq.bot as bot

# Init the url and body of your request
url="https://reqres.in/api/users"
body ={
    "name": "morpheus",
    "job": "leader"
}

# Create your request
myBot = bot.BotReq(body,url)

# Set PrintOutPut(True) so that we can see the response
myBot.PrintOutPut(False)

# Run your request created
myBot.runRequest()

