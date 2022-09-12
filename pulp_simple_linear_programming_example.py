from pulp import *

model = LpProblem("Furniture_Profit", LpMaximize)

# Decision variables
f1 = LpVariable("tables", 0, None, LpInteger)
f2 = LpVariable("chairs", 0, None, LpInteger)
f3 = LpVariable("bookcases", 0, None, LpInteger)

# Define Objective function
model += 40*f1 + 30*f2 + 45*f3

# Create Contraints
model += 2*f1 + f2 + 2.5*f3 <= 60, "Labour"
model += 0.8*f1 + 0.6*f2 + 1.9*f3 <= 16, "Machine"
model += 30*f1 + 20*f2 + 30*f3 <= 400, "Wood"
model += f1 >= 10, "Tables"

model.solve()
for v in model.variables():
    print(v.name, "=", v.varValue)

print("Objective = ", value(model.objective))
