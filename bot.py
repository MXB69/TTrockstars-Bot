import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

from tkinter import *
import tkinter as tk
import tkinter.font as font



window = tk.Tk()
window.geometry("850x700")

for i in range(9):
    if(i == 1):
        window.columnconfigure(i, weight=4)
    else:
        window.columnconfigure(i, weight=1)

for x in range(16):
    window.rowconfigure(x, weight=1)

window.configure(background="black")

myFont = font.Font(family="Arial", size=12)

school_name_tk = tk.Label(window, text="School Name",
                          fg="white", bg="black", font=myFont)
school_name_tk.grid(row=1, column=1)
entry1 = tk.Entry()
entry1.grid(row=1, column=2)


username_tk = tk.Label(window, text="Username",
                       fg="white", bg="black", font=myFont)
username_tk.grid(row=3, column=1)
entry2 = tk.Entry()
entry2.grid(row=3, column=2)


password_tk = tk.Label(
    window, text="Account Password (Leave blank if using pin)", fg="white", bg="black", font=myFont)
password_tk.grid(row=5, column=1)
entry3 = tk.Entry()
entry3.grid(row=5, column=2)


pin_tk = tk.Label(window, text="Account Pin (Leave blank if using password)",
                  fg="white", bg="black", font=myFont)
pin_tk.grid(row=7, column=1)
entry4 = tk.Entry()
entry4.grid(row=7, column=2)


chosen_password_tk = tk.Label(
    window, text="Pin if its in numbers else password", fg="white", bg="black", font=myFont)
chosen_password_tk.grid(row=9, column=1)
entry5 = tk.StringVar()
r1 = tk.Radiobutton(window, text='Password', variable=entry5,
                    value='Password',font=myFont)
r1.grid(row=9, column=2)
r2 = tk.Radiobutton(window, text='Pin', variable=entry5,
                    value='Pin',font=myFont)
r2.grid(row=10, column=2)


gamenumber_tk = tk.Label(
    window, text="The number of games you want the bot to play", fg="white", bg="black", font=myFont)
gamenumber_tk.grid(row=11, column=1)
entry6 = tk.Entry()
entry6.grid(row=11, column=2)

gamenumber_tk = tk.Label(
    window, text="Interval between answers (0.1 recommended", fg="white", bg="black", font=myFont)
gamenumber_tk.grid(row=12, column=1)
entry9 = tk.Entry()
entry9.grid(row=12, column=2)


gamemode_tk = tk.Label(window, text="The gamemode",
                       fg="white", bg="black", font=myFont)
gamemode_tk.grid(row=13, column=1)
entry7 = tk.StringVar()
e1 = tk.Radiobutton(window, text="Garage", variable=entry7,value="Garage",font=myFont)
e2 = tk.Radiobutton(window, text="Studio", variable=entry7, value="Studio",font=myFont)
e1.grid(row=13, column=2)
e2.grid(row=14, column=2)

def getAllValues():
    global School
    global username_string
    global password_string
    global mode_to_play
    global games_to_play
    global pin_string
    global chosen_password
    global time_to_sleep
    School = entry1.get()
    username_string = entry2.get()
    password_string = entry3.get()
    mode_to_play = entry7.get()
    games_to_play = int(entry6.get())
    pin_string = entry4.get()
    chosen_password = entry5.get()
    time_to_sleep = float(entry9.get())
    

def quit():
  window.destroy()


MyButton1 = Button(window, text="Run Bot", command=lambda: [
                   getAllValues(), quit()])

MyButton1.grid(row=15, column=5)

window.mainloop()


option = webdriver.ChromeOptions()

option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

option.add_argument("window-size=1280,800")


driver = webdriver.Chrome(
    executable_path=r".\chromedriver.exe", options=option)


website = driver.get("https://play.ttrockstars.com/auth/school/student")


time.sleep(3)


schoolForm = driver.find_element_by_id("mat-input-0")

schoolForm.click()
time.sleep(5)
schoolForm.send_keys(School)
time.sleep(2.5)

autocomplete_School = driver.find_element_by_xpath(
    "/html/body/div[2]/div/div/div/mat-option")

time.sleep(5)


try:
    autocomplete_School.click()
except(StaleElementReferenceException):
    time.sleep(2)
    autocomplete_School.click()


time.sleep(3)


username = driver.find_element_by_id('mat-input-1')

print("Check the School name")

username.clear()
username.click()
username.send_keys(username_string)

time.sleep(1)

if(chosen_password == 'Password'):
    password_button = driver.find_element_by_xpath(
        "/html/body/ttr-root/ttr-root-app/div/mat-sidenav-container/mat-sidenav-content/div/section/ttr-login2/ttr-splash/div/div/div/ttr-login-form/div/form/mat-card/div[3]/div[2]/button")
    time.sleep(0.5)
    password_button.click()
    time.sleep(1.5)
    password = driver.find_element_by_id('mat-input-2')
    time.sleep(1)
    password.clear()
    password.click()
    password.send_keys(password_string)
