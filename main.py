from keep_alive import keep_alive
import discord, os, traceback, datetime, random
from discord.ext import commands

fightdict={}
testdict={}

def getfight(id, dicte):
	variables=None
	ids=None
	for a, b in dicte.items():
		if str(id) in a:
			ids=a
			variables=b
	stuff=[ids, variables]
	return stuff

async def log(ctx, extra="None"):
	cmdtime=str(datetime.datetime.today()).replace("-", "/").split(".")[0]+" (UTC)"

	cmduser=ctx.author.name+"#"+ctx.author.discriminator

	try:
		cmdname=ctx.command.name
	except:
		cmdname="(dad)"

	if(cmdname=="ball"):
		cmdname="8ball"
	
	cmdchannel=ctx.channel.name
	cmdserver=ctx.guild.name
	
	extra = extra.replace("`", "")
	logchannel=bot.get_channel(781124111216017458)
	otherlogchannel=bot.get_channel(763769618036031488)
	await logchannel.send(f"Command .{cmdname} used by `{cmduser}` at {cmdtime} in {cmdchannel} ({cmdserver}), Extra Information: `{extra}`\n")
	await otherlogchannel.send(f"Command .{cmdname} used by `{cmduser}` at {cmdtime} in {cmdchannel} ({cmdserver}), Extra Information: `{extra}`\n")

#methe
#test banana

