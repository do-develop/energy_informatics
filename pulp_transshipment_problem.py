# Initialize LP Model
from pulp import *
prob = LpProblem("Mateiral_Supply_Problem", LpMinimize)

# Create variables/parameters
factories = ["F1", "F2", "F3"]
supply = {"F1": 100, "F2": 200, "F3": 300}
projects = ["D1", "D2", "D3"]
demand = {"D1": 50, "D2": 150, "D3": 300}
warehouses = ["W1", "W2"]
# cost factories to wareshouses
cost_1 = [
    [3, 2],
    [4, 3],
    [2.5, 3.5],
]
# cost warehouses to demand
cost_2 = [
    [2, 1, 4],
    [3, 2, 5],
]

cost_1 = makeDict([factories, warehouses], cost_1, 0)
cost_2 = makeDict([warehouses, projects], cost_2, 0)

# Define Decision Variable
Routes1 = [(f, w) for f in factories for w in warehouses]
r1 = LpVariable.dicts("Route", (factories, warehouses), 0, None, LpInteger)
Routes2 = [(w, p) for w in warehouses for p in projects]
r2 = LpVariable.dicts("Route", (warehouses, projects), 0, None, LpInteger)

# Objective Function
prob += (
        lpSum([r1[f][w] * cost_1[f][w] for (f, w) in Routes1]) + \
        lpSum([r2[w][p] * cost_2[w][p] for (w, p) in Routes2]),
        "Sum_of_transporting_costs",
    )

# Define Constraints
for f in factories:
    prob += (
        lpSum([r1[f][w] for w in warehouses]) <= supply[f],
        "Sum_of_product_ouf_of_factorie_%s" % f,
    )
for d in projects:
    prob += (
        lpSum([r2[w][d] for w in warehouses]) >= demand[d],
        "Sum_of_product_ouf_of_factorie_%s" % d,
    )
for w in warehouses:
    prob += (
        lpSum([r1[f][w] for f in factories]) - \
        lpSum([r2[w][d] for d in projects]) == 0,
        "Demand_and_supply_matches_%s" % w,
    )

prob.solve()
for v in prob.variables():
    print(v.name, "=", v.varValue)

print("Value of Objective Function = ", value(prob.objective))

