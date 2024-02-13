from state_handler.special_agent import SpecialAgent

zones_to_monitor = [(5, 10), (2, 2), (10, 5), (2, 18), (18, 2), (18, 18)]

agent_1 = SpecialAgent('agent_1', zones_to_monitor)

while True:
    agent_1.on_update()
