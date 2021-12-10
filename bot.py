from re import U
import BotReq.bot as bot
import BotReq.util.generate as gen

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

myBot.PrintOutPut(-1)
myBot.runNTimes(5)