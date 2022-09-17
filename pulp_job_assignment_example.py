from pulp import *

workers = [1,2,3,4]
jobs = [1,2,3,4]

# Cost matrix
costs = [[1,2,1,9],
         [4,5,2,2],
         [7,3,9,3],
         [2,3,5,1]]

prob = LpProblem("job_assignment", LpMinimize)

# the cost data into a dictionary
costs = makeDict([workers, jobs], costs, 0)
assign = [(w, j) for w in workers for j in jobs]
# decision variable
d_var = LpVariable.dicts("assign", (workers, jobs), 0, None, LpBinary) # whether the job will be assigned to a worker or not

# OBJECTIVE FUNCTION
prob += ( lpSum([d_var[w][j] * costs[w][j] for (w, j) in assign]),
          "sum_of_assignment_costs",
          )

# Constraints
for j in jobs:
    prob += lpSum(d_var[w][j] for w in workers) == 1

for w in workers:
    prob += lpSum(d_var[w][j] for j in jobs) == 1

prob.solve()
for v in prob.variables():
    if v.varValue == 1.0:
        print(v.name, "=", v.varValue)
print("Value of Objective Function = ", value(prob.objective))
