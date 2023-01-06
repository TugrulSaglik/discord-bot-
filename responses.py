import string
from random import randint
import re
import os
from dotenv import load_dotenv
import dotenv

load_dotenv("C:/Users/tugru/OneDrive/Masaüstü/Kodlama/discord.env")

#The function that determines how to respond to any given message
def handle_response(content,channel):
  bora_random = ["bora", "güneş", "söğü", "ğaneş", "söğü ğaneş", "bora gübeş", "BORA GÜBEŞ", "ĞAMEŞ SÖĞÜ", "gübeş bora"]
  tuğrul_random = ["tuğrul", "tuğrul SAĞLIK","tugug","tugugi bugugi","tugug saglik","tugrul the lol","ibo tugug","abraham health"]
  ozan_random = ["ozan", "ozi", "ozi mozi", "ozan DÖNMEZ", "ozan ölmez kuşu ötmez", "ozon ülmez", "ozan ölür", "ölmez ozan"]
  p_message = content.lower()  
  
  if "!max" in p_message:
    last_index = p_message.rfind("!max")
    if "bora" in p_message[last_index:]:
      return "max " + bora_random[randint(0,8)]
    elif "ozan" in p_message[last_index:]:
      return "max " + ozan_random[randint(0,7)]
    elif "tuğrul" in p_message[last_index:]:
      return "max " + tuğrul_random[randint(0,7)]
    else:
      return p_message[(last_index)+1:]
    
  elif "!bora" in p_message:
    return "boradan ss gönder"
   
  elif "!ozan" in p_message:
    return "ozandan ss gönder"
  
  elif "!tuğrul" in p_message:
    return "tuğruldan ss gönder"
    
  elif p_message == "!mesajsayısı":
    channel_name = channel 
    toplam_mesajlar = os.getenv("{}".format(channel_name))
    if "<" in channel_name:
      channel_name = channel_name.replace("<", "i")
       
    return "Toplamda #{a} kanalında {b} tane mesaj var!".format(a=channel_name,b= str(int(toplam_mesajlar)+1 ))
  else:
    return