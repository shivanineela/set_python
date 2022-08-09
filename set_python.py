# a={}
# print(a,type(a))  # {} <class 'dict'>

# a={1,4.7,"hi",("hi",2)}
# print(a,type(a))  # <class 'set'>
# b={1,4.7,"hi",("hi",2),{5}}
# print(b,type(b))
# c={1,4.7,"hi",("hi",2),[5]}
# print(c,type(c))

# m={20,25,30,35}
# print(m[2])

"""Set Methods"""

# a={4,7,8}
# b='hey',1,3,5
# a.add(b)
# print(a)
# b.add(a)
# print(b)
# a={4,7,8}
# b={'hey',1,3,5}
# a.add(b)
# print(a)

# b={1,8,5}
# b.clear()
# print(b)  # set()

# a={1,2,3}; b={4,3,3,6}; c={10,15,20}; d={1,4,7}
# print(a.intersection(b))
# print(a.intersection(c))
# print(a.intersection(d))
# print(b.intersection(c))

# a={'hi',3,4,5}
# b={'hello',5,6,7}
# c={'hey',7,8,9}
# print(a.union(b))
# print(b.union(a))
# print(a.union(c))

# a={1,2,3}
# b={3,4,5}
# c={4,3,6}
# a.update(b)  #{1,2,3,4,5}
# a.update(c)  #{1,2,3,4,5,6}
# print(a)

# a={5,10,15,20}
# b={15,20,25,30}
# print(a.difference(b))
# print(b.difference(a))
# print(a-b)
# print(b-a)

# d={45,47,79,74,45}
# d.discard(79)
# print(d)
# d.discard(45)
# print(d)

# c={4,89,67,5}
# c.pop()
# print(c)

# a={1,2,3,4}
# b={5,6,7}
# c={4,5,6}
# print('Are a and b disjoint?',a.isdisjoint(b))
# print('Are a and c disjoint?',a.isdisjoint(c))
# print('Are b and c disjoint?',b.isdisjoint(c))

# a={1,2,3}
# b={1,2,3,4,5}
# c={1,2,4,5}
# print(a.issubset(b))
# print(b.issubset(a))
# print(a.issubset(c))
# print(c.issubset(b))

"""Remove"""
# a={8,9,10,12,15}
# a.remove(12)
# print(a)
# print(a.remove(14))

"""issuperset"""
# a={8,9,10,12,14}
# b={10,14,15,1}
# print(a.issuperset(b))
# a={8,9,10,12,14}
# b={8,9,10}
# print(a.issuperset(b))
# print(b.issuperset(a))