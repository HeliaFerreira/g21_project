# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:48:26 2026

@author: marti
"""
# -*- coding: utf-8 -*-
"""
Created on Wed May 13 09:54:56 2026

@author: hsff2
"""

from classes.curator import Curator
from classes.exhibit import Exhibit 
from classes.museum import Museum
from classes.specialty import Specialty
from classes.visitors import Visitors 


# Reads the classes info
Curator.read('data/database.db')
Exhibit.read('data/database.db')
Museum.read('data/database.db')
Specialty.read('data/database.db') 
Visitors.read('data/database.db')


#creates 3 museums

m1 = Museum(501, "M1")
m2 = Museum.from_string("502;M2")
m3 = Museum(503,"M3")

if m1.id not in Museum.lst:
    Museum.insert(m1.id)
if m2.id not in Museum.lst:
    Museum.insert(m2.id)
if m3.id not in Museum.lst:
    Museum.insert(m3.id)

for id in Museum.lst:
    print(Museum.obj[id])

#creates 2 specialties 
s1 = Specialty(1,"Renascimento")
s2 = Specialty.from_string("2;Surrealismo")
if s1.id not in Specialty.lst:
    Specialty.insert(s1.id)
if s2.id not in Specialty.lst:    
    Specialty.insert(s2.id)

for id in Specialty.lst:
    print(Specialty.obj[id]) 

#creates 2 exhibits 

e1 = Exhibit(1001,"2025-02-11","Creation","cat") 
e2 = Exhibit.from_string("1002;2024-02-11;Patience;Saint")

if e1.id not in Exhibit.lst:
    Exhibit.insert(e1.id)
if e2.id not in Exhibit.lst:
    Exhibit.insert(e2.id)
for id in Exhibit.lst:
    print(Exhibit.obj[id]) 

#creates a curator 
for id in Curator.lst:
    print(Curator.obj[id]) 
    
#creates a curator 
c1 = Curator(2001, "Curador Principal Teste", 501, 1) 
c2 = Curator.from_string("2002;Curador Assistente Teste;502;2")

if c1.id not in Curator.lst:
    Curator.insert(c1.id)
if c2.id not in Curator.lst:
    Curator.insert(c2.id)

#creates 2 visitors 
v1 = Visitors(9001, 1001, 501, "2025-12-31", 500)
v2 = Visitors.from_string("9002;1002;502;2025-12-31;850")

if v1.id not in Visitors.lst:
    Visitors.insert(v1.id)
if v2.id not in Visitors.lst:
    Visitors.insert(v2.id)

for id in Visitors.lst:
    print(Visitors.obj[id])
    

"""
if len(Customer.lst) == 0:
    c1 = Customer(0, 'Joaquim', 'Rua do Joaquim', '91934567')
    Customer.insert(c1.id)
# Creates two orders
if len(CustomerOrder.lst) == 0:
    o1 = CustomerOrder(0, '2021-03-20', 1)
    o2 = CustomerOrder(0, '2021-03-21', 1)
    CustomerOrder.insert(o1.id)
    CustomerOrder.insert(o2.id)
# Creates product orders for order 1 and 2
if len(OrderProduct.lst) == 0:
    op1 = OrderProduct(0, 1, 2, 5, 50)
    op2 = OrderProduct(0,1,3, 10, 1000)
    op3 = OrderProduct(0,2,1, 2, 200)
    print(op1._id, op1._order_id, op1._product_id, op1._quantity, op1._price)
    OrderProduct.insert(op1.id)
    OrderProduct.insert(op2.id)
    OrderProduct.insert(op3.id)
# Select the products ordered in order 1
order = OrderProduct.getlines('order_id',1)
print('\nOrderProduct codes for order 1:', order)
print('Ordered products in order 1:')
for id in order:
    product_id = OrderProduct.obj[id].product_id
    print(Product.obj[product_id])
"""