import time, os, sys, telebot, requests
from dotenv import load_dotenv, dotenv_values 
from pyfirmata2 import Arduino

os.system("cls")

PORT = 'COM5'
board = Arduino(PORT)

load_dotenv() 

# Reading the token from the .env file
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Creating the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Handling the command "on"
@bot.message_handler(commands=['start'])
def getOnCommand(message):
    text = "Welcome to our bot.\nYou can type:\n\t/start - to start the bot\n\t/on - to turn the LED on\n\t/off - " 
    text+= "to turn the LED off\n\t/stop - to stop the bot"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    print("LED on")
    board.digital[13].write(1)

# Handling the command "on"
@bot.message_handler(commands=['on'])
def getOnCommand(message):
    text = "You turned the LED on."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    print("LED on")
    board.digital[13].write(1)

# Handling the command "off"
@bot.message_handler(commands=['off'])
def getOffCommand(message):
    text = "You turned the LED off."
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")    
    print("LED off")
    board.digital[13].write(0)

# Handling the command "stop"
@bot.message_handler(commands=['stop'])
def stopExecution(message):
    os.system("cls")
    text = "Your bot has stopped"
    bot.send_message(message.chat.id, text, parse_mode="Markdown")  
    print(text)
    os._exit(os.EX_OK)

# Handling all other commands
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, "You sent " + message.text + ". This command is not supported.")

# Running the bot
bot.infinity_polling()