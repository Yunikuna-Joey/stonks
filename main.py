# remember to run pip install discord.py 
import discord 
from discord.ext import commands 

# here remember to run pip install python-dotenv(?)
from dotenv import load_dotenv
load_dotenv()
import os 

# here remember to run pip install yfinance in cmd for these imports  
import yfinance as yf 

# establish connection to discord server 
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.messages = True 
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command() 
async def info(ctx, ticker): 
    stats = yf.Ticker(ticker)
    data = stats.history(period="id")

    if data.empty: 
        await ctx.send(f'No data available for symbol {ticker}.')
    else: 
        last_close_price = data.iloc[-1]['Close']
        await ctx.send(f'Last close price for {ticker}: {last_close_price}')

bot.run(TOKEN)


