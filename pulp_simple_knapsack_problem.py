from pulp import *

model = LpProblem("Cargo_Loading_Problem", LpMaximize)

# Decision Variables
x1 = LpVariable("A", 0, None, LpInteger)
x2 = LpVariable("B", 0, None, LpInteger)
x3 = LpVariable("C", 0, None, LpInteger)

# Objective Function
model += 12*x1 + 25*x2 + 38*x3

# Define storage capacity contraint
model += x1 + 2*x2 + 3*x3 <= 10

# Solve and print result
model.solve()
for v in model.variables():
    print(v.name, " = ", v.varValue)

print("Value of Objective Function = ", value(model.objective))
