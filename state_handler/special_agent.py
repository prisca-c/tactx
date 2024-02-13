from j2l.pytactx import agent as pytactx_agent
from state_handler.agent_state import ScanState, AttackState
from state_handler.state import StateMachine

import env

ARENA = env.ARENA
USERNAME = env.USERNAME
PASSWORD = env.PASSWORD
SERVER = env.SERVER

config_args = {
    "arena": ARENA,
    "username": USERNAME,
    "password": PASSWORD,
    "server": SERVER
}


class SpecialAgent(pytactx_agent.Agent):
    """
    SpecialAgent class that inherits from the Agent class from the pytactx module.
    """

    def __init__(self, player_id, zones_to_monitor: list[tuple]):
        global config_args
        args = {"player_id": player_id, **config_args}
        super().__init__(*args.values())
        self.__fsm = StateMachine(None)
        self.__zones = zones_to_monitor
        self.__fsm.set_state(ScanState(self.__fsm, self, self.__zones))

    def on_update(self):
        print("on_update")
        if self.__fsm.current_state is not None:
            if len(self.range) == 0:
                self.__fsm.set_state(ScanState(self.__fsm, self, self.__zones))
            else:
                self.__fsm.set_state(AttackState(self, self.__fsm))

        self.__fsm.do_action()
        self.update()
        return
