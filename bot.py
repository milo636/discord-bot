import os

import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


class DiscordBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("Comandos slash sincronizados.")


bot = DiscordBot()


@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")


@bot.tree.command(name="hola", description="Recibe un mensaje de bienvenida")
async def hola(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hola {interaction.user.mention}! Bienvenido/a al servidor."
    )


if not TOKEN:
    raise RuntimeError("Falta DISCORD_TOKEN en el archivo .env")

bot.run(TOKEN)
