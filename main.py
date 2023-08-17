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

# just to confirm that bot establishes connection 
# # this event will trigger when the initial connection from the bot --> server is established 
@bot.event
async def on_ready():   # event handler is on_ready or AKA when connection is established bot --> server 
    for guild in bot.guilds: 
        if guild.name == GUILD: 
            break
    print(
        f'{bot.user} has connected to Discord!\n'
        f'{guild.name}(id: {guild.id})\n'  
    )

    # member_list = '\n - '.join([member.name for member in guild.members])
        # translated version of the line above 
    member_list = [] 
    for member in guild.members: 
        member_list.append(member.name)
    member_list = '\n - '.join(member_list)

    # output the people in the guild
    print(f'Guild Members:\n - {member_list}')  # for some reason it only outputs the bot name... EDIT: probably the premissions 
    print('Done!')


# show information about a stock ticker
@bot.command() 
async def info(ctx, ticker): 
    stats = yf.Ticker(ticker)
    data = stats.history(period="id")

    if data.empty: 
        await ctx.send(f'No data available for symbol {ticker}.') 
    else: 
        # iloc is used for index based [r][c] calling 
        last_close_price = data.iloc[-1]['Close']
        await ctx.send(f'Last close price for {ticker}: {last_close_price}')

bot.run(TOKEN)


