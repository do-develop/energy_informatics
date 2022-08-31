from pulp import *

# Define the model
model = LpProblem(name="blending-problem", sense=LpMaximize)

# Define the decision variables
types = range(0, 5)
states = range(0, 3) # 0: buying, 1: using, 2: storing
months = range(0, 6)

x = LpVariable.dicts("oil", (types, states, months),lowBound=0, cat="Continuous")
y = {i: LpVariable(name=f"y{i}", lowBound=0) for i in months}
z = LpVariable.dicts("oil", (types, months),lowBound=0, cat="Binary")

m_rate =[[110, 120, 130, 110, 115],
        [130, 130, 110, 90, 115],
        [110, 140, 130, 100, 95],
        [120, 110, 120, 120, 125],
        [100, 120, 150, 110, 105],
        [90, 100, 140, 80, 135]]
# Add contraints
for m in months:
    model += (x[0][1][m] + x[1][1][m] <= 200, f"veg{m}")
    model += (x[2][1][m] + x[3][1][m] + x[4][1][m] <= 250, f"non-veg{m}")
    model += (8.8*x[0][1][m] + 6.1*x[1][1][m] + 2.0*x[2][1][m] + 4.2*x[3][1][m] + 5.0*x[4][1][m] - 6*y[m] <= 0, f"max-hardness{m}")
    model += (8.8*x[0][1][m] + 6.1*x[1][1][m] + 2.0*x[2][1][m] + 4.2*x[3][1][m] + 5.0*x[4][1][m] - 3*y[m] >= 0, f"min-hardness{m}")
    # Set the objectives
    model += (-1* m_rate[m][0] * x[0][0][m] + \
              -1* m_rate[m][1] * x[1][0][m] + \
              -1* m_rate[m][2] * x[2][0][m] + \
              -1* m_rate[m][3] * x[3][0][m] + \
              -1* m_rate[m][4] * x[4][0][m] + \
              150 * y[m])
# Additional storage constraints
for t in types:
    model += (x[t][0][0] - x[t][1][0] - x[t][2][0] == -500, f"oil{t}-storage1")
    model += (x[t][2][0] + x[t][0][1] - x[t][1][1] - x[t][2][1] == 0, f"oil{t}-storage2")
    model += (x[t][2][1] + x[t][0][2] - x[t][1][2] - x[t][2][1] == 0, f"oil{t}-storage3")
    model += (x[t][2][2] + x[t][0][3] - x[t][1][3] - x[t][2][1] == 0, f"oil{t}-storage4")
    model += (x[t][2][3] + x[t][0][4] - x[t][1][4] - x[t][2][1] == 0, f"oil{t}-storage5")
    model += (x[t][2][4] + x[t][0][5] - x[t][1][5] == 500, f"oil{t}-storage6")
# Additional minimum use contraints
for t in types:
    for m in months:
        model += (x[t][1][m] - 200 * z[t][m] <= 0)
        model += (x[t][1][m] - 20 * z[t][m] >= 0)
# at least three should be used
for m in months:
    model += (z[0][m] + z[1][m] + z[2][m] + z[3][m] + z[4][m] <= 3)
    # oil1 oil2 used then use oil5
    model += (z[0][m] - z[4][m] <= 0)
    model += (z[1][m] - z[4][m] <= 0)
    
    
status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
for t in types:
    for s in states:
        for m in months:
            print(f"{x[t][s][m]}: {x[t][s][m].value()}")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
