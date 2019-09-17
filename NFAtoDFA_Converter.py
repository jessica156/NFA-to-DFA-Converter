from typing import NamedTuple

# A Data Structure that holds information about finite automatas
class Finite_Automata(NamedTuple):
    list_of_states: list
    variables: list
    start_state: int
    final_states: list
    transitions: list
    final_dfa_states: list

# A class that converts files to NFA and NFA to DFA
class automata_conversion:

    # Prints out the final DFA to a text file
    def print_dfa(self, dfa):
        fileOutput = open("dfa.txt", 'w')
        fileOutput.write("Number of States: " + str(len(dfa.final_dfa_states)) + "\r\n")
        fileOutput.write("Variables: " + " ".join(dfa.variables) + "\r\n")
        fileOutput.write("Start State: " + str(dfa.start_state) + "\r\n")
        fileOutput.write("Final States: " + " ".join(str(state) for state in dfa.final_states) + "\r\n")
        fileOutput.write("DFA Transitions:" + "\r\n")
        for transition in sorted(dfa.transitions):
            fileOutput.write(" ".join(str(trans) for trans in transition) + "\r\n")

    # Reads in the input file and converts it into a NFA
    def file_to_NFA(self, lines):
        states = list(range(int(lines[0])))
        vars = list(lines[1].strip())
        transitions = []
        for index in range(4, len(lines)):
            current_transition = lines[index].split(" ")
            transition_function = (int(current_transition[0]), current_transition[1], int(current_transition[2]))
            transitions.append(transition_function)

        nfa_input = Finite_Automata(states, vars, int(lines[2]), lines[3].split(), transitions, [])
        return nfa_input

    # Converts the NFA to a DFA
    def NFA_to_DFA(self, automata):
        automata.final_dfa_states.append((0,))
        combined_nfa_transitions = {}
        transition_map = {}

        # Combine NFA states that have the same current state and variable transition
        for current_transition in automata.transitions:
            current_state = current_transition[0]
            variable = current_transition[1]
            state_input = (current_state, variable)
            next_state = current_transition[2]

            # Add unique combinations to the list
            if state_input in combined_nfa_transitions:
                combined_nfa_transitions[state_input].append(next_state)
            else:
                combined_nfa_transitions[state_input] = [next_state]


        # Convert NFA transitions to DFA transitions
        for dfa_state in automata.final_dfa_states:
            for var in automata.variables:
                # Find the next states for the initial start state (usually state q0)
                if len(dfa_state) == 1 and (dfa_state[0], var) in combined_nfa_transitions:
                    transition_map[(dfa_state, var)] = combined_nfa_transitions[(dfa_state[0], var)]
                    if tuple(transition_map[(dfa_state, var)]) not in automata.final_dfa_states:
                        automata.final_dfa_states.append(tuple(transition_map[(dfa_state, var)]))

                # Find the next states for every other DFA states (including combined states such as q0q1)
                else:
                    next_states = []
                    for nfa_state in dfa_state:
                        if (nfa_state, var) in combined_nfa_transitions and combined_nfa_transitions[
                            (nfa_state, var)] not in next_states:
                                value = list(combined_nfa_transitions[(nfa_state, var)])
                                if value not in next_states:
                                    next_states += value

                    transition_map[(dfa_state, var)] = next_states

                    if tuple(next_states) not in automata.final_dfa_states:
                        automata.final_dfa_states.append(tuple(next_states))

        # Update NFA transitions to DFA transitions
        new_transitions = []
        for delta in transition_map:
            new_transitions.append((list(delta[0]), delta[1], transition_map[delta]))

        # Return the new DFA
        dfa_automata = Finite_Automata(automata.list_of_states, automata.variables, automata.start_state,
                                       automata.final_states, new_transitions, automata.final_dfa_states)

        return dfa_automata