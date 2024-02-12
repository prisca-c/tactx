import j2l.pytactx.agent as pytactx
from getpass import getpass
import time
import event
from dotenv import load_dotenv, dotenv_values

from state_handler.agent import SpecialAgentState

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

cp = [(15, 10), (10, 15), (5, 10)]

state = 'monitor'


def moveTo(agentToMove: pytactx.Agent, x: int, y: int):
    while not (agentToMove.x == x and agentToMove.y == y):
        agentToMove.moveTowards(x, y)
        agentToMove.update()


def updateColor(agentToUpdate: pytactx.Agent):
    if state == 'monitor':
        agent.setColor(0, 255, 0)
    elif state == 'search':
        agentToUpdate.setColor(255, 90, 0)
    elif state == 'attack':
        agentToUpdate.setColor(255, 0, 0)
    agentToUpdate.update()


def checkpointMonitoring(agentToMove: pytactx.Agent):
    global state
    while state == 'monitor' and agentToMove.distance == 0:
        agentToMove.fire(False)
        for i in range(len(cp)):
            moveTo(agentToMove, cp[i][0], cp[i][1])
            time.sleep(0.3)

    state = 'search'


def searchForEnnemy(agentToMove: pytactx.Agent):
    global state
    while state == 'search':
        if agentToMove.distance == 0:
            state = 'monitor'
            break


def attack(agentToMove: pytactx.Agent):
    pass


# while True:
#
#     updateColor(agent)
#     if state == 'monitor':
#         checkpointMonitoring(agent)
#     elif state == 'search':
#         searchForEnnemy(agent)
#     elif state == 'attack':
#         attack(agent)
#     time.sleep(0.1)

SpecialAgentState(agent)
