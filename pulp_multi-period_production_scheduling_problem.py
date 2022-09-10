from pulp import *

# Define problem
model = LpProblem("Minimize_Cost", LpMinimize)

# Defind production cost, inventory cost and demand
quaters = list(range(4))
prod_cost = [3000, 3300, 3600, 3600]
inv_cost = [250, 250, 250, 250]
demand = [2300, 2000, 3100, 3000]

# Decision Variables
x = LpVariable.dicts("quarter_prod", quaters, lowBound=0, cat="Continuous")
y = LpVariable.dicts("quarter_inv", quaters, lowBound=0, cat="Continuous")

# Objective Function
model += lpSum([prod_cost[i] * x[i] for i in quaters]) + \
         lpSum([inv_cost[i] * y[i] for i in quaters])

# Constraints
# production capacity
for i in quaters:
    model.addConstraint(x[i] <= 3000)
# inventory balance
model.addConstraint(x[0] - y[0] == demand[0]) # first month
for i in quaters[1:]:
    model.addConstraint(x[i] - y[i] + y[i - 1] == demand[i])

# Solve
model.solve()
for v in model.variables():
    print(v.name, "=", v.varValue)
print("Value of Objective Function = ", value(model.objective))
