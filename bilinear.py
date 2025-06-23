# _*_ coding: utf_8 _*_
# @Time : 2025/6/23 20:39
# @Author : flynn
# @File : bilinear
# @Project: or-gurobi-demos
# Copyright 2025, Gurobi Optimization, LLC

# This example formulates and solves the following simple bilinear model:
#  maximize    x
#  subject to  x + y + z <= 10
#              x * y <= 2         (bilinear inequality)
#              x * z + y * z = 1  (bilinear equality)
#              x, y, z non-negative (x integral in second version)

import gurobipy as gp
from gurobipy import GRB

m = gp.Model("bilinear")

# 变量
x = m.addVar(name="x")
y = m.addVar(name="y")
z = m.addVar(name="z")

m.setObjective(x,GRB.MAXIMIZE)

# 约束
m.addConstr(x+y+z <= 10,name="c1")
m.addConstr(x*y <= 2,name="bilinear0")
m.addConstr(x*z + y*z == 1,name="bilinear1")

m.optimize()

# 加引号
m.printAttr("x")

x.VType=GRB.INTEGER
m.optimize()

m.printAttr("x")






