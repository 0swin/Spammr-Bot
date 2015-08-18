import tweepy
import telebot
from config import *

telegram = telebot.TeleBot(tgToken)
auth = tweepy.OAuthHandler(twConsumerKey, twConsumerSecret)
auth.secure = True
auth.set_access_token(twAccessToken, twAccessTokenSecret)
twitter = tweepy.API(auth)
registeredUser = True


# SCRIPT
def listener(messages):
    global registeredUser
    for message in messages:
        tgContact = message.chat.username
        tgChatID = message.chat.id
        text = message.text
        print tgContact + ": " + text
        if message.content_type == "text" and tgContact == tgUsername:
            registeredUser = True
            print "Registered user"
        else:
            registeredUser = False
            telegram.send_message(tgChatID, "Sorry, you are not allowed to use this bot")
            print "Unregistered user, access denied"


@telegram.message_handler(commands=['tweet'])
def command_tweet(tweet):
    global registeredUser
    tgChatID = tweet.chat.id
    twText = tweet.text
    twText = twText.replace("/tweet ", "")
    if registeredUser:
        if len(twText) <= 140 and registeredUser:
            # twitter.update_status(status=twText)
            telegram.send_message(tgChatID, "Tweet successful")
            print "Tweet successful"
        else:
            telegram.send_message(tgChatID, "Sorry, wrong Twitter API Keys or message too long (max: 140 char.)")
            print "Sorry, wrong Twitter API Keys or message too long (max: 140 char.)"


telegram.set_update_listener(listener)
telegram.polling()
telegram.polling(none_stop=True)
telegram.polling(interval=1)


while True:
    pass
