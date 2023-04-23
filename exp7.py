

code = """
    MACRO
    ADD X,Y
    LDA X
    ADD Y
    STA Z
    MEND

    ADD A,B
    ADD C,D
"""

macro_name_table = {}
current_macro_name = None

for line in code.splitlines():
    tokens = line.split()
    if tokens:
        if tokens[0] == "MACRO" and len(tokens) > 1:
            macro_name = tokens[1]
            macro_name_table[macro_name] = {"start": len(macro_name_table)}
            current_macro_name = macro_name
        elif tokens[0] == "MEND":
            if current_macro_name:
                macro_name_table[current_macro_name]["end"] = len(macro_name_table) - 1
                current_macro_name = None

print("Macro Name Table:")
print("{:<10} {:<10} {:<10}".format("Macro Name", "Start", "End"))
for macro_name, macro_info in macro_name_table.items():
    start = macro_info["start"]
    end = macro_info["end"] if "end" in macro_info else ""
    print("{:<10} {:<10} {:<10}".format(macro_name, start, end))
