from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# Create the model
model = LpProblem(name="small-problem", sense=LpMaximize)

# Initialize the decision variables
x = LpVariable(name="x", lowBound = 0, cat="Integer") # can solve mixed-integer linear programming problems
y = LpVariable(name="y", lowBound = 0)

model += (2 * x + y <= 20, "red_constraint")
model += (4 * x - 5 * y >= -10, "blue_contraint")
model += (-x + 2 * y >= -2, "yellow_contraint")
model += (-x + 5 * y == 15, "green_contraint")

# Add the objective function to the model
model += lpSum([x, 2 * y])

# Solve the problem
status = model.solve()

# Show result
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")
for var in model.variables():
    print(f"{var.name}: {var.value()}")

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")