bot = commands.AutoShardedBot(command_prefix = ".", description = "it fights dummy",case_insensitive=True)
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
	if str(msg.author.id) in str(fightdict):
		fight=getfight(msg.author.id, fightdict)
		p1id=int(fight[0].split("/")[1])
		p2id=int(fight[0].split("/")[2])
		p1=None
		if msg.author.id == p1id:
			p1=True
		elif msg.author.id ==p2id:
			p1=False
		attnames=["attack","att","a","attack1","att1","a1","1"]
		att2names=["secondary attack","secondary att","secondary a","sec attack","sec att","sec a","s attack","s att","s a","attack2","att2","a2","2"]
		if(msg.content.lower() in attnames):
			if(p1==True and fight[1]["turn"]==True):
				randomdmg=round(random.randint(15, 20)*fight[1]["guardp2"])
				if fight[1]["focusturnp1"]==fight[1]["turncounter"]:
					randomdmg=round(randomdmg*2)
				new = {
					"p1hp" : fight[1]["p1hp"],
					"p2hp" : fight[1]["p2hp"]-randomdmg,
					"turn" : False,
					"turncounter": fight[1]["turncounter"]+1,
					"focusturnp1": fight[1]["focusturnp1"],
					"focusturnp2": fight[1]["focusturnp2"],
					"guardp1": fight[1]["guardp1"],
					"guardp2": 1
				}
				fightdict[fight[0]]=new
				newhp=str(new["p2hp"])
				await msg.channel.send(f"you dealt {randomdmg} damage")	
				if 0>=new["p2hp"]:
					await msg.channel.send(f"{msg.author.mention} you win!!! \ncongratulations you get nothing")
					del fightdict[fight[0]]
				else:
					await msg.channel.send(f"theyre now at {newhp} hp")
					await msg.channel.send(f"<@{str(p2id)}> youre next")
			elif(p1==False and fight[1]["turn"]==False):
				randomdmg=round(random.randint(15, 20)*fight[1]["guardp1"])
				if fight[1]["focusturnp2"]==fight[1]["turncounter"]:
					randomdmg=round(randomdmg*2)
				new = {
					"p1hp" : fight[1]["p1hp"]-randomdmg,
					"p2hp" : fight[1]["p2hp"],
					"turn" : True,
					"turncounter": fight[1]["turncounter"]+1,
					"focusturnp1": fight[1]["focusturnp1"],
					"focusturnp2": fight[1]["focusturnp2"],
					"guardp1": 1,
					"guardp2": fight[1]["guardp2"]
				}
				fightdict[fight[0]]=new
				newhp=str(new["p1hp"])
				await msg.channel.send(f"you dealt {randomdmg} damage")	
				if 0>=new["p1hp"]:
					await msg.channel.send(f"{msg.author.mention} you win!!! \ncongratulations you get nothing")
					del fightdict[fight[0]]
				else:
					await msg.channel.send(f"theyre now at {newhp} hp")
					await msg.channel.send(f"<@{str(p1id)}> youre next")
		elif(msg.content.lower() in att2names):
			hitchance=random.randint(1,100)
			if fight[1]["focusturnp1"]==fight[1]["turncounter"] and p1 == True:
				hitchance=random.randint(0,75)
			elif fight[1]["focusturnp2"]==fight[1]["turncounter"] and p1 == False:
				hitchance=random.randint(0,75)
			hit=None
			if hitchance>50:
				hit=True
			else:
				hit=False
			if hit:
				if(p1==True and fight[1]["turn"]==True):
					randomdmg=round(random.randint(35, 40)*fight[1]["guardp2"])
					if fight[1]["focusturnp1"]==fight[1]["turncounter"]:
						randomdmg=round(randomdmg*1.75)
					new = {
						"p1hp" : fight[1]["p1hp"],
						"p2hp" : fight[1]["p2hp"]-randomdmg,
						"turn" : False,
						"turncounter": fight[1]["turncounter"]+1,
						"focusturnp1": fight[1]["focusturnp1"],
						"focusturnp2": fight[1]["focusturnp2"],
						"guardp1": fight[1]["guardp1"],
						"guardp2": 1
					}
					fightdict[fight[0]]=new
					newhp=str(new["p2hp"])
					await msg.channel.send(f"you dealt {randomdmg} damage")	
					if 0>=new["p2hp"]:
						await msg.channel.send(f"{msg.author.mention} you win!!! \ncongratulations you get nothing")
						del fightdict[fight[0]]
					else:
						await msg.channel.send(f"theyre now at {newhp} hp")
						await msg.channel.send(f"<@{str(p2id)}> youre next")
				elif(p1==False and fight[1]["turn"]==False):
					randomdmg=round(random.randint(35, 40)*fight[1]["guardp1"])
					if fight[1]["focusturnp2"]==fight[1]["turncounter"]:
						randomdmg=round(randomdmg*1.75)
					new = {
						"p1hp" : fight[1]["p1hp"]-randomdmg,
						"p2hp" : fight[1]["p2hp"],
						"turn" : True,
						"turncounter": fight[1]["turncounter"]+1,
						"focusturnp1": fight[1]["focusturnp1"],
						"focusturnp2": fight[1]["focusturnp2"],
						"guardp1": 1,
						"guardp2": fight[1]["guardp2"]
					}
					fightdict[fight[0]]=new
					newhp=str(new["p1hp"])
					await msg.channel.send(f"you dealt {randomdmg} damage")	
					if 0>=new["p1hp"]:
						await msg.channel.send(f"{msg.author.mention} you win!!! \ncongratulations you get nothing")
						del fightdict[fight[0]]
					else:
						await msg.channel.send(f"theyre now at {newhp} hp")
						await msg.channel.send(f"<@{str(p1id)}> youre next")
			else:
				if(p1==True and fight[1]["turn"]==True):
					new = {
						"p1hp" : fight[1]["p1hp"],
						"p2hp" : fight[1]["p2hp"],
						"turn" : False,
						"turncounter": fight[1]["turncounter"]+1,
						"focusturnp1": fight[1]["focusturnp1"],
						"focusturnp2": fight[1]["focusturnp2"],
						"guardp1": fight[1]["guardp1"],
						"guardp2": fight[1]["guardp2"]
					}
					fightdict[fight[0]]=new
					b=str(fight[1]["p2hp"])
					await msg.channel.send("you missed the move!")	
					await msg.channel.send(f"theyre still at {b} hp")
					await msg.channel.send(f"<@{str(p2id)}> youre next")
				elif(p1==False and fight[1]["turn"]==False):
					new = {
						"p1hp" : fight[1]["p1hp"],
						"p2hp" : fight[1]["p2hp"],
						"turn" : True,
						"turncounter": fight[1]["turncounter"]+1,
						"focusturnp1": fight[1]["focusturnp1"],
						"focusturnp2": fight[1]["focusturnp2"],
						"guardp1": fight[1]["guardp1"],
						"guardp2": fight[1]["guardp2"]
					}
					fightdict[fight[0]]=new
					b=str(fight[1]["p1hp"])
					await msg.channel.send("you missed the move!")	
					await msg.channel.send(f"theyre still at {b} hp")
					await msg.channel.send(f"<@{str(p1id)}> youre next")
		elif(msg.content.lower() == "focus"):
			if(p1):
				new = {
				"p1hp" : fight[1]["p1hp"],
				"p2hp" : fight[1]["p2hp"],
				"turn" : False,
				"turncounter": fight[1]["turncounter"]+1,
				"focusturnp1": fight[1]["turncounter"]+2,
				"focusturnp2": fight[1]["focusturnp2"],
				"guardp1": fight[1]["guardp1"],
				"guardp2": fight[1]["guardp2"]
				}
				fightdict[fight[0]]=new
				b=str(fight[1]["p1hp"])
				await msg.channel.send("you have activated focus")	
				await msg.channel.send(f"theyre still at {b} hp")
				await msg.channel.send(f"<@{str(p2id)}> youre next")
			else:
				new = {
				"p1hp" : fight[1]["p1hp"],
				"p2hp" : fight[1]["p2hp"],
				"turn" : True,
				"turncounter": fight[1]["turncounter"]+1,
				"focusturnp1": fight[1]["focusturnp1"],
				"focusturnp2": fight[1]["turncounter"]+2,
				"guardp1": fight[1]["guardp1"],
				"guardp2": fight[1]["guardp2"]
				}
				fightdict[fight[0]]=new
				b=str(fight[1]["p1hp"])
				await msg.channel.send("you have activated focus")	
				await msg.channel.send(f"theyre still at {b} hp")
				await msg.channel.send(f"<@{str(p1id)}> youre next")
		elif(msg.content.lower() == "guard"):
			if(p1):
				g=None
				if(not fight[1]["guardp1"]==1):
					g=True
				else:
					g=False
				new = {
				"p1hp" : fight[1]["p1hp"],
				"p2hp" : fight[1]["p2hp"],
				"turn" : False,
				"turncounter": fight[1]["turncounter"]+1,
				"focusturnp1": fight[1]["turncounter"],
				"focusturnp2": fight[1]["focusturnp2"],
				"guardp1": round(random.uniform(0.25, 0.4), 2),
				"guardp2": fight[1]["guardp2"]
				}
				fightdict[fight[0]]=new
				b=new["guardp1"]
				gp=100-int(float(100)*float(b))
				if g == False:
					await msg.channel.send("you have activated guard")
					await msg.channel.send(f"your guard is {str(gp)}%")
				else:
					await msg.channel.send("your guard was already activated")
					await msg.channel.send(f"your new guard is {gp}%")
				await msg.channel.send(f"<@{str(p2id)}> youre next")
			else:
				g=None
				if(not fight[1]["guardp2"]==1):
					g=True
				else:
					g=False
				new = {
				"p1hp" : fight[1]["p1hp"],
				"p2hp" : fight[1]["p2hp"],
				"turn" : True,
				"turncounter": fight[1]["turncounter"]+1,
				"focusturnp1": fight[1]["focusturnp1"],
				"focusturnp2": fight[1]["turncounter"],
				"guardp1": fight[1]["guardp1"],
				"guardp2": round(random.uniform(0.25, 0.4), 2)
				}
				fightdict[fight[0]]=new
				b=new["guardp2"]
				gp=100-int(float(100)*float(b))
				if g == False:
					await msg.channel.send("you have activated guard")
					await msg.channel.send(f"your guard is {str(gp)}%")
				else:
					await msg.channel.send("your guard was already activated")
					await msg.channel.send(f"your new guard is {gp}%")
				await msg.channel.send(f"<@{str(p1id)}> youre next")
		elif(msg.content.lower() == "stats"):
			send=f"(focus and turn are maybe confusing but use .fighthelp to know what they means)\nPlayer 1 (p1): <@{str(p1id)}>\nPlayer 2 (p2): <@{str(p2id)}>\n"
			for a, b in fight[1].items():
				if(a=="guardp1" or a=="guardp2"):
					b=str(round(100-(100*b)))+"%"
				send+=a+": "+str(b)+"\n"
			await msg.channel.send(send)
		elif(msg.content.lower() == "end" and not p1 == None):
			await msg.channel.send(f"{msg.author.mention} gave up due to the extreme swag of their opponent")
			del fightdict[fight[0]]
	await bot.process_commands(msg)

