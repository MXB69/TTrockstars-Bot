import time;
import keyboard;
from selenium import webdriver;
from selenium.webdriver import ActionChains;
from selenium.common.exceptions import NoSuchElementException;
from selenium.webdriver.common.keys import Keys;
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import threading
import sys
import os
import math

School = #Enter the School Name
username_string = #Enter the username
password_string = #Enter your password
mode_to_play = #Enter you mode that you want to play either Garage or Studio
games_to_play = #Enter the number of games to play

option = webdriver.ChromeOptions()

option.add_experimental_option("excludeSwitches", ["enable-automation"])
option.add_experimental_option('useAutomationExtension', False)

option.add_argument("window-size=1280,800")
option.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")


driver = webdriver.Chrome(executable_path=r"C:\Users\MTK29\Downloads\chromedriver.exe", options = option)


if (School == 'Penglais'):

  website = driver.get("https://play.ttrockstars.com/auth/school/student/5197/password")

elif(School == 'Plascrug'):

  website = driver.get("https://play.ttrockstars.com/auth/school/student/5182/password")



time.sleep(5)



username = driver.find_element_by_id('mat-input-1')

username.clear()
username.click()
username.send_keys(username_string)

time.sleep(1)

password = driver.find_element_by_id('mat-input-2')

password.clear()
password.click()
password.send_keys(password_string)

time.sleep(3)


Login_Button = driver.find_element_by_css_selector(".mat-card-actions .mat-button:first-child, .mat-card-actions .mat-raised-button:first-child, .mat-card-actions .mat-stroked-button:first-child")

Login_Button.submit()


time.sleep(7)


if (mode_to_play == 'Garage'):
    
  gamemode_to_play = driver.find_element_by_xpath("/html/body/ttr-root/ttr-root-app/div/div/section/ttr-play-page/section/nav/ttr-game-list[1]/div/div/button[1]/mat-card/button")

  gamemode_to_play.click()

elif(mode_to_play == 'Studio'):

  gamemode_to_play = driver.find_element_by_xpath("/html/body/ttr-root/ttr-root-app/div/div/section/ttr-play-page/section/nav/ttr-game-list[1]/div/div/button[2]/mat-card/button")

  gamemode_to_play.click()

elif(mode_to_play == 'Festival'):

  gamemode_to_play = driver.find_element_by_xpath("/html/body/ttr-root/ttr-root-app/div/div/section/ttr-play-page/section/nav/ttr-game-list[2]/div/div/button[2]/mat-card/div")

  gamemode_to_play.click()

  gamemode_to_play_2 = driver.find_element_by_xpath("/html/body/ttr-root/ttr-root-app/div/div/section/ttr-play-page/section/div/ttr-festival-preview/ttr-game-preview/mat-card/div[2]/ttr-game-stages/div/div[1]/ttr-game-stage/button/mat-card/div[1]")

  gamemode_to_play_2.click()



time.sleep(6)

def play_again():
    if(mode_to_play == 'Studio'):
      driver.find_element_by_xpath("/html/body/ttr-root/ttr-root-app/div/div/section/ttr-studio/ttr-game-holder/div/div/div/button[2]").click()
      time.sleep(7)
    elif(mode_to_play == 'Garage'):
      driver.find_element_by_xpath("/html/body/ttr-root/ttr-root-app/div/div/section/ttr-garage/ttr-game-holder/div/div/div/button[2]").click()
      time.sleep(7)

    



def calculator(x):
  if(type(x) == type(username_string)):
    equation = 0
    if(x == '11 × 11'):
        equation += 121
    elif(len(x) == 5):
      equation += int(x[0])
      
      if(x[2] == '×'): equation *= int(x[-1])
    
      elif(x[2] == '÷'): equation /= int(x[-1])

    elif((len(x) == 6) & (x[1].isdigit() == True)):
      equation += int(x[0:2])
      
      if(x[3] == '×'):
        equation *= int(x[-1])

      elif(x[3] == '÷'): equation /= int(x[-1])


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
        equation += 12;

      
        
    return int(equation)
  else: 
      time.sleep(2)
      


wait_5 = WebDriverWait(driver, 10)

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



if(mode_to_play == 'Studio'):

  question_future = driver.find_element_by_xpath("/html/body/ttr-root/ttr-root-app/div/div/section/ttr-studio/ttr-game-holder/div/div/div/ttr-game-footpedal/section[2]/section/ttr-game-question/span[2]").text

  question_present = driver.find_element_by_css_selector("ttr-game-question .current:not(.missing)").text

  def try_and_except():
    if (type(question_present) != None):
        return driver.find_element_by_css_selector("ttr-game-question .current:not(.missing)").text
    else: 
      time.sleep(1)
      if (question_present != None):
        return question_present
      else: play_again()

  def try_and_except_2():
    if (question_future != None):
      return driver.find_element_by_xpath("/html/body/ttr-root/ttr-root-app/div/div/section/ttr-studio/ttr-game-holder/div/div/div/ttr-game-footpedal/section[2]/section/ttr-game-question/span[2]").text
    else: 
      time.sleep(1)
      if (question_future != None):
        return question_future
      else: play_again()

elif(mode_to_play == 'Garage'):
    question_future = driver.find_element_by_xpath("/html/body/ttr-root/ttr-root-app/div/div/section/ttr-garage/ttr-game-holder/div/div/div/ttr-game-footpedal/section[2]/section/ttr-game-question/span[2]").text

    question_present = driver.find_element_by_css_selector("ttr-game-question .current:not(.missing)").text


    def try_and_except():
      if (type(question_present) != None):
        return driver.find_element_by_css_selector("ttr-game-question .current:not(.missing)").text
      else: 
        time.sleep(1)
        if (question_present != None):
          return question_present
        else: play_again()

    def try_and_except_2():
      if (question_future != None):
        return driver.find_element_by_xpath("/html/body/ttr-root/ttr-root-app/div/div/section/ttr-garage/ttr-game-holder/div/div/div/ttr-game-footpedal/section[2]/section/ttr-game-question/span[2]").text
      else: 
        time.sleep(1)
        if (question_future != None):
          return question_future
        else: pass

 




def key_press_studio():
  
  for i in range(1):
    if(1000 != 0):

      a_string = try_and_except()
      b_string = try_and_except_2()

      print(a_string)
      print(b_string)

      answer = calculator(a_string)
      answer_2 = calculator(b_string)

      print(answer)
      print(answer_2)

      answer_complete_list = iterate(answer)
      answer_complete_list_2 = iterate2(answer_2)

      for i in answer_complete_list:
        driver.find_element_by_xpath('/html/body').send_keys(i)
      driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)


      for j in answer_complete_list_2:
        driver.find_element_by_xpath('/html/body').send_keys(j)
      driver.find_element_by_xpath('/html/body').send_keys(Keys.ENTER)

     





for i in range(games_to_play):
  try:
    for i in range(400000000):   
      key_press_studio()
      time.sleep(0.13)
  except(NoSuchElementException):
    time.sleep(7)
    try:
      play_again()
    except(NoSuchElementException):
      pass