import BotReq.bot as bot


url="https://impflotterie-salzburg-ag.at/json/action/promotionActions.php"
body ={
    "action": "submitParticipation",
    "sex": "m",
    "first_name": "Christopher",
    "last_name": "Buchberger",
    "email": "cocoplenty31@gmail.com",
    "address": "28 Ritzlhofstraße",
    "zip": "4052",
    "city": "Ansfelden",
    "policy": "true",
    "data-agreement": "true",
    "save": "1"
}

myBot =bot.BotReq(body,url)

myBot.PremutGmail("email")
myBot.PrintOutPut(True)
myBot.AddBodyValue("email","cocoplenty32")
myBot.AddBodyValue("ee","cocoplenty32")
print(myBot.getBody())
#myBot.runNTimes(5)