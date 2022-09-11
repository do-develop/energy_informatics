from pulp import *
import pandas as pd

# DEFINE PROBLEM
model = LpProblem("Manufacturing_Profits", LpMaximize)

# DEFINE DECISION VARIABLES
A = LpVariable('A', lowBound=0)
B = LpVariable('B', lowBound=0)

# OBJECTIVE FUNCTION
model += 60*A + 50*B

# CONSTRAINTS
model += 4*A + 10*B <= 100  # slack 24 in c1 - increase or decrease upto 24, it won't affect the objective value
model += 2*A + 1*B <= 22    # shadow 10 in c2 - increase 1 here then the objective value increases by 10
model += 3*A + 3*B <= 39    # shadow 13.3 in c3 - increase 1 here then the objective value increases by 13.3

model.solve()
print("Model Status:{}".format(LpStatus[model.status]))
print("Objective = ", value(model.objective))
for v in model.variables():
    print(v.name, "=", v.varValue)

# SENSITIVE ANALYSIS
# shadow price and slack variables
data = [{'name':name, 'shadow price':c.pi, 'slack':c.slack} for name, c in model.constraints.items()]
print(pd.DataFrame(data))
