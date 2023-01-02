import discord
import responses 
import asyncio
import os
from dotenv import load_dotenv
import dotenv
import datetime

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
        
    
    @client.event
    
    #Defines a function which instructs the bot on what to do when any new message is sent
    async def on_message(message):
        if message.channel == client.get_channel(855450711356866610):
          messagechannel = os.getenv("CHANNEL_MESSAGE")
          os.environ["CHANNEL_MESSAGE"] = str(int(messagechannel) + 1)
          dotenv.set_key("C:/Users/tugru/OneDrive/Masaüstü/Kodlama/discord.env", "CHANNEL_MESSAGE", os.environ["CHANNEL_MESSAGE"])
        if message.author == client.user:
              return
        username = str(message.author)
        user_message = str(message.content)
        channel = message.channel
        list = ["borağ","niggers","zzzzz"]
        msg_content = message.content.lower()
        
        #Checks if the keywords are in the message, then decides to delete it or not
        if any(word == msg_content for word in list):
         await message.delete()
         
      
        """
        Checks if the censored emoji/emojis are in the message's content.
        If its in the content, then it deletes the original message and sends a modified version of it
        """
        if "😃" in message.content:
          
            user_id = message.author.id
            await message.delete()
            censored_message = await censor_emoji(message.content)
            await message.channel.send(f"<@{user_id}> şahsının **düzeltilmiş** mesajı: " + censored_message)
        
        
        #If no other condition is met, it sends the result it gets from the handle_response function  
        else:
          await channel.send(responses.handle_response(message.content))
    
    
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
          
    @client.event
    async def on_message_edit(before, after):
    # Check if the edited message contains an emoji that is not allowed
      if "😃" in after.content:
       # Get the user's ID
       user_id = after.author.id
       # Delete the original message
       await after.delete()
       # Censor the message
       censored_message = await censor_emoji(after.content)
       # Send the censored message
       await after.channel.send(f"<@{user_id}> şahsının **düzeltilmiş** mesajı: " + censored_message)
       if after.channel == client.get_channel(855450711356866610):
          messagechannel = os.getenv("CHANNEL_MESSAGE")
          os.environ["CHANNEL_MESSAGE"] = str(int(messagechannel) - 1)
          dotenv.set_key("C:/Users/tugru/OneDrive/Masaüstü/Kodlama/discord.env", "CHANNEL_MESSAGE", os.environ["CHANNEL_MESSAGE"])

    @client.event
    async def ping_ozan():
         channel = client.get_channel(855450711356866610)
         message_count = 0
         async for message in channel.history(limit=1000):
          timestamp = message.created_at
          formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
          if "😃" in message.content:
           censored_message = await censor_emoji(message.content)
           await channel.send(f"<@{message.author.id}> şahsının **düzeltilmiş** mesajı: " + censored_message + "\n" +"\n" + "\n" + formatted_timestamp + "   (yazılan zaman türkiye saatinden 3 saat geridedir.)")
           await message.delete()
           if message.channel == client.get_channel(855450711356866610):
            messagechannel = os.getenv("CHANNEL_MESSAGE")
            os.environ["CHANNEL_MESSAGE"] = str(int(messagechannel) - 1)
            dotenv.set_key("C:/Users/tugru/OneDrive/Masaüstü/Kodlama/discord.env", "CHANNEL_MESSAGE", os.environ["CHANNEL_MESSAGE"])
          
          message_count += 1
          print("{0:.1%} tamamlandi :)!".format(message_count/1000))
    
  
    
    client.run(TOKEN)
