"""Module for main execution"""
import quintuples

for state, transitions in quintuples.transitionTable.items():
    print(f"State {quintuples.states[state]}:")
    for i, symbol in enumerate(transitions):
        if symbol:
            print(f"  - Input '{quintuples.alphabetList[i]}' goes to State {symbol}")


# Example usage:
def get_next_state(current_state, input_symbol):
    if current_state in quintuples.states and input_symbol in quintuples.alphabetList:
        symbol_index = quintuples.alphabetList.index(input_symbol)
        next_state = quintuples.transitionTable[quintuples.states.index(current_state)][symbol_index]
        # print(next_state)
        if next_state:
            for finalState in quintuples.finalStates:
                if next_state == finalState:
                    return "FINAL STATES"
            return next_state
    else:
        return None

def get_next_state_sequence(current_state, input_sequence):
    for input_symbol in input_sequence:
        # print(input_symbol)
        next_state = get_next_state(current_state, input_symbol)
        print(f"Current state: {current_state}, Input symbol: {input_symbol}, Next state: {next_state}")
        if not next_state:
           # return None  # Invalid transition
           print(None)
        current_state = next_state  # Update the current state

    return current_state

# Example usage:
current_state = quintuples.initialState
inputSequence = ["b", "m", "x", "w", "u"]  # Input
next_state = get_next_state_sequence(current_state, inputSequence)


if next_state:
    print(f"Current state: {current_state}, Input symbol: {inputSequence}, Next state: {next_state}")
else:
    print("State Stuck!")

# scenario lengkapi dengan output

# Final State Scenario:

# acdfhy
# acdehy
# acdfggy
# bxwu
# bxvs
# b m m m m m
# bmxwu
# bmmxwu
# bmmmxwu
# bmmmmxwu
# bmmmmmxwu