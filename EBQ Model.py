import numpy as np
import pandas as pd
from itertools import permutations

import gurobipy as gp
from gurobipy import GRB

#SKUs list. Taking at oil level for example
products = ["BLEND", "RICEBRAN", "SOYA", "PALM"]

#Taking only two months due to Gurobi license
months = ["Apr", "May"]

#monthly demand
demand = {("Apr","BLEND"):120,("May","BLEND"):130,
          ("Apr","RICEBRAN"):270,("May","RICEBRAN"):260,
          ("Apr","SOYA"):3000,("May","SOYA"):4000,
          ("Apr","PALM"):4000,("May","PALM"):5000}

#Sequence-dependent changeover costs
changeover = {("BLEND","RICEBRAN"):4401,
              ("BLEND","SOYA"):4401,
              ("BLEND","PALM"):4401,
              ("RICEBRAN","BLEND"):4401,
              ("RICEBRAN","SOYA"):5401,
              ("RICEBRAN","PALM"):1499,
              ("SOYA","BLEND"):3401,
              ("SOYA","RICEBRAN"):3401,
              ("SOYA","PALM"):1099,
              ("PALM","BLEND"):4401,
              ("PALM","RICEBRAN"):2901,
              ("PALM","SOYA"):2901}

#generating all permutations
sequences = list(permutations(products,2))

changeover_cost = {}

for i in range(len(products)-1):
    sequences += list(permutations(products,i+3))

#Creating permutation-wise changeover costs
for sequence in sequences:
    x = 0
    for i in range(len(sequence)-1):
        x += changeover[(sequence[i],sequence[i+1])]
    changeover_cost[sequence] = x


factory = gp.Model('Changeover Planning')

store = factory.addVars(months, products, name="Store") 

make = factory.addVars(months, products, name="Make")

select = factory.addVars(months, tuple(sequences), vtype=GRB.INTEGER, name="Select")

#M0 closing inventory
InventoryM0 = factory.addConstrs((make[months[0], product] == demand[months[0], product] 
                  + store[months[0], product] for product in products), name="Initial_Balance")
    
#Other months closing inventory
InventoryM = factory.addConstrs((store[months[months.index(month) -1], product] + 
                make[month, product] == demand[month, product] + store[month, product] 
                for product in products for month in months 
                if month != months[0]), name="Balance")

#Constraint for selecting only 1 sequence per month
Select_Sequence = factory.addConstrs(gp.quicksum(select[(month,)+ sequence] for sequence in sequences) == 1 for month in months)

#Constraint for production only if the product is present in selected sequence for the month
Make_If = factory.addConstrs(select[(month,) + sequence] * make[month,product] == make[month,product] for product in sequence for sequence in sequences for month in months)

#Constraint for keeping lot size same across months
Same_Lot = factory.addConstrs(make[months[months.index(month) -1],product] == make[month,product] for month in months for product in products if month != months[0])

#Objective function to Minimize changeover + inventory holding cost rate. Considered 3 as inventory holding cost rate per unit without considering oil cost.
obj = gp.quicksum(select[(month,)+ sequence] * changeover_cost[sequence]+ (store[month,product]) * 3 for product in sequence for sequence in sequences for month in months)

factory.params.NonConvex = 2

factory.setObjective(obj, GRB.MINIMIZE)


factory.optimize()


#Print results
rows = months.copy()
columns = products.copy()
make_plan = pd.DataFrame(columns=columns, index=rows, data=0.0)


for month, product in make.keys():
        make_plan.loc[month, product] = np.round(make[month, product].x, 1)
print(make_plan)

