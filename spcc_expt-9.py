#NAME- Chirag Mithilesh Varma
#Division - TE4
#Roll No- 58
#Batch - D
#Subject - System Programming and compiler constructionimport re
import re
# Evaluate constant expressions at compile-time
def eval_const_expr(expr):
    try:
        return str(eval(expr))
    except:
        return expr

# Remove dead code by detecting and removing unreachable statements
def remove_dead_code(code):
    labels = set(re.findall(r'^\w+:', code, flags=re.M))
    jumps = set(re.findall(r'\bJ\w+', code))
    used_labels = set()
    for jump in jumps:
        used_labels.add(jump)
    for label in labels:
        if label[:-1] not in used_labels:
            code = re.sub(r'^' + label + '.*$', '', code, flags=re.M)
    return code

# Main program
def main():
    input_code = '''
    MOV AX, 5
    MOV BX, 7
    ADD AX, BX
    MOV CX, 10
    MUL CX
    SUB AX, 5
    JZ L1
    MOV DX, 1
    JMP L2
    L1: MOV DX, 0
    L2: INT 21h
    '''

    # Step 1: Evaluate constant expressions
    input_code = re.sub(r'(?<![a-zA-Z0-9])(\d+ [\+\-\*\/] \d+)(?![a-zA-Z0-9])', lambda m: eval_const_expr(m.group(1)), input_code)

    # Step 2: Remove dead code
    input_code = remove_dead_code(input_code)

    print(input_code)

if __name__ == '__main__':
    main()