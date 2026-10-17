import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)



quiz = [
    {
        "Domanda 1: Quando si butta la spazzatura l'umido?",
        "opzioni" "A: Lunedì e Giovedì\nB: Martedì e Venerdì\nC: Mercoledì e Sabato",
        "corretta" "B",
    },
    {
        "Domanda 2: Cosa fai quando lasci una stanza?",
        "opzioni" "A: Lascio le luci accese\nB: Spengo le luci",
        "corretta" "B",
    }
]
@bot.command()
async def eco(ctx):
    await ctx.send(f'Hey,che ne dici di verificare se stai aiutando a inquinare di meno? Rispondi scrivendo A o B')

    
    punteggio = 0
    consigli = []
    
    
    def controlla_utente(messaggio):
        return messaggio.author == ctx.author and messaggio.channel == ctx.channel

    for dati in quiz:
      
        await ctx.send(f"\n**{dati['domanda']}**\n{dati['opzioni']}")
        
        
        risposta = await bot.wait_for('message', check=controlla_utente)
        
       
        scelta = risposta.content.upper()
        
        if scelta == dati["corretta"]:
            punteggio += 1
        else:
            consigli.append(dati["consiglio"])

    
    risultato = f"\nQuiz finito, {ctx.author.name}.\nPunteggio: {punteggio}/{len(quiz)}\n"
    
    if punteggio == len(quiz):
        risultato += "Ottimo lavoro. Non stai inquinando."
    else:
        risultato += "Ecco come puoi migliorare:\n"
        for c in consigli:
            risultato += f"- {c}\n"
            
    await ctx.send(risultato)

bot.run("")