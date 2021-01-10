# Auto-Reply Discord Bot 

## Intall

### Basic Usage
simply invite the bot to your server using this link
[Invitation link](https://discord.com/api/oauth2/authorize?client_id=792374375722123284&permissions=6144&scope=bot)

### Development
Feel free to clone this repo and play with it as you want!
first you need to create a virtual environment then run 

```bash
 pip install -r requirments.txt

```

then, you just need to rename `.env.sample` file to `.env` and get your own **app_token** from the Discord Dev website 

## Usage
This bot has a few commands at the moment:

- $wiki {keyword} : search wikipedia with keyword and return an embed with the search result
- $get joke : gets a joke that has more up votes that downvotes. It gets the jokes from 'joke3' api
- $get dad joke : gets a dad joke from 'icanhazdadjoke' api
- $get quote : gets quote from 'quotable' api 

There's also a feature to automatically mention ofline members, when you mention any of the user's nicknames in a message, you can do this by calling  `mention_user` function  on  `on_message` function

Also there's a sentiment analysis fearutre, that analyze a sentiment and returns the sentiment of it 

## Future Work
- add a dictionary for all guild members, and initalize every member entry with the name, so it can be used to auto mention any member in the guild if their name was contained in a message 

- utilize the sentiment analysis feature 