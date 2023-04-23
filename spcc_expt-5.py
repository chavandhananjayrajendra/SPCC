
class Production:
	def __init__(self, variable, prodRHS):
		self.variable = variable
		self.prodRHS = prodRHS
		self.first = []

	def computeFirst(self, productions):
		if len(self.first) == 0:
			for i in self.prodRHS:
				for j in i:
					if j.islower() or j == '$' or j == '+' or j == '*' or j == '-' or j =='/' or j == 'i' or j =='(' or j == ')':
						self.first.append(j)
						break
					else:
						firstOfVar = productions[j].computeFirst(productions)
						self.first = list(set(self.first) | set(firstOfVar))
						if '$' not in productions[j].first:
							break
		self.first.sort()
		return self.first


def accept():
	nOfProductions = int(input("Enter number of productions: "))
	productions = {}

	print("Enter productions separated by '|' and press Enter")
	print("Use '$' for Epsilon")
	for i in range(nOfProductions):
		variable, prod = input().replace(" ", "").split('->')
		prodRHS = prod.split('|')
		productions[variable] = Production(variable, prodRHS)

	return productions


productions = accept()
for key, value in productions.items():
	value.computeFirst(productions)
	print('\nFirst({}) = {{'.format(key), end="")
	print((' ').join(value.first), end='}')
