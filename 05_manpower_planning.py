from pulp import *

# Define the model
model = LpProblem(name="manpower-planning", sense=LpMaximize)

##################################################################
# Define the decision variables

types = range(1, 4) # 1: skilled, 2: semi-skilled 3: unskilled
years = range(0, 4) # 0: current 1: year1 ...
# Strength of Labour Force
lf = LpVariable.dicts("lf", (years, types), lowBound=0, cat="Integer")
# Recruitment
rc = LpVariable.dicts("rc", (years, types), lowBound=0, cat="Integer")

# Retraining
rt_usss = {i: LpVariable(name=f"rt_usss{i}", lowBound=0) for i in years}
rt_sssk = {i: LpVariable(name=f"rt_sssk{i}", lowBound=0) for i in years}
# Downgrading
d_skss = {i: LpVariable(name=f"d_skss{i}", lowBound=0) for i in years}
d_skus = {i: LpVariable(name=f"d_skus{i}", lowBound=0) for i in years}
d_ssus = {i: LpVariable(name=f"d_ssus{i}", lowBound=0) for i in years}
# Redundancy
rd_sk = {i: LpVariable(name=f"rd_sk{i}", lowBound=0) for i in years}
rd_ss = {i: LpVariable(name=f"rd_ss{i}", lowBound=0) for i in years}
rd_us = {i: LpVariable(name=f"rd_us{i}", lowBound=0) for i in years}
# Short-time Working
st_sk = {i: LpVariable(name=f"st_sk{i}", lowBound=0) for i in years}
st_ss = {i: LpVariable(name=f"st_ss{i}", lowBound=0) for i in years}
st_us = {i: LpVariable(name=f"st_us{i}", lowBound=0) for i in years}
# Overmanning
ov_sk = {i: LpVariable(name=f"ov_sk{i}", lowBound=0) for i in years}
ov_ss = {i: LpVariable(name=f"ov_ss{i}", lowBound=0) for i in years}
ov_us = {i: LpVariable(name=f"ov_us{i}", lowBound=0) for i in years}

##################################################################
# Add Constraints

# initial condition
model += (lf[0][1] == 1000)
model += (lf[0][2] == 1500)
model += (lf[0][3] == 2000)

# 1. Continuity
for i in (1, 4):
    model += (lf[i][1] == 0.95 * lf[i-1][1] + 0.9 * rc[i][1]  + 0.95 * rt_sssk[i] - d_skss[i] - d_skus[i] - rd_sk[i])
    model += (lf[i][2] == 0.95 * lf[i-1][2] + 0.8 * rc[i][2]  + 0.95 * rt_usss[i] - rt_sssk[i] + 0.5 * d_skss[i] - d_ssus[i] - rd_ss[i])
    model += (lf[i][3] == 0.9 * lf[i-1][3] + 0.75 * rc[i][3] - rt_usss[i] + 0.5 * d_skus[i] + 0.5 * d_ssus[i] - rd_us[i])
    
# 2. Retraining semi-skilled workers
for i in years:
    model += (rt_sssk[i] - 0.25 * lf[i][1] <= 0)
    
# 3. Overmanning
for i in years:
    ov_sk[i] + ov_ss[i] + ov_us <= 150
    
# 4. Requirements
model += lf[1][1] - ov_sk[1] - 0.5 * st_sk[1] == 1000
model += lf[2][1] - ov_sk[2] - 0.5 * st_sk[2] == 1500
model += lf[3][1] - ov_sk[3] - 0.5 * st_sk[3] == 2000

model += lf[1][2] - ov_ss[1] - 0.5 * st_ss[1] == 1400
model += lf[2][2] - ov_ss[2] - 0.5 * st_ss[2] == 2000
model += lf[3][2] - ov_ss[3] - 0.5 * st_ss[3] == 2500

model += lf[1][3] - ov_ss[1] - 0.5 * st_ss[1] == 1000
model += lf[2][3] - ov_ss[2] - 0.5 * st_ss[2] == 500
model += lf[3][3] - ov_ss[3] - 0.5 * st_ss[3] == 0

##################################################################
# Objective Function

# 1 minimize redundancy

# 2 minimize cost


"""
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
for t in types:
    for s in states:
        for m in months:
            print(f"{x[t][s][m]}: {x[t][s][m].value()}")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
"""
