import json

def init_config(file):
    with open(f"{file}", "r") as config:
        return json.load(config)
    
config = init_config("config/config.json")
  