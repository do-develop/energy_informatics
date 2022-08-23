from scipy.optimize import linprog

obj = [-550, -600, -350, -400, -200]

lhs_ineq = [[20, 20, 20, 20, 20],   # Manpower
            [12, 20, 0, 25, 15],    # Grinding
            [10, 8, 16, 0, 0]]      # Drilling

rhs_ineq = [384,
            288,
            192]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
              method="revised simplex")

print(opt)
