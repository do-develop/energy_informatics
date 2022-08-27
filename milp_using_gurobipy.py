# mixed integer linear programming using gurobipy
from gurobipy import *

# 1 build model
milp_model = Model("milp")

# 2 add variables
x = milp_model.addVar(vtype=GRB.BINARY, name="x")
y = milp_model.addVar(vtype=GRB.CONTINUOUS, lb=0, name="y")
z = milp_model.addVar(vtype=GRB.INTEGER, lb=0, name="z")

# 3 define objective function
obj_fn = 2 * x + y + 3 * z
milp_model.setObjective(obj_fn, GRB.MAXIMIZE)

# 4 add contraints
c1 = milp_model.addConstr(x + 2 * y + z <= 4, "c1")
c2 = milp_model.addConstr(2 * z + y <= 5, "c2")
c3 = milp_model.addConstr(x + y >= 1, "c3")

milp_model.optimize()
