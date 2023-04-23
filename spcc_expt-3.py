

sym_table = {} 
counter = 0

with open("input.asm", "r") as file:
    for line in file:
        line = line.strip()
        tokens = line.split()

        if len(tokens) == 3 and tokens[1] == "DC":
            sym_table[tokens[0]] = counter
            counter += 1
        elif len(tokens) == 2:
            sym_table[tokens[0]] = counter
            counter += 1
        else:
            counter += 1


print("Symbol Table")
print("------------")
for symbol, location in sym_table.items():
    print(f"{symbol} : {location}")
print("------------")
print(f"LOCATION COUNTER: {counter}")
