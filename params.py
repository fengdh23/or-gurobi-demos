# Use parameters that are associated with a model.
#
# A MIP is solved for a few seconds with different sets of parameters.
# The one with the smallest MIP gap is selected, and the optimization
# is resumed until the optimal solution is found.

import sys
import gurobipy as gp


if len(sys.argv) < 2:
    print("Usage: params.py filename")
    sys.exit(0)


# Read model and verify that it is a MIP
m = gp.read(sys.argv[1])
if m.IsMIP == 0:
    print("The model is not an integer program")
    sys.exit(1)

# Set a 2 second time limit
m.Params.TimeLimit = 2

# Now solve the model with different values of MIPFocus
bestModel = m.copy()
bestModel.optimize()
for i in range(1, 4):
    m.reset()
    m.Params.MIPFocus = i
    m.optimize()
    if bestModel.MIPGap > m.MIPGap:
        bestModel, m = m, bestModel  # swap models

# Finally, delete the extra model, reset the time limit and
# continue to solve the best model to optimality
del m
bestModel.Params.TimeLimit = float("inf")
bestModel.optimize()
print(f"Solved with MIPFocus: {bestModel.Params.MIPFocus}")

# python .\params.py C:\gurobi1202\win64\examples\data\p0033.lp ide 中脚本形参
# 全路径可以？C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe D:\code\python\or-gurobi-demos\params.py C:\gurobi1202\win64\examples\data\p0033.lp