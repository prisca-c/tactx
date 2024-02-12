import j2l.pytactx.agent as pytactx
import event
from dotenv import load_dotenv, dotenv_values

from state_handler.init import AgentHandler

load_dotenv()

config = dotenv_values(".env")
print(config)

PLAYER_ID = config.get("PLAYER_ID")
ARENA = config.get("ARENA")
USERNAME = config.get("USERNAME")
PASSWORD = config.get("PASSWORD")
SERVER = config.get("SERVER")

agent = pytactx.Agent(playerId=PLAYER_ID,
                      arena=ARENA,
                      username=USERNAME,
                      password=PASSWORD,
                      server=SERVER,
                      verbosity=2)
event.subscribe(agent)

zones_to_monitor = [(15, 10), (10, 15), (5, 10)]

AgentHandler(agent, zones_to_monitor)
