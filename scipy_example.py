from scipy.optimize import linprog
"""
linprog only solves only minimization problems!!!
"""
# objective function
obj = [-1, -2] # coefficients of x , y

# inequality contraints
lhs_ineq = [[2, 1],
            [-4, 5],
            [1, -2]]
rhs_ineq = [20,
            10,
            2]

# equality contraints
lhs_eq = [[-1, 5]]
rhs_eq = [15]

# bounds
bnd = [(0, float("inf")), # bounds of x
       (0, float("inf"))] # bounds of y

# Optimise!
opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd,
              method="revised simplex")
"""
method="interior-point" selects the interior-point method. This option is set by default.
method="revised simplex" selects the revised two-phase simplex method.
method="simplex" selects the legacy two-phase simplex method.
"""

print(opt)
"""
.con is the equality constraints residuals.

.fun is the objective function value at the optimum (if found).

.message is the status of the solution.

.nit is the number of iterations needed to finish the calculation.

.slack is the values of the slack variables, or the differences between the values of the left and right sides of the constraints.

.status is an integer between 0 and 4 that shows the status of the solution, such as 0 for when the optimal solution has been found.

.success is a Boolean that shows whether the optimal solution has been found.

.x is a NumPy array holding the optimal values of the decision variables.
"""
