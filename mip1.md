Optimize a model with 2 rows, 3 columns and 5 nonzeros 
模型有2个约束（行）、3个变量（列）、5个非零系数。

Model fingerprint: 0x98886187
Variable types: 0 continuous, 3 integer (3 binary)
Coefficient statistics:  系数分析
  Matrix range     [1e+00, 3e+00]
  Objective range  [1e+00, 2e+00]
  Bounds range     [1e+00, 1e+00]
  RHS range        [1e+00, 4e+00]
Found heuristic solution: objective 2.00000000  启发式解法，目标函数值为2
Presolve removed 2 rows and 3 columns   预处理 删除了2行和3列
Presolve time: 0.00s
Presolve: All rows and columns removed

Explored 0 nodes (0 simplex iterations) in 0.00 seconds (0.00 work units)
Thread count was 1 (of 24 available processors)

Solution count 2: 3 2
'找到2个可行解，最优目标值为3，次优为2。'

Optimal solution found (tolerance 1.00e-04)
Best objective 3.000000000000e+00, best bound 3.000000000000e+00, gap 0.0000%
x 1
y 0
z 1
Obj: 3