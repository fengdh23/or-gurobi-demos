# Solve a multi-commodity flow problem.  Two products ('Pencils' and 'Pens')
# are produced in 2 cities ('Detroit' and 'Denver') and must be sent to
# warehouses in 3 cities ('Boston', 'New York', and 'Seattle') to
# satisfy supply/demand ('inflow[h,i]').
#
# Flows on the transportation network must respect arc capacity constraints
# ('capacity[i,j]'). The objective is to minimize the sum of the arc
# transportation costs ('cost[i,j]').
import gurobipy as gp
from gurobipy import GRB

# Base data
commodities = ["Pencils", "Pens"]
nodes = ["Detroit", "Denver", "Boston", "New York", "Seattle"]

arcs, capacity = gp.multidict({
  ("Detroit", "Boston"):   100,
  ("Detroit", "New York"): 80 ,
  ("Detroit", "Seattle"):  120,
  ("Denver", "Boston"):    120,
  ("Denver", "New York"):  120,
  ("Denver", "Seattle"):   120
})

# Cost for triplets commodity-source-destination
cost = {
    ("Pencils", "Detroit", "Boston"):   10,
    ("Pencils", "Detroit", "New York"): 20,
    ("Pencils", "Detroit", "Seattle"):  60,
    ("Pencils", "Denver", "Boston"):   40,
    ("Pencils", "Denver", "New York"): 40,
    ("Pencils", "Denver", "Seattle"):  30,
    ("Pens", "Detroit", "Boston"):   20,
    ("Pens", "Detroit", "New York"):   20,
    ("Pens", "Detroit", "Seattle"):   80,
    ("Pens", "Denver", "Boston"):   60,
    ("Pens", "Denver", "New York"):   70,
    ("Pens", "Denver", "Seattle"):   30
}

# Supply (> 0) and demand (< 0) for pairs of commodity-city
inflow = {
    ("Pencils", "Detroit"):  50,
     ("Pencils", "Denver"): 60,
    ("Pencils", "Boston"):  -50,
    ("Pencils", "New York"): -50,
    ("Pencils", "Seattle"):    -10,
    ("Pens", "Detroit"): 60,
    ("Pens", "Denver"): 40,
    ("Pens", "Boston"): -40,
    ("Pens", "New York"): -30,
    ("Pens", "Seattle"): -30,
}


# Create optimization model
m = gp.Model("netflow")

# create variables
flow = m.addVars(commodities, arcs, obj=cost, name="flow")

# Arc-capacity constraints
m.addConstrs((flow.sum("*", i, j) <= capacity[i, j] for i, j in arcs), "Cap")

# Flow-conservation constraints
m.addConstrs(
   (
        flow.sum(h, "*", j) + inflow[h, j] == flow.sum(h, j, "*")
        for h in commodities
        for j in nodes
    ),
    "node",
)

# Compute optimal solution
m.optimize()

# Print solution
if m.Status == GRB.OPTIMAL:
    solution = m.getAttr("X", flow)
    for h in commodities:
        print(f"\nOptimal flows for {h}:")
        for i, j in arcs:
            if solution[h, i, j] > 0:
                print(f"{i} -> {j}: {solution[h, i, j]:g}")

                # Print solution
if m.Status == GRB.OPTIMAL:
    solution = m.getAttr("X", flow)
    for h in commodities:
        print(f"\nOptimal flows for {h}:")
        for i, j in arcs:
            if solution[h, i, j] > 0:
                print(f"{i} -> {j}: {solution[h, i, j]:g}")


