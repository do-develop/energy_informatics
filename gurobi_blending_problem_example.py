from gurobipy import *

model = Model()

# Decision Variable (two ingredients)
x1 = model.addVar(vtype="C", name="ingredient_1") # C = continuous 
x2 = model.addVar(vtype="C", name="ingredient_2")

# Objective Function
model.setObjective(4*x1 + 5*x2, GRB.MINIMIZE)

# Constraints
model.addConstr(3*x1 + 5*x2 >= 30, "protein_in_grams")
model.addConstr(3*x1 + 2*x2 >= 24, "carbohydrates_in_grams")
model.addConstr(x1 >= 0, "ingredient1_low_bound")
model.addConstr(x2 >= 0, "ingredient2_low_bound")

# Solve
model.optimize()

for v in model.getVars():
    print(v.varName, v.x)
    
print("Minimized cost: ", model.objVal)
