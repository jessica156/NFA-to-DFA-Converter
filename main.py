from NFAtoDFA_Converter import automata_conversion

"""
NFA to DFA converter: This program reads in a NFA text file, convert the NFA to a DFA, and then print out the DFA to a 
text file called 'dfa.txt'
"""

print('Hello User!')
print('------------------------')
print('The NFA file has the following format:')
print('Line 1: A int N, which is the total number of NFA states')
print('Line 2: A string of all input variables')
print('Line 3: The starting state (usually 0)')
print('Line 4: A list of final states separated by spaces')
print('Remaining Lines: N lines of transitions in the form <current state> <variable> <next state>')
print('------------------------')

fileInput = input('Please enter the file name of the NFA file: ')

# Reads in the content of the NFA file
readFile = open(fileInput, 'r')
lines = readFile.readlines()
readFile.close()

nfa_automata = automata_conversion().file_to_NFA(lines)
dfa_automata = automata_conversion().NFA_to_DFA(nfa_automata)
automata_conversion().print_dfa(dfa_automata)

print('The converted DFA has been printed to a text file called: dfa.txt')
print('Thank you for using our NFA to DFA converter!')
print('Here is a cat on a bicycle!')
print(r"""
                 ________________
                |                |_____    __
                |  I Love You!   |     |__|  |_________
                |________________|     |::|  |        /
   /\**/\       |                \.____|::|__|      <
  ( o_o  )_     |                      \::/  \._______\
   (u--u   \_)  |
    (||___   )==\
  ,dP"/b/=( /P"/b\
  |8 || 8\=== || 8
  `b,  ,P  `b,  ,P
    ''''`    ''''`
""")
