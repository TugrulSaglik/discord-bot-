import string
from random import randint
import re
import os
from dotenv import load_dotenv
import discord

load_dotenv("C:/Users/tugru/OneDrive/Masaüstü/Kodlama/discord.env")


#Checks if there is a pattern of several letters line up in a specific way with nothing before and after the sequence
def check_for_zort(message):
  pattern = r"\bz+o+r+t\b"  
  if re.search(pattern, message, re.IGNORECASE):
    return True
  return False  

#The function that determines how to respond to any given message
def handle_response(message):
  
  #Message is converted into lowercase version so more variations of the same message could be recognized as the same
    p_message = message.lower()
    
    """
    The following if statement checks if the first three indexes of the message is "max". 
    If it is, and there is no such file as "yarrak.txt" then it creates such a file with an integer of 0, then adds 1 to it and saves.
    Or, if there is such a file as "yarrak.txt" then it increments by 1 and saves it.
    """
    if p_message[0] == "m" and p_message[1]== "a" and p_message[2] == "x":
      
        f = open("yarrak.txt",'r') 
        data = f.read() 
        counter = int(data)   
        
        datatowrite =str(counter + 1) 
        a = open("yarrak.txt",'w')
        a.write(datatowrite) 
        a.close()
        return message
    
    """
    The following if statements checks if the data on "yarrak.txt" is greater then zero.
    If it isn't, it creates a variable as "counter" with a value of 0, and then it returns a string.
    If it is greater than zero, then it creates a variable equal to the integer and then returns a string.
    """
    if p_message == "counter":
        f = open("yarrak.txt",'r') 
        data = f.read() 
        if not len(data) > 0: 

          counter = 0
        else:
          counter = int(data)
        return str(counter) + " kere max."
    
    if p_message == "borağ":
      
      return "efe(zoomeg) ve aral borayı sikeyim."
    
    if p_message == "niggers":
      return "I hate niggers"
    
    if p_message == "zzzzz":
      return "documentation yok ozan sorma"
    
    if p_message == "yusuf ananı sikebilir miyim":
      return "evet efendim, serbestçe sikebilirsiniz annemi."
    
    if p_message == "mahmut, tuğrul hakkında ne düşünüyorsun?":
      return "direkt allahım"
    
    if p_message == "mahmut, bora hakkında ne düşünüyorsun?":
      return "based birisi ama underage arkadaşları o kadar based değil"
    
    if p_message == "iyi geceler yusuf":
      return "iyi geceler 😏 🤙 "  
    
    if check_for_zort(p_message) == True:
      zort_answers = ["zort ", "zarttiri zort zort ", "ZORT ", "zzzzzORT ", "ZART ZURT ","lol ZORT "]
      if "bora" in p_message:
        possible_bora = ["bora", "boraĞ", "söğü", "bora güneş", "ğağeş", "güneş bora", "söğü ğaneş"]
        return zort_answers[randint(0,5)] + possible_bora[randint(0,6)]
      elif "ozan" in p_message:
        possible_ozan = ["ozan","ozi","ozan ölmez", "ozan DÖNMEZ", "ozi mozi", "ozan ölmez kuşu ötmez"]
        return zort_answers[randint(0,5)] + possible_ozan[randint(0,5)]
      elif "tuğrul" in p_message:
        possible_tuğrul = ["tugug", "tuğrul", "tuğrul SAĞLIK", "tugug salak","ibo tugug saĞ"]
        return zort_answers[randint(0,5)] + possible_tuğrul[randint(0,4)]
      return zort_answers[randint(0,5)]
    
    if p_message == "!mesajsayısı":
      toplam_mesajlar = os.getenv("CHANNEL_MESSAGE") 
      return "Toplamda #genel kanalında {} tane mesaj var!".format(toplam_mesajlar)