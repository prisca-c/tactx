import time

from state_handler.state import StateMachine, IState
import j2l.pytactx.agent as pytactx_agent


class AgentState:
    def __init__(self, _agent: pytactx_agent.Agent):
        super().__init__()
        self._agent = _agent

    def fire(self, enable: bool = True, firepath: any = None):
        return self._agent.fire(enable, firepath)

    def move_to(self, x: int, y: int):
        while not (self._agent.x == x and self._agent.y == y):
            self._agent.moveTowards(x, y)
            self._agent.update()

    def on_update(self):
        self._agent.update()

    def get_distance(self):
        return self._agent.distance

    def get_color(self):
        return self._agent.color

    def set_color(self, r: int, g: int, b: int):
        self._agent.setColor(r, g, b)


class SpecialAgentState:
    def __init__(self, player_instance: pytactx_agent, zones_to_monitor: list[tuple]):
        self._agent = AgentState(player_instance)
        self.__fsm = StateMachine(None)
        self.__zones = zones_to_monitor
        while True:
            if self._agent.get_distance() == 0:
                print("Zone Monitoring")
                self._zone_monitoring()
            else:
                print("Attacking")
                self._attack()

    def _zone_monitoring(self) -> None:
        scan_state = ScanState(self._agent, self.__zones)
        self.__fsm.set_state(scan_state)
        scan_state.do_action()

    def _attack(self):
        attack_state = AttackState(self._agent)
        self.__fsm.set_state(attack_state)
        attack_state.do_action()


class ScanState(IState):
    def __init__(self,
                 player_instance: AgentState,
                 zones: list[tuple]):
        super().__init__()
        self.__agent: AgentState = player_instance
        self.__zones = zones

    def do_action(self):
        self.scan()

    def scan(self):
        self.__agent.fire(False)
        self.__agent.set_color(0, 255, 0)
        self.__agent.on_update()
        for i in range(len(self.__zones)):
            self.__agent.move_to(self.__zones[i][0], self.__zones[i][1])
            self.__agent.on_update()
            time.sleep(0.3)


class AttackState(IState):
    def __init__(self, player_instance: AgentState):
        super().__init__()
        self.__agent = player_instance

    def do_action(self):
        self.attack()

    def attack(self):
        self.__agent.fire(True)
        self.__agent.set_color(255, 0, 0)
        self.__agent.on_update()
