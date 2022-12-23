import discord
import responses 
from datetime import datetime, timedelta, time 
import asyncio


 

        
    
def run_discord_bot():    
    TOKEN = "MTA0Mjc3ODgyMjAwNjgwMDM4NA.GHZWM3.GLbk3aH__2KpSBPpF37ZR3oHxa088APFcCLup8"    
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    
    
    @client.event 
    async def on_ready():
        client.loop.create_task(main())
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        list = ["borağ","niggers","zzzzz"]
        msg_content = message.content.lower()
        message_to_send = responses.handle_response(msg_content)
        await channel.send(message_to_send)
        if any(word == msg_content for word in list):
         await message.delete()
              
    
    @client.event
    async def interval_task(channel): 
      await channel.send("I hate niggers")

    async def main():
        channel = client.get_channel(855450711356866610)
    
        interval = 21600
        while True:
        
          await interval_task(channel)
        
          await asyncio.sleep(interval)

    
        
    
    client.run(TOKEN)   