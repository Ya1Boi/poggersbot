from keep_alive import keep_alive
import discord, os, traceback, datetime, threading
from discord.ext import commands

banlist=[738052976723099751, 746241690028736582, 745686303479169105, 741919727110062198, 754459212658114698, 751614817412055081, 738064884159348848, 738064841658335283, 748977999285714996, 753064737721286836, 738064786218025111, 743875265532264479, 741303074857156658, 742386914383888456, 755854291063013539]

serverdadlist=[741804759681335417, 738052976723099748]

async def log(ctx, extra="None"):
	cmdtime=str(datetime.datetime.today()).replace("-", "/").split(".")[0]+" (UTC)"

	cmduser=ctx.author.name+"#"+ctx.author.discriminator

	cmdname=ctx.command.name

	if(cmdname=="ball"):
		cmdname="8ball"
	
	cmdchannel=ctx.channel.name
	cmdserver=ctx.guild.name
	
	if(ctx.channel.id in banlist):
		return
	else:
		logchannel=bot.get_channel(763769618036031488)
		otherlogchannel=bot.get_channel(771455922215583814)
		await logchannel.send(f"Command .{cmdname} used by `{cmduser}` at {cmdtime} in {cmdchannel} ({cmdserver}), Extra Information: `{extra}`\n")
		await otherlogchannel.send(f"Command .{cmdname} used by `{cmduser}` at {cmdtime} in {cmdchannel} ({cmdserver}), Extra Information: `{extra}`\n")


async def sendm(banlist, ctx, text=""):
	if(ctx.channel.id in banlist):
		return
	else:
		await ctx.send(text)

async def sendem(banlist, ctx, embed):
	if(ctx.channel.id in banlist):
		return
	else:
		await ctx.send(embed=embed)
		

#methe
#test banana

bot = commands.AutoShardedBot(command_prefix = '.', description = "it fights dummy",case_insensitive=True)
bot.remove_command('help')
IgnoreImport = []

for Extension in [f.replace('.py', '') for f in os.listdir("Cogs") if os.path.isfile(os.path.join("Cogs", f))]:
	if Extension in IgnoreImport:
		continue
	try:
		print(f"Loading extension {Extension}")
		bot.load_extension(f"Cogs.{Extension}")
		print(f"Extension {Extension} loaded.")
	except (discord.ClientException, ModuleNotFoundError, commands.errors.ExtensionFailed):
		print(f'Failed to load extension {Extension}.')
		traceback.print_exc()

@bot.event
async def on_message(msg):
	
	listofwords=["im", "Im", "iM", "IM", "i'm", "I'm", "i'M", "I'M"]
	for i in listofwords:
		if (msg.content.startswith(i+" ") and msg.guild.id in serverdadlist and msg.channel.id not in banlist and not msg.channel.id == 739288768279740436):
			txt="Hi, "+msg.content.replace(i+" ","",1)+", I'm dad!"
			bruh=msg.guild.roles
			bruh2=[]
			bruh3=[]
			for i in bruh:
				a=i.name
				b=i.id
				bruh2.append(a)
				bruh3.append(b)
			for idx, i in enumerate(bruh3):
				txt=txt.replace(f"<@&{str(i)}>", bruh2[idx])
				txt=txt.replace("@everyone", "everyone")
				txt=txt.replace("@here", "here")
			await msg.channel.send(txt)
	await bot.process_commands(msg)

@bot.event
async def on_ready():
	print('my body is ready \n')
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you"))

keep_alive()
token = os.environ.get("TOKEN")
bot.run(token)
"""
dumb bot made by @retard#9070 v1.3.0, to run it yourself, make a file named .env and paste TOKEN=token in there and replace the lowercase token with your bot token * GITHUB: https://github.com/Ya1Boi/poggersbot *
"""

