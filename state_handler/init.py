from state_handler.agent import ScanState, AttackState
from state_handler.state import StateMachine
from agent import AgentState, SpecialAgentState


# def main():
#     fsm = StateMachine()
#     attack = AttackState(fsm)
#     scan = ScanState(fsm)
#     fsm.set_state(attack)
#     print(str(fsm.current_state == attack))
#     fsm.set_state(scan)
#     print(str(fsm.current_state == scan))
#     print("All tests passed.")
#
#
# main()

class Handler:
    def __init__(self, agent: SpecialAgentState):
        self.__agent = agent
        self.__fsm = StateMachine()
        self.__attack = AttackState(self.__fsm)
        self.__scan = ScanState(self.__fsm)
        self.__fsm.set_state(self.__scan)

    def on_update(self):
        self.__fsm.do_action()
        self.__agent.update()
