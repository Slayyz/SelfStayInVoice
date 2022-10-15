import yaml

with open("config.yaml", 'r') as f:
    cfg = yaml.safe_load(f)

with open("token.txt", "r") as f:
    with open("config.yaml", "w") as yml:
        for line in f:
            if "#" in line:
                continue
            data = line.split()
            if type(cfg) is not dict:
                cfg = {}
            if 'tokens' in cfg:
                cfg['tokens'].append({ 'token': data[0] })
                print("ajout")
            else:
                cfg['tokens'] = []
                cfg['tokens'].append({ 'token': data[0] })
                print("ajout")
        # print(cfg)
        yaml.dump(cfg, yml, sort_keys=False)

f = open('token.txt', 'r+')
f.truncate(0)

class Token_config:
    token = None
    guild_id = None
    channel_id = None
    self_mute = None
    self_deaf = None

def get_default():
    config = Token_config()
    config.guild_id = cfg['default']['guild_id']
    config.channel_id = cfg['default']['channel_id']
    config.self_mute = cfg['default']['self_mute']
    config.self_deaf = cfg['default']['self_deaf']
    return config

def get_tokens():
    tokens = []
    for token in cfg['tokens']:
        config = get_default()
        config.token = token['token']
        if 'guild_id' in token:
            config.guild_id = token['guild_id']
        if 'channel_id' in token:
            config.channel_id = token['channel_id']
        if 'self_mute' in token:
            config.self_mute = token['self_mute']
        if 'self_deaf' in token:
            config.self_deaf = token['self_deaf']
        tokens.append(config)
    return tokens