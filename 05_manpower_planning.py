from pulp import *

# Define the model
model = LpProblem(name="manpower-planning", sense=LpMaximize)

##################################################################
# Define the decision variables

types = range(1, 3) # 1: skilled, 2: semi-skilled 3: unskilled
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

# continuity

