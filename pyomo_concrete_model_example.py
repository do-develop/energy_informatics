from pyomo.environ import *

model = ConcreteModel()

# decision variables
model.l = Var(within=NonNegativeReals) # number of llmas the farmer should raise
model.g = Var(within=NonNegativeReals) # number of goats the farmer should raise

# objective function
model.maximizeProfit = Objective(expr = 200 * model.l + 300 * model.g, sense=maximize)

# constraints
# constraints - labor: the farmer has only 100 hours
model.LaborConstraint = Constraint(expr = 3 * model.l + 2 * model.g <= 100)
# constraints - medical: only has 120 dollars for medical
model.MedicalConstraint = Constraint(expr = 2 * model.l + 4 * model.g <= 120)
# constraints - acres: only has 45 acres
model.LandConstraint = Constraint(expr = model.l + model.g <= 45)

# run model
optimiser = SolverFactory("glpk")
optimiser.solve(model)
model.display()
