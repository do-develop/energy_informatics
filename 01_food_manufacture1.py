import pulp as pl

# Define the model
model = pl.LpProblem(name="blending-problem", sense=pl.LpMaximize)

# Define the decision variables
x = {i: pl.LpVariable(name=f"x{i}", lowBound=0) for i in range(1, 6)}
y = pl.LpVariable("y", lowBound = 0, cat="Continuous")

# Add contraints
model += (x[1] + x[2] <= 200, "refine_contraint_on_veg_oil")
model += (x[3] + x[4] + x[5] <= 250, "refine_contraint_on_non-veg_oil")
model += (8.8*x[1] + 6.1*x[2] + 2.0*x[3] + 4.2*x[4] + 5.0*x[5] - 6*y <= 0, "max_hardness_constraint")
model += (8.8*x[1] + 6.1*x[2] + 2.0*x[3] + 4.2*x[4] + 5.0*x[5] - 3*y >= 0, "min_hardness_constraint")

# Set the objectives
model += -110 * x[1] + -120 * x[2] + -130 * x[3] - 110 * x[4] -115 * x[5] + 150 * y

status = model.solve()

print(f"status: {model.status}, {pl.LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
for var in x.values():
    print(f"{var.name}: {var.value()}")
for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
