# BotFramework

## Use cases
- Todo

# Documentation

Import the Library
```
import BotReq.bot as bot
```

Create a Bot instance

```python
url="WebsiteUrl" # The request URL fom the API
body ={} # The response given by the API
myBot = bot.BotReq(body,url)
```

Run the request a single time :

```python
myBot.runRequest()
```

Run the request N times :
```python
myBot.runNTimes(N) #N = amount of requests to send
```

## Options
GmailDotTrick to to change emails
```python
# specifies the key value of the emailfield inside the body 
myBot.PremutGmail("email")
```

Print out the response
```python
# specifies if the result should be printed
myBot.PrintOutResult(True)
```

## Manipulate the body Object

Add  a sigle key-value pair of the body
```python
#Adds a the new key value pair "number":"420" if it does not exist
myBot.ChangeBodyValue("number","420")
```
Change a sigle key-value pair of the body
```python
#Changes the body value of "email"  to "john.smith@gmail.com" if it exist
myBot.ChangeBodyValue("email","john.smith@gmail.com")
```