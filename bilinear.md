C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe D:\code\python\or-gurobi-demos\bilinear.py 
Restricted license - for non-production use only - expires 2026-11-23
Gurobi Optimizer version 12.0.0 build v12.0.0rc1 (win64 - Windows 11.0 (22621.2))

CPU model: 13th Gen Intel(R) Core(TM) i7-13700F, instruction set [SSE2|AVX|AVX2]
Thread count: 16 physical cores, 24 logical processors, using up to 24 threads

Optimize a model with 1 rows, 3 columns and 3 nonzeros
Model fingerprint: 0x83663ee2
Model has 2 quadratic constraints
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  QMatrix range    [1e+00, 1e+00]
  Objective range  [1e+00, 1e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [1e+01, 1e+01]
  QRHS range       [1e+00, 2e+00]

Continuous model is non-convex -- solving as a MIP

Presolve time: 0.00s
Presolved: 12 rows, 6 columns, 27 nonzeros
Presolved model has 3 bilinear constraint(s)
Variable types: 6 continuous, 0 integer (0 binary)
Found heuristic solution: objective 9.8989795

Root relaxation: interrupted, 0 iterations, 0.00 seconds (0.00 work units)

Explored 1 nodes (0 simplex iterations) in 0.00 seconds (0.00 work units)
Thread count was 24 (of 24 available processors)

Solution count 1: 9.89898 

Optimal solution found (tolerance 1.00e-04)
Best objective 9.898979482305e+00, best bound 9.898980554584e+00, gap 0.0000%

    Variable            x 
-------------------------
           x      9.89898 
           z     0.101021 
Gurobi Optimizer version 12.0.0 build v12.0.0rc1 (win64 - Windows 11.0 (22621.2))

CPU model: 13th Gen Intel(R) Core(TM) i7-13700F, instruction set [SSE2|AVX|AVX2]
Thread count: 16 physical cores, 24 logical processors, using up to 24 threads

Optimize a model with 1 rows, 3 columns and 3 nonzeros
Model fingerprint: 0x81133406
Model has 2 quadratic constraints
Variable types: 2 continuous, 1 integer (0 binary)
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  QMatrix range    [1e+00, 1e+00]
  Objective range  [1e+00, 1e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [1e+01, 1e+01]
  QRHS range       [1e+00, 2e+00]

MIP start from previous solve did not produce a new incumbent solution

Presolve time: 0.00s
Presolved: 12 rows, 6 columns, 27 nonzeros
Presolved model has 3 bilinear constraint(s)

Solving non-convex MIQCP

Variable types: 5 continuous, 1 integer (0 binary)
Found heuristic solution: objective -0.0000000

Root relaxation: objective 9.000000e+00, 1 iterations, 0.00 seconds (0.00 work units)

    Nodes    |    Current Node    |     Objective Bounds      |     Work
 Expl Unexpl |  Obj  Depth IntInf | Incumbent    BestBd   Gap | It/Node Time

*    0     0               0       9.0000000    9.00000  0.00%     -    0s

Explored 1 nodes (1 simplex iterations) in 0.00 seconds (0.00 work units)
Thread count was 24 (of 24 available processors)

Solution count 2: 9 -0 

Optimal solution found (tolerance 1.00e-04)
Best objective 9.000000000000e+00, best bound 9.000000000000e+00, gap 0.0000%

    Variable            x 
-------------------------
           x            9 
           z     0.111111 

进程已结束，退出代码为 0
