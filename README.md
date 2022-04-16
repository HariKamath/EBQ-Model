# EBQ-Model
Paper Model for Determining Economic Order Quantity

**products** = ["BLEND", "RICEBRAN", "SOYA", "PALM"]

**months** = ["Apr", "May"]

**demand** = {("Apr","BLEND"):120,("May","BLEND"):130,
          ("Apr","RICEBRAN"):270,("May","RICEBRAN"):260,
          ("Apr","SOYA"):3000,("May","SOYA"):4000,
          ("Apr","PALM"):4000,("May","PALM"):5000}

**changeover** = {("BLEND","RICEBRAN"):4401,
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
			  
**sequences** = ('BLEND', 'RICEBRAN')
('BLEND', 'SOYA')
('BLEND', 'PALM')
('RICEBRAN', 'BLEND')
('RICEBRAN', 'SOYA')
('RICEBRAN', 'PALM')
('SOYA', 'BLEND')
('SOYA', 'RICEBRAN')
('SOYA', 'PALM')
('PALM', 'BLEND')
('PALM', 'RICEBRAN')
('PALM', 'SOYA')
('BLEND', 'RICEBRAN', 'SOYA')
('BLEND', 'RICEBRAN', 'PALM')
('BLEND', 'SOYA', 'RICEBRAN')
('BLEND', 'SOYA', 'PALM')
('BLEND', 'PALM', 'RICEBRAN')
('BLEND', 'PALM', 'SOYA')
('RICEBRAN', 'BLEND', 'SOYA')
('RICEBRAN', 'BLEND', 'PALM')
('RICEBRAN', 'SOYA', 'BLEND')
('RICEBRAN', 'SOYA', 'PALM')
('RICEBRAN', 'PALM', 'BLEND')
('RICEBRAN', 'PALM', 'SOYA')
('SOYA', 'BLEND', 'RICEBRAN')
('SOYA', 'BLEND', 'PALM')
('SOYA', 'RICEBRAN', 'BLEND')
('SOYA', 'RICEBRAN', 'PALM')
('SOYA', 'PALM', 'BLEND')
('SOYA', 'PALM', 'RICEBRAN')
('PALM', 'BLEND', 'RICEBRAN')
('PALM', 'BLEND', 'SOYA')
('PALM', 'RICEBRAN', 'BLEND')
('PALM', 'RICEBRAN', 'SOYA')
('PALM', 'SOYA', 'BLEND')
('PALM', 'SOYA', 'RICEBRAN')
('BLEND', 'RICEBRAN', 'SOYA', 'PALM')
('BLEND', 'RICEBRAN', 'PALM', 'SOYA')
('BLEND', 'SOYA', 'RICEBRAN', 'PALM')
('BLEND', 'SOYA', 'PALM', 'RICEBRAN')
('BLEND', 'PALM', 'RICEBRAN', 'SOYA')
('BLEND', 'PALM', 'SOYA', 'RICEBRAN')
('RICEBRAN', 'BLEND', 'SOYA', 'PALM')
('RICEBRAN', 'BLEND', 'PALM', 'SOYA')
('RICEBRAN', 'SOYA', 'BLEND', 'PALM')
('RICEBRAN', 'SOYA', 'PALM', 'BLEND')
('RICEBRAN', 'PALM', 'BLEND', 'SOYA')
('RICEBRAN', 'PALM', 'SOYA', 'BLEND')
('SOYA', 'BLEND', 'RICEBRAN', 'PALM')
('SOYA', 'BLEND', 'PALM', 'RICEBRAN')
('SOYA', 'RICEBRAN', 'BLEND', 'PALM')
('SOYA', 'RICEBRAN', 'PALM', 'BLEND')
('SOYA', 'PALM', 'BLEND', 'RICEBRAN')
('SOYA', 'PALM', 'RICEBRAN', 'BLEND')
('PALM', 'BLEND', 'RICEBRAN', 'SOYA')
('PALM', 'BLEND', 'SOYA', 'RICEBRAN')
('PALM', 'RICEBRAN', 'BLEND', 'SOYA')
('PALM', 'RICEBRAN', 'SOYA', 'BLEND')
('PALM', 'SOYA', 'BLEND', 'RICEBRAN')
('PALM', 'SOYA', 'RICEBRAN', 'BLEND')

**Changeover_cost** = ('BLEND', 'RICEBRAN')  :  4401
('BLEND', 'SOYA')  :  4401
('BLEND', 'PALM')  :  4401
('RICEBRAN', 'BLEND')  :  4401
('RICEBRAN', 'SOYA')  :  5401
('RICEBRAN', 'PALM')  :  1499
('SOYA', 'BLEND')  :  3401
('SOYA', 'RICEBRAN')  :  3401
('SOYA', 'PALM')  :  1099
('PALM', 'BLEND')  :  4401
('PALM', 'RICEBRAN')  :  2901
('PALM', 'SOYA')  :  2901
('BLEND', 'RICEBRAN', 'SOYA')  :  9802
('BLEND', 'RICEBRAN', 'PALM')  :  5900
('BLEND', 'SOYA', 'RICEBRAN')  :  7802
('BLEND', 'SOYA', 'PALM')  :  5500
('BLEND', 'PALM', 'RICEBRAN')  :  7302
('BLEND', 'PALM', 'SOYA')  :  7302
('RICEBRAN', 'BLEND', 'SOYA')  :  8802
('RICEBRAN', 'BLEND', 'PALM')  :  8802
('RICEBRAN', 'SOYA', 'BLEND')  :  8802
('RICEBRAN', 'SOYA', 'PALM')  :  6500
('RICEBRAN', 'PALM', 'BLEND')  :  5900
('RICEBRAN', 'PALM', 'SOYA')  :  4400
('SOYA', 'BLEND', 'RICEBRAN')  :  7802
('SOYA', 'BLEND', 'PALM')  :  7802
('SOYA', 'RICEBRAN', 'BLEND')  :  7802
('SOYA', 'RICEBRAN', 'PALM')  :  4900
('SOYA', 'PALM', 'BLEND')  :  5500
('SOYA', 'PALM', 'RICEBRAN')  :  4000
('PALM', 'BLEND', 'RICEBRAN')  :  8802
('PALM', 'BLEND', 'SOYA')  :  8802
('PALM', 'RICEBRAN', 'BLEND')  :  7302
('PALM', 'RICEBRAN', 'SOYA')  :  8302
('PALM', 'SOYA', 'BLEND')  :  6302
('PALM', 'SOYA', 'RICEBRAN')  :  6302
('BLEND', 'RICEBRAN', 'SOYA', 'PALM')  :  10901
('BLEND', 'RICEBRAN', 'PALM', 'SOYA')  :  8801
('BLEND', 'SOYA', 'RICEBRAN', 'PALM')  :  9301
('BLEND', 'SOYA', 'PALM', 'RICEBRAN')  :  8401
('BLEND', 'PALM', 'RICEBRAN', 'SOYA')  :  12703
('BLEND', 'PALM', 'SOYA', 'RICEBRAN')  :  10703
('RICEBRAN', 'BLEND', 'SOYA', 'PALM')  :  9901
('RICEBRAN', 'BLEND', 'PALM', 'SOYA')  :  11703
('RICEBRAN', 'SOYA', 'BLEND', 'PALM')  :  13203
('RICEBRAN', 'SOYA', 'PALM', 'BLEND')  :  10901
('RICEBRAN', 'PALM', 'BLEND', 'SOYA')  :  10301
('RICEBRAN', 'PALM', 'SOYA', 'BLEND')  :  7801
('SOYA', 'BLEND', 'RICEBRAN', 'PALM')  :  9301
('SOYA', 'BLEND', 'PALM', 'RICEBRAN')  :  10703
('SOYA', 'RICEBRAN', 'BLEND', 'PALM')  :  12203
('SOYA', 'RICEBRAN', 'PALM', 'BLEND')  :  9301
('SOYA', 'PALM', 'BLEND', 'RICEBRAN')  :  9901
('SOYA', 'PALM', 'RICEBRAN', 'BLEND')  :  8401
('PALM', 'BLEND', 'RICEBRAN', 'SOYA')  :  14203
('PALM', 'BLEND', 'SOYA', 'RICEBRAN')  :  12203
('PALM', 'RICEBRAN', 'BLEND', 'SOYA')  :  11703
('PALM', 'RICEBRAN', 'SOYA', 'BLEND')  :  11703
('PALM', 'SOYA', 'BLEND', 'RICEBRAN')  :  10703
('PALM', 'SOYA', 'RICEBRAN', 'BLEND')  :  10703

#List of sequences which start with a given oil

**First** = {('BLEND', 'SOYA') : 'BLEND', 
         ('BLEND', 'PALM') : 'BLEND',
         ('BLEND', 'RICEBRAN', 'SOYA') : 'BLEND', 
         ....., 
         ('BLEND', 'RICEBRAN', 'SOYA', 'PALM') : 'BLEND',
         ('PALM', 'BLEND'), ('PALM', 'RICEBRAN') : 'PALM',
         ('PALM', 'BLEND', 'RICEBRAN') : 'PALM',
         ....., 
         ('PALM', 'SOYA', 'RICEBRAN', 'BLEND') : 'PALM',
         .....
         .....}


#List of sequences which end with a given oil

**End** = {('RICEBRAN', 'BLEND') : 'BLEND', 
       ('SOYA', 'BLEND'), ('SOYA', 'PALM', 'BLEND') : 'SOYA',
       .....,
       ('PALM', 'SOYA', 'RICEBRAN', 'BLEND') : 'PALM',
       ('BLEND', 'PALM'),('SOYA', 'PALM') : 'BLEND',
       ('SOYA', 'BLEND', 'PALM') : 'PALM',
       .....,
       ('BLEND', 'RICEBRAN', 'SOYA', 'PALM') : 'PALM',
       .....,
       .....}

#Selection of sequence for a month

**select** = {sequence : 0}

#Initial Closing Inventory

Q(month[0],product) == I(month[0],product) + demand ([month[0],product)

#Constraint on Monthly Closing Inventory

Q(month,product) + I(month-1,product) ==I(month[0],product) + demand (month, product)

#Constraint to Manufacture only when the product is included in the sequence

select(month,sequence) * Q(month,product element of sequence) == Q(month,product element of sequence)

#Constraint to Select only 1 sequence for a month

SUM(select(month,sequence)) for each month == 1

#Constraint for Changeover continuing across months. This logic is not included in the python.

First(month, selected sequence) == End(month+1, selected sequence) 

#Objective Function

objective = Minimize(select(month,sequence) * changeover_cost(sequence) + I(month,product) * Invholding cost
