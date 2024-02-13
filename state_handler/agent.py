import time

from state_handler.state import StateMachine, State
import j2l.pytactx.agent as pytactx_agent

cpi = 0


class AgentState(State):
    def __init__(self, agent: pytactx_agent.Agent, fsm):
        super().__init__(fsm)
        self._agent = agent

    def fire(self, enable: bool = True, firepath: any = None):
        return self._agent.fire(enable, firepath)

    def move_to(self, x: int, y: int):
        self._agent.moveTowards(x, y)

    def get_distance(self):
        return self._agent.distance

    def get_color(self):
        return self._agent.color

    def set_color(self, r: int, g: int, b: int):
        self._agent.setColor(r, g, b)

    def do_action(self):
        pass


class SpecialAgent(pytactx_agent.Agent):
    def __init__(self, agent_args: dict, zones_to_monitor: list[tuple]):
        super().__init__(*agent_args.values())
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


class ScanState(AgentState):
    def __init__(self,
                 fsm: StateMachine,
                 player_instance: SpecialAgent,
                 zones: list[tuple]):
        super().__init__(player_instance, fsm)
        self.__zones = zones

    def do_action(self):
        self.scan()

    def scan(self):
        global cpi
        print("Scanning")
        self.fire(False)
        self.set_color(0, 255, 56)
        if self._agent.x == self.__zones[cpi][0] and self._agent.y == self.__zones[cpi][1]:
            cpi = (cpi + 1) % len(self.__zones)

        self.move_to(self.__zones[cpi][0], self.__zones[cpi][1])


class AttackState(AgentState):
    def __init__(self, agent: SpecialAgent, fsm: StateMachine):
        super().__init__(agent, fsm)
        self.__agent = agent

    def do_action(self):
        self.attack()

    def attack(self):
        print("Attacking")
        self.__agent.fire(True)
        self.set_color(255, 0, 0)
