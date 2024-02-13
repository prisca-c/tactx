import j2l.pytactx.agent as pytactx
import event
from dotenv import load_dotenv, dotenv_values

from state_handler.agent import SpecialAgent

load_dotenv()

config = dotenv_values(".env")
print(config)

PLAYER_ID = config.get("PLAYER_ID")
ARENA = config.get("ARENA")
USERNAME = config.get("USERNAME")
PASSWORD = config.get("PASSWORD")
SERVER = config.get("SERVER")
zones_to_monitor = [(5, 10), (2, 2),(10, 5), (2, 18), (18, 2), (18, 18)]

agent_first = {
    "playerId": PLAYER_ID,
    "arena": ARENA,
    "username": USERNAME,
    "password": PASSWORD,
    "server": SERVER
}

agent = SpecialAgent(agent_first, zones_to_monitor)

while True:
    agent.on_update()
