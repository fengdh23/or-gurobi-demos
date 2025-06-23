# _*_ coding: utf_8 _*_
# @Time : 2025/6/23 21:16
# @Author : flynn
# @File : mip1
# @Project: or-gurobi-demos
# Copyright 2025, Gurobi Optimization, LLC

# This example formulates and solves the following simple MIP model:
#  maximize
#        x +   y + 2 z
#  subject to
#        x + 2 y + 3 z <= 4
#        x +   y       >= 1
#        x, y, z binary 二进制


import gurobipy as gp
from gurobipy import GRB

try:
    m = gp.Model("mip")
    # Create variables
    x = m.addVar(vtype=GRB.BINARY, name="x")
    y = m.addVar(vtype=GRB.BINARY, name="y")
    z = m.addVar(vtype=GRB.BINARY, name="z")

    # Set objective
    m.setObjective(x+y + 2*z, GRB.MAXIMIZE)

    # Add constraint: x + 2 y + 3 z <= 4
    m.addConstr(x + 2 * y + 3 * z <= 4, name="c1")
    # Add constraint: x + y >= 1
    m.addConstr(x + y >= 1, name="c2")

    # Optimize model
    m.optimize()

    for v in m.getVars():
        print(f"{v.VarName} {v.X:g}")

    print(f"Obj: {m.ObjVal:g}")

except gp.GurobiError as e:
    print(f"Error code {e.errno}: {e}")
except AttributeError:
    print("Encountered an attribute error")


