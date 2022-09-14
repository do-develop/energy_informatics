from pulp import *

model = LpProblem("Staff_Scheduling_Problem", LpMinimize)

# 4 types of shift
shifts = list(range(4))

# Decision Variables
x = LpVariable.dict("fulltimeshift_", shifts, lowBound=0, cat="Integer")
y = LpVariable.dict("parttimeshift_", shifts, lowBound=0, cat="Integer")

# Objective Function
model += 150*lpSum([x[i] for i in shifts]) + 45*lpSum([y[i] for i in shifts])

# Constraints
model += x[0] + y[0] >= 6
model += x[0] + x[1] + y[1] >= 11
model += x[0] + x[1] + y[2] >= 8
model += x[1] + y[3] >= 6

model += x[0] >= 1
model += x[1] >= 1

model.solve()
for v in model.variables():
    print(v.name, " = ", v.varValue)
print("Total staffing cost : ", value(model.objective))
