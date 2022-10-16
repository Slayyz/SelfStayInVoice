## Introduction
A Code written in **Python** that helps you to keep a lot of accounts 24/7 on discord voice channels.

## Installing
Python 3.8 or higher is required

To install the library :
```
# Linux/macOS
python3 -m pip install -U "discord.py-self[voice]"

# Windows
py -3 -m pip install -U discord.py-self[voice]
```

## Help
Put token(s) on the [token.txt](https://github.com/Slayyz/SelfStayInVoice/blob/main/token.txt)

Rename config.yaml.example to config.yaml

Put true or false for self_deaf and self_mute. If you want your tokens to be mute or defan.

Put game in game if you want to token play a game. Put None if you want to no play game.

We can do this for each token.

## Exemple
An exemple of a config.yaml
```
default:
  guild_id: 843826017273643028
  channel_id: 923694659459514449
  self_mute: true
  self_deaf: false
  game: VALORENT
tokens:
- tokens: ODUzMzE4MDc3OTI0MTE0NDgz.G-8Gh6.obh14rR8pybXgEiCnEeMkgOLfaBv9s6-Kq3QK0
  guild_id: 873885836138147851
  channel_id: 963131012613824616
  self_mute: false
  self_deaf: false
  game: Fortnite
```