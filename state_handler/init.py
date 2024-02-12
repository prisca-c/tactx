import j2l.pytactx.agent as pytactx_agent
from state_handler.agent import SpecialAgentState


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

class AgentHandler:
    def __init__(self, agent: pytactx_agent.Agent, zones_to_monitor: list[tuple]):
        while True:
            SpecialAgentState(agent, zones_to_monitor)
