class IState:
    def do_action(self, *args, **kwargs):
        pass

    def __str__(self):
        return self.__class__.__name__


class StateMachine:
    def __init__(self, initial_state: IState = None):
        self.__current_state: IState = initial_state

    @property
    def current_state(self):
        return self.__current_state

    def set_state(self, state: IState):
        print(f"Changing state from {self.__current_state} to {state}")
        self.__current_state = state

    def do_action(self, *args, **kwargs):
        if self.__current_state is not None:
            print(f"Doing action for {self.__current_state}")
            return self.__current_state.do_action()


class State(IState):
    def __init__(self, parent_fsm: StateMachine):
        self._state_machine = parent_fsm

    def do_action(self):
        pass
