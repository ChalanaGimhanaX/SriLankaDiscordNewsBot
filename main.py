import os
import discord
from discord.ext import commands
from discord import app_commands
from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORDTOKEN')

englishNewsPageBaseUrl = 'https://www.hirunews.lk/english/local-news.php?pageID='
sinhalaNewsPageBaseUrl = 'https://www.hirunews.lk/local-news.php?pageID='
tamilNewsPageBaseUrl = 'https://www.hirunews.lk/tamil/local-news.php?pageID='

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

async def get_news(language):
    base_url = ''
    if language == 'English':
        base_url = englishNewsPageBaseUrl
    elif language == 'Sinhala':
        base_url = sinhalaNewsPageBaseUrl
    elif language == 'Tamil':
        base_url = tamilNewsPageBaseUrl

    news = []
    page_number = 1
    current_date = None
    request_next_page = True

    while request_next_page:
        url = f"{base_url}{page_number}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        news_elements = soup.select('.section > .trending-section > .row')
        if not news_elements:
            break

        for element in news_elements:
            title = element.find('img').get('alt')
            image = element.find('img').get('src')
            read_more = element.find('a').get('href')
            date_and_time = element.select_one('.middle-tittle-time').get_text(strip=True).replace('\n', '')

            if not current_date:
                current_date = date_and_time.split(',')[1].strip()

            if current_date in date_and_time:
                full_article = await get_full_article(read_more)
                news.append({
                    'title': title,
                    'image': image,
                    'read_more': read_more,
                    'date_and_time': date_and_time,
                    'content': full_article
                })
                request_next_page = True
            else:
                request_next_page = False

        page_number += 1

    return news

async def get_full_article(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    paragraphs = soup.select('.article-content p')
    content = "\n\n".join([p.get_text(strip=True) for p in paragraphs])
    return content

async def send_news(news, interaction):
    for n in news[::-1]:  # Reverse news to get the latest news at the end
        message = f"{n['image']}\n\n**{n['title']}**\n\n{n['content']}\n\n{n['date_and_time']}"
        await interaction.followup.send(message)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'We have logged in as {bot.user}')

@bot.tree.command(name="news", description="Get news in your preferred language")
@app_commands.choices(language=[
    app_commands.Choice(name="English", value="English"),
    app_commands.Choice(name="Sinhala", value="Sinhala"),
    app_commands.Choice(name="Tamil", value="Tamil"),
])
async def news(interaction: discord.Interaction, language: str):
    await interaction.response.defer()
    news = await get_news(language)
    await send_news(news, interaction)

bot.run(TOKEN)
