from pulp import *

# Minimization Problem
model = LpProblem("Material_Supply_Problem", LpMinimize)

# Variables
warehouses = ["W1", "W2", "W3"]
projects = ["D1", "D2", "D3"]
# creates a list of tuples containing all the possible routes for transport
Routes = [(w, d) for w in warehouses for d in projects]

supply = {"W1": 300, "W2": 600, "W3": 600}
demand = {
    "D1": 150,
    "D2": 450,
    "D3": 900,
}

costs = [
    [5,1,9],
    [4,2,8],
    [8,7,2]
]
costs = makeDict([warehouses, projects], costs, 0)
# dictionary to contain the referenced variables (the routes)
route = LpVariable.dicts("Route", (warehouses, projects), 0, None, LpInteger)

# OBJECTIVE FUNCTION
model += (
    lpSum([route[w][d] * costs[w][d] for (w, d) in Routes]),
    "Sum_of_Transportation_Costs",
)

# CONSTRAINTS
# the supply maximum constraints are added to prob for each supply node
for w in warehouses:
    model += (
            lpSum([route[w][d] for d in projects]) <= supply[w],
            "supply_restriction_%s" % w,
        )

for d in projects:
    model += (
            lpSum([route[w][d] for w in warehouses]) >= demand[d],
            "demand_restriction_%s" % d,
        )

# SOLUTION
model.solve()
for v in model.variables():
    print(v.name, "=", v.varValue)
print("Value of Objective Function = ", value(model.objective))







