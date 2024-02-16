# This example requires the 'message_content' privileged intent to funct
import discord
from PIL import Image, ImageDraw, ImageFont
import io

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!emoji'):
        emoji = message.content.split(' ')[-1]
        font = ImageFont.truetype('Alkatra-Medium.ttf', 128)
        image = Image.new('RGBA', (512, 512), (255, 255, 255, 0))
        draw = ImageDraw.Draw(image)
        draw.text((128, 128), emoji, font=font, fill=(0, 0, 0, 255))

        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        buffered.seek(0)

        sticker = await message.guild.create_sticker(name=f"{emoji}_sticker", description=f"Custom sticker of {emoji}", file=buffered, emoji=emoji)
        await message.channel.send(f"Created sticker: {sticker.name}")

bot.run("MTE2ODAyMDY0MTkxMjQ3NTY5OA.GgTWoN.1rZJs6tF9VkmUwARzKGbT0u_ou5Cb_p9HSPf08")

        