elif(chosen_password == "Pin"):
    pin_button = driver.find_element_by_xpath(
        "/html/body/ttr-root/ttr-root-app/div/div/section/ttr-login2/ttr-splash/div/div/div/ttr-login-form/div/form/mat-card/div[3]/div[1]/button")
    time.sleep(0.5)
    pin_button.click()
    time.sleep(1.5)
    pin = driver.find_element_by_id('mat-input-2')
    time.sleep(1)
    pin.clear()
    pin.click()
    pin.send_keys(pin_string)


time.sleep(3)


Login_Button = driver.find_element_by_css_selector(
    ".mat-card-actions .mat-button:first-child, .mat-card-actions .mat-raised-button:first-child, .mat-card-actions .mat-stroked-button:first-child")

Login_Button.submit()


time.sleep(7)
global gamemode_to_play

if (mode_to_play == 'Garage'):

    gamemode_to_play = driver.find_element_by_xpath(
        "/html/body/ttr-root/ttr-root-app/div/mat-sidenav-container/mat-sidenav-content/div/section/ttr-play-page/section/nav/ttr-game-list[1]/div/div/button[1]/mat-card/button")

    gamemode_to_play.click()

elif(mode_to_play == 'Studio'):

    gamemode_to_play = driver.find_element_by_xpath(
        "/html/body/ttr-root/ttr-root-app/div/mat-sidenav-container/mat-sidenav-content/div/section/ttr-play-page/section/nav/ttr-game-list[1]/div/div/button[3]/mat-card/button")

    gamemode_to_play.click()

elif(mode_to_play == 'Festival'):

    gamemode_to_play = driver.find_element_by_xpath(
        "/html/body/ttr-root/ttr-root-app/div/mat-sidenav-container/mat-sidenav-content/div/section/ttr-play-page/section/nav/ttr-game-list[2]/div/div/button[1]")

    gamemode_to_play.click()
    time.sleep(2)

    gamemode_to_play_2 = driver.find_element_by_xpath(
        "/html/body/ttr-root/ttr-root-app/div/mat-sidenav-container/mat-sidenav-content/div/section/ttr-play-page/section/div/ttr-festival-preview/ttr-game-preview/mat-card/div[2]/ttr-game-stages/div/div[4]/ttr-game-stage")

    gamemode_to_play_2.click()


time.sleep(6)



def play_again():
        driver.find_element_by_css_selector(
            "body > ttr-root > ttr-root-app > div > mat-sidenav-container > mat-sidenav-content > div > section > ttr-studio > ttr-game-holder > div > div > div > button.mat-focus-indicator.margin-5.play-button.stamp.mat-raised-button.mat-button-base.mat-accent.ng-star-inserted").click()
        time.sleep(5.5)


def calculator(x):
    if(type(x) == type(username_string)):
        equation = 0
        if(x == '11 × 11'):
            equation += 121
        elif(x == "108 ÷ 9"):
            equation += 12
        elif(len(x) == 5):
            equation += int(x[0])

            if(x[2] == '×'):
                equation *= int(x[-1])

            elif(x[2] == '÷'):
                equation /= int(x[-1])

        elif((len(x) == 6) & (x[1].isdigit() == True)):
            equation += int(x[0:2])

            if(x[3] == '×'):
                equation *= int(x[-1])

            elif(x[3] == '÷'):
                equation /= int(x[-1])

        elif((len(x) == 6) & (x[-2].isdigit() == True)):

            equation += int(x[0])

            if(x[2] == '×'):
                equation *= int(x[-2:])

            elif(x[2] == '÷'):
                equation /= int(x[-2:])

        elif((len(x) == 7) & (x[-2].isdigit() == True) & (x[0:2].isdigit() == True)):

            equation += int(x[0:2])
            if(x[3] == '×'):
                equation *= int(x[-2:])

            elif(x[3] == '÷'):
                equation /= int(x[-2:])

        elif(len(x) == 8):
            equation += int(x[0:3])
            equation /= int(x[-2:])

        elif(x == '12 × 12'):
            equation += 12

        return int(equation)
    else:
        time.sleep(2)





def iterate(w):
    list = []
    for i in str(w):
        list.append(int(i))
    return list


def iterate2(w):
    list2 = []
    for i in str(w):
        list2.append(int(i))
    return list2

global question_future
global question_present

def getQuestion():
    if(mode_to_play == "Studio"):
        question_present = driver.find_element_by_css_selector(
            "ttr-game-question .current:not(.missing)").text
    elif(mode_to_play == "Garage"):
        question_present = driver.find_element_by_css_selector(
            "ttr-game-question .current:not(.missing)").text
    
    return question_present
        




def key_press_studio():

    for i in range(1):
        if(1000 != 0):

            a_string = getQuestion()

            print(a_string)

            answer = calculator(a_string)

            print(answer)

            answer_complete_list = iterate(answer)

            for i in answer_complete_list:
                driver.find_element_by_xpath('/html/body').send_keys(i)
            driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)


def run():
    for i in range(3500000):
        key_press_studio()
        time.sleep(time_to_sleep)

for i in range(games_to_play):
    try:
        run()
    except(NoSuchElementException, StaleElementReferenceException):
        time.sleep(2)
        
    try:
        play_again()
    except(NoSuchElementException, StaleElementReferenceException):
        pass
    try:
        gamemode_to_play.click()
    except(NoSuchElementException, StaleElementReferenceException):
        pass
