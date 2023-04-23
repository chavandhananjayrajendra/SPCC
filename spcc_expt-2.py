import re

# Define the regular expressions for each token
tokens = [
    (r'int', 'INT'),
    (r'float', 'FLOAT'),
    (r'char', 'CHAR'),
    (r'if', 'IF'),
    (r'else', 'ELSE'),
    (r'while', 'WHILE'),
    (r'do', 'DO'),
    (r'for', 'FOR'),
    (r'[0-9]+', 'NUM'),
    (r'"[^"]*"', 'STRING'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULT'),
    (r'/', 'DIV'),
    (r'=', 'EQUALS'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r';', 'SEMICOLON'),
    (r',', 'COMMA'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),
]

# Define the main program
if __name__ == "__main__":
    # Read the input program from a file
    with open("input_program.txt", "r") as f:
        program = f.read()

    # Initialize the token list
    token_list = []

    # Tokenize the input program
    pos = 0
    while pos < len(program):
        match = None
        for token in tokens:
            pattern, token_type = token
            regex = re.compile(pattern)
            match = regex.match(program, pos)
            if match:
                text = match.group(0)
                token_list.append((text, token_type))
                break
        if not match:
            print(f"Error: unexpected character at position {pos}")
            break
        else:
            pos = match.end(0)

    # Print the token list
    for token in token_list:
        text, token_type = token
        print(f"{token_type}: {text}")