@bot.command()
async def fight(ctx, obama : discord.Member):
	a1=0
	a2=0
	for fn in fightdict:
		if(str(ctx.author.id) in fn and str(obama.id) in fn):
			a1+=1
			a2+=1
		if(str(ctx.author.id) in fn):
			a1+=1
		if(str(obama.id) in fn):
			a2+=1
	if(obama.id==741811813615927307):
		#funny scenario trying to fight the bot
		await ctx.send("ok i win you lose")
	elif(obama.bot):
		#trying to fight a bot
		await ctx.send(f"{obama.mention} is a bot and im pretty sure you cant fight robots they would instantly win")
	elif(obama.id==ctx.author.id):
		#trying to fight self
		await ctx.send(f"{obama.mention} what you cant fight yourself dumb")
	elif(a1>=1 and a2>=1):
		#the command user and the other person are already fighting
		await ctx.send(f"{ctx.author.mention} youre already fighting that person")
	elif(a1>=1):
		#the command user is already fighting
		await ctx.send(f"{ctx.author.mention} stop thinking youre so good you cant fight two people at once")
	elif(a2>=1):
		#the other person is already fighting
		await ctx.send(f"{ctx.author.mention} why are you trying to fight {obama.mention} theyre already doing it with someone else")
	else:
		#actual fight

		# await ctx.send("clas???????")
		# classselection=0

		# classdict={
		# "scout": 1,
		# "soldier": 2,
		# "pyro": 3,
		# "demoman": 4,
		# "heavy": 5,
		# "engineer": 6,
		# "medic": 7,
		# "sniper": 8,
		# "spy": 9,
		# "random": 10
		# }
		# selec=classdict[classselection]

		turn=None

		a=random.randint(1, 100)
		if(a>=50):
			turn=True
		else:
			turn=False
		
		add = {
		"p1hp": 150,
		"p2hp": 150,
		"turn": turn,
		"turncounter": 0,
		"focusturnp1": 999999999999999999999999,
		"focusturnp2": 999999999999999999999999,
		"guardp1": 1,
		"guardp2": 1,
		"classp1": None,
		"classp2": None
		}
		fightdict[f"/{str(ctx.author.id)}/{str(obama.id)}/"]=add
		if turn==True:
			await ctx.send(f"welcome to fight command scuffed edition!!!\n{ctx.author.mention} you are the starter\n use the .fighthelp command in case you dont know what to do")
		else:
			await ctx.send(f"welcome to fight command scuffed edition!!!\n{obama.mention} you are the starter\n use the .fighthelp command in case you dont know what to do")

@bot.command()
async def printfd(ctx):
	await ctx.send(str(fightdict))
@bot.command()
async def clearfd(ctx):
	for key in fightdict.keys():
  	  del fightdict[key]
	await ctx.send("ok")

@bot.event
async def on_ready():
	print('my body is ready \n')
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you're mom"))
	
keep_alive()
token = os.environ.get("TOKEN")
bot.run(token)

"""
dumb bot made by @walmart#6969, to run it yourself, check the README

GITHUB: https://github.com/Ya1Boi/poggersbot (i just realized this is kind of useless because if youre seeing this youre probably already on the github)
"""

"""
send help
"""