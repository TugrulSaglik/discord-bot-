import discord
import responses 
import asyncio
import os
from dotenv import load_dotenv
import dotenv
import datetime
from random import randint

#Loads .env file that carries the discord token

load_dotenv("C:/Users/tugru/OneDrive/Masaüstü/Kodlama/discord.env")

 

        
#Defines the function that will run when bot is initiated    
def run_discord_bot():    
    TOKEN = os.getenv("DISCORD_TOKEN")    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    #This function returns a variation of the message where emoji/emojis are removed from any new sent message
    async def censor_emoji(message):
      censored_message = message.replace("😃", "**[BU EMOJİ YASAKLANMIŞTIR]** ")
      
      return censored_message
    
     
    
    @client.event
    
    #Defines a function that makes sure the bot is logged in so it can execute the following loops without any errors 
    async def on_ready():
        await client.wait_until_ready()
        
        
        client.loop.create_task(main())
        #client.loop.create_task(sec())
        
    
    @client.event
    
    #Defines a function which instructs the bot on what to do when any new message is sent
    async def on_message(message):
        channel = message.channel
        nameofchannel = channel.name
        if "i" in nameofchannel:
          nameofchannel = nameofchannel.replace("i","<")
        messagechannel = os.getenv("{}".format(nameofchannel))
        os.environ["{}".format(nameofchannel)] = str(int(messagechannel) + 1)
        dotenv.set_key("C:/Users/tugru/OneDrive/Masaüstü/Kodlama/discord.env", "{}".format(nameofchannel), os.environ["{}".format(nameofchannel)])
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)

               
        """
        Checks if the censored emoji/emojis are in the message's content.
        If its in the content, then it deletes the original message and sends a modified version of it
        """
        if "😃" in message.content:
          
            user_id = message.author.id
            await message.delete()
            channel = message.channel
            nameofchannel = channel.name
            if "i" in nameofchannel:
             nameofchannel = nameofchannel.replace("i","<")
            messagechannel = os.getenv("{}".format(nameofchannel))
            os.environ["{}".format(nameofchannel)] = str(int(messagechannel) - 1)
            dotenv.set_key("C:/Users/tugru/OneDrive/Masaüstü/Kodlama/discord.env", "{}".format(nameofchannel), os.environ["{}".format(nameofchannel)])
            censored_message = await censor_emoji(message.content)
            await message.channel.send(f"<@{user_id}> şahsının **düzeltilmiş** mesajı: " + censored_message)
        
        
         #If no other condition is met, it sends the result it gets from the handle_response function  
        elif responses.handle_response(message.content,nameofchannel) == None:
          return
        elif responses.handle_response(message.content,nameofchannel) == "boradan ss gönder":
          bora_possible_images = ["C:/Users/tugru/OneDrive/Masaüstü/Kodlama/bora_apzına_alıyor.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/bora_loves_minors.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/bora_tank_namlusu.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/bora_when_minors.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/kedi.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/sussy_bora.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/yaş_sadece_sayı.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/zencigöt.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/anal_fisting_bora.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/arkadan_anal.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/mükemmel_erkek_bora.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/sik_o_taşları.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/ortalama_bora_anı.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/medeni.png"]  
          await channel.send(file=discord.File(bora_possible_images[randint(0,len(bora_possible_images)-1)]))
        elif responses.handle_response(message.content,nameofchannel) == "ozandan ss gönder":
          ozan_possible_images = ["C:/Users/tugru/OneDrive/Masaüstü/Kodlama/adam_gay_değil.png", "C:/Users/tugru/OneDrive/Masaüstü/Kodlama/ağzına_almadan_duramıyor.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/alt_insanlarla_konuşurken_ben.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/her_gün_ağzına.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/ilk_evcilleştirilen_hayvan.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/kas_ne_amk.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/oç_ozan.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/sandalye_ozan.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/şarkıyı_rape.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/savaş_çıkınca_ben.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/zenci_karşıtı_ozan.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/türk_memeler.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/rape_teacher.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/ozan_löp_löp.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/memeyi.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/meme_yapamıyor.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/git_otobüs.png"]
          await channel.send(file=discord.File(ozan_possible_images[randint(0,len(ozan_possible_images)-1)]))
        elif responses.handle_response(message.content,nameofchannel) == "tuğruldan ss gönder":
          tuğrul_possible_images = ["C:/Users/tugru/OneDrive/Masaüstü/Kodlama/egzoz.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/ınga.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/kar.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/kaymak.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/müğzik.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/tokyo.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/wednesday.png","C:/Users/tugru/OneDrive/Masaüstü/Kodlama/zenci_kız.png"]
          await channel.send(file=discord.File(tuğrul_possible_images[randint(0,len(tuğrul_possible_images)-1)]))
        else:
          await channel.send(responses.handle_response(message.content,nameofchannel))
    
    
    @client.event
    
    #Defines a function which sends "I hate niggers" every 6 hours in a specific channel
    async def interval_task(channel): 
      await channel.send("I hate niggers")

    async def main():
      channel = client.get_channel(855450711356866610)
      await ping_ozan()
      interval = 21600
      while True:
          await interval_task(channel)
          await asyncio.sleep(interval)
          
    #@client.event
    #async def interval_bora_ping(channel):
      user_id = 856931709761355807
      await channel.send(f"<@{user_id}> gel oç bora")
    
    #async def sec():
      channel = client.get_channel(855450711356866610)
      interval = 0
      while True:
        await interval_bora_ping(channel)
        await asyncio.sleep(interval)
      
          
    @client.event
    async def on_message_edit(before, after):
    # Check if the edited message contains an emoji that is not allowed
      if "😃" in after.content:
       # Get the user's ID
       user_id = after.author.id
       # Delete the original message
       await after.delete()
       channel = after.channel
       nameofchannel = channel.name
       if "i" in nameofchannel:
          nameofchannel = nameofchannel.replace("i","<")
       messagechannel = os.getenv("{}".format(nameofchannel))
       os.environ["{}".format(nameofchannel)] = str(int(messagechannel) - 1)
       dotenv.set_key("C:/Users/tugru/OneDrive/Masaüstü/Kodlama/discord.env", "{}".format(nameofchannel), os.environ["{}".format(nameofchannel)])
       # Censor the message
       censored_message = await censor_emoji(after.content)
       # Send the censored message
       await after.channel.send(f"<@{user_id}> şahsının **düzeltilmiş** mesajı: " + censored_message)

    @client.event
    async def ping_ozan():
         channel = client.get_channel(855450711356866610)
         message_count = 0
         async for message in channel.history(limit=1):
          timestamp = message.created_at
          formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
          #if "gel oç bora" in message.content:
           #await message.delete()
           #channel = message.channel
           #nameofchannel = channel.name
           #if "i" in nameofchannel:
            #nameofchannel = nameofchannel.replace("i","<")
           #messagechannel = os.getenv("{}".format(nameofchannel))
           #os.environ["{}".format(nameofchannel)] = str(int(messagechannel) - 1)
           #dotenv.set_key("C:/Users/tugru/OneDrive/Masaüstü/Kodlama/discord.env", "{}".format(nameofchannel), os.environ["{}".format(nameofchannel)])
          if "😃" in message.content:
           censored_message = await censor_emoji(message.content)
           await channel.send(f"<@{message.author.id}> şahsının **düzeltilmiş** mesajı: " + censored_message + "\n" +"\n" + formatted_timestamp)
           await message.delete()
           channel = message.channel
           nameofchannel = channel.name
           if "i" in nameofchannel:
            nameofchannel = nameofchannel.replace("i","<")
           messagechannel = os.getenv("{}".format(nameofchannel))
           os.environ["{}".format(nameofchannel)] = str(int(messagechannel) - 1)
           dotenv.set_key("C:/Users/tugru/OneDrive/Masaüstü/Kodlama/discord.env", "{}".format(nameofchannel), os.environ["{}".format(nameofchannel)])
          message_count += 1
          print("{0:.2%} tamamlandi :)!".format(message_count/100))
    
  
    
    client.run(TOKEN)
