from pulp import *

# Define Model
model = LpProblem("Balanced_Diet_Problem", LpMinimize)

# Define Decision Variables
x1 = LpVariable("wheat", 0, None, LpContinuous)
x2 = LpVariable("rice", 0, None, LpContinuous)
x3 = LpVariable("corn", 0, None, LpContinuous)

# Define Objective Function
model += 0.03 * x1 + 0.05 * x2 + 0.02 * x3

# Define Contraints
model += 4*x1 + 2*x2 + 2*x3 >= 27       # Protien
model += 420*x1 + 25*x2 + 21*x3 >= 240  # Carbohyderate
model += 90*x1 + 110*x2 + 100*x3 >= 27  # Calories
model += x1 + x2 + x3 >= 12

# Solve
model.solve()

# Result
for v in model.variables():
    print(v.name, '=', v.varValue)

print("Value of Objective Function = ", value(model.objective))
