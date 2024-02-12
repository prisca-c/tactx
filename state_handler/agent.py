from state_handler.state import StateMachine, State
import j2l.pytactx.agent as pytactx_agent


class AgentState:
    def __init__(self, _agent: pytactx_agent.Agent):
        super().__init__()
        self.__agent = _agent

    @property
    def agent(self):
        return self.__agent

    def _on_update(self):
        self.agent.update()


class SpecialAgentState(AgentState):
    def __init__(self, player_instance: pytactx_agent.Agent):
        super().__init__(player_instance)
        self.__fsm = StateMachine(None)
        self.__fsm.set_state(self)


class ScanState(State):
    def __init__(self, state_machine, player_instance: pytactx_agent.Agent):
        super().__init__(state_machine)
        self.__agent = player_instance

    def do_action(self):
        self.scan()

    def scan(self):
        self.__agent.fire(False)


class AttackState(State):
    def __init__(self, state_machine, player_instance: pytactx_agent.Agent):
        super().__init__(state_machine)
        self.__agent = player_instance

    def do_action(self):
        self.attack()

    def attack(self):
        self.__agent.fire(True)
