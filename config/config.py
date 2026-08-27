import yaml
def load_config():
  with open("config/config.yaml", 'r',encoding="utf-8") as f:
    raw_config= yaml.safe_load(f)
    env=raw_config["env"]
    env_config=raw_config[env]
    return env_config

config = load_config()
print(config)
print(type(config))
base_url=config["base_url"]
httpbin_url=config["httpbin_url"]
timeout=config["timeout"]