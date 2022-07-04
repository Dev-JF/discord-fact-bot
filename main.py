import discord
import os
import requests
import json
import factAPI
import jokeAPI
import triviaGeneralQuestion
import random



client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )



   


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    factRes = factAPI.randomFactCall()
    jokeRes = jokeAPI.jokeCall()
    triviaGeneralRes = triviaGeneralQuestion.triviaGeneral()
    triviaRes = json.loads(triviaGeneralRes)
    
    
    if message.content == 'random fact':
        response = factRes
        await message.channel.send(response)
        
    if message.content == 'joke':
        response = jokeRes
        await message.channel.send(response)
        
    
    
   
    
    if message.content == 'trivia':
        
        triviaQuestion = triviaRes[0]
        trivQuestion = triviaQuestion['question']
        global trivAnswer
        trivAnswer = triviaQuestion['answer']
        response = trivQuestion
        
        await message.channel.send(response)
    
       
    

    if message.content == trivAnswer:
        
        await message.reply('True', mention_author=True)
   
    if message.content == "I give up":
                 
        await message.reply('The answer is ' + trivAnswer, mention_author=True)
  
    
    
    
    if message.content == 'help':
         helpRes = "To get a random fact type in the keywords: random fact \nTo get a joke type in the keyword:  joke \nFor trivia type in the keyword: trivia, if you guess it right you will get a true. if you cant get it, type in I give up"
         await message.channel.send(helpRes)
        
        


# gets the discord toke form .env file
client.run('your env for discord')
