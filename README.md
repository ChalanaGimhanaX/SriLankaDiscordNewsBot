# 📰 Discord News Bot 📢

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Discord](https://img.shields.io/badge/Discord-Bot-blue.svg)](https://discord.com)
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

## 📋 Description

This **Discord News Bot** allows users to fetch the latest news articles in their preferred language from Hiru News. Users can choose between **English**, **Sinhala**, and **Tamil** to receive news updates directly in their Discord channel.

The bot scrapes the news content using **BeautifulSoup** and displays it in an organized format within the Discord chat.

---

## 🎯 Features

- Fetch the latest news in **English**, **Sinhala**, or **Tamil**.
- Scrapes news articles from Hiru News website.
- Sends news articles along with images directly to Discord channels.
- Supports pagination to retrieve multiple articles at once.

---

## 🛠️ Requirements

- **Python 3.9+**
- **discord.py** for Discord bot functionality
- **beautifulsoup4** for web scraping
- **requests** for making HTTP requests
- **python-dotenv** for managing environment variables

Install required libraries via:
```bash
pip install discord.py beautifulsoup4 requests python-dotenv
```

---

## 📁 Project Structure

```
discord-news-bot/
│
├── main.py                 # Main bot script
├── .env                    # Environment variables (for bot token)
├── requirements.txt        # Dependencies
└── README.md               # Documentation (this file)
```

---

## ⚙️ Setup & Configuration

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ChalanaGimhanaX/SriLankaDiscordNewsBot.git
   cd SriLankaDiscordNewsBot
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` File:**

   In the root directory, create a `.env` file with the following content:

   ```
   DISCORDTOKEN=your_discord_bot_token_here
   ```

4. **Run the Bot:**
   ```bash
   python main.py
   ```

---

## 📌 Usage

Once the bot is running, you can use the `/news` command in Discord to fetch the latest news. The command supports three language options:

- **English**
- **Sinhala**
- **Tamil**

The bot will return the latest news articles in the selected language.

---

## 🛡️ License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more details.
