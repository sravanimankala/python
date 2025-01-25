#1.set intersection
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.intersection(set2))

#2.set union
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2))

#3.set difference
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.difference(set2))

#4.set symmetric difference
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.symmetric_difference(set2))

#5.set membership test
my_set={1,2,3,4,5}
print([i in my_set for i in[3]])


#exercise
set_1={1,3,5,7,9}
set_2={2,4,6,8,9}
print(set_1.intersection(set_2))
print(set_1.union(set_2))
print(set_1.difference(set_2))
print(set_1.symmetric_difference(set_2))