from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# Define the model
model = LpProblem(name="resource-allocation", sense=LpMaximize)

# Define the decision variables
x = {i: LpVariable(name=f"x{i}", lowBound=0) for i in range(1, 6)}

# Add contraints
model += (20 * x[1] + 20 * x[2] + 20 * x[3] + 20 * x[4] + 20 * x[5] <= 384, "manpower")
model += (12 * x[1] + 20 * x[2] + 25 * x[4] + 15 * x[5] <= 288, "grinding")
model += (10 * x[1] + 8 * x[2] + 16 * x[3] <= 192, "drilling")

# Set the objectives
model += 550 * x[1] + 600 * x[2] + 350 * x[3] + 400 * x[4] + 200 * x[5]

status = model.solve()

print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
for var in x.values():
    print(f"{var.name}: {var.value()}")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
