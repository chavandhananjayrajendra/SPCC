#NAME- Chirag Mithilesh Varma
#Division - TE4
#Roll No- 58
#Batch - D
#Subject - System Programming and compiler construction
# Define the grammar as a dictionary of production rules
grammar = {
    'S': ['A B', 'C D'],
    'A': ['a', 'B c'],
    'B': ['b', 'epsilon'],
    'C': ['c', 'A D'],
    'D': ['d', 'epsilon']
}

# Define a function to calculate the FOLLOW() set for a given nonterminal
def follow(nonterminal, grammar):
    follow_set = set()
    if nonterminal == 'S':
        follow_set.add('$')
    for symbol in grammar:
        for production in grammar[symbol]:
            if nonterminal in production:
                index = production.index(nonterminal)
                if index == len(production) - 1:
                    if symbol != nonterminal:
                        follow_set |= follow(symbol, grammar)
                else:
                    next_symbol = production[index + 1]
                    if next_symbol.isupper():
                        follow_set |= first(next_symbol, grammar)
                        if 'epsilon' in grammar[next_symbol]:
                            follow_set |= follow(symbol, grammar)
                    else:
                        follow_set.add(next_symbol)
    return follow_set

# Define a function to calculate the FIRST() set for a given symbol
def first(symbol, grammar):
    first_set = set()
    if symbol.islower() or symbol == 'epsilon':
        first_set.add(symbol)
    else:
        for production in grammar[symbol]:
            for symbol_prime in production.split():
                first_set |= first(symbol_prime, grammar)
                if 'epsilon' not in first_set:
                    break
            else:
                first_set.add('epsilon')
    return first_set

# Test the functions with the example grammar
print(f"Follow of S: {follow('S', grammar)}")
print(f"Follow of A: {follow('A', grammar)}")
print(f"Follow of B: {follow('B', grammar)}")
print(f"Follow of C: {follow('C', grammar)}")
print(f"Follow of D: {follow('D', grammar)}")