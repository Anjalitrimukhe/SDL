
A=set([1,2,3,4])
print (A)

len (A)
print(2 in A)

print(5 in A)

B=set([2,4,6,8])
print (B)

print ("\n Set union : ")
c=A|B
print (c)

print("\n Using function : ")
print(A.union(B))

print ("\n Set intersection : ")
d=A & B

print (d)

print("\n Using function : ")
print(A.intersection(B))

print("\n Set difference : ")
c=A-B

print(c)

print("\n Using function : ")
print(A.difference(B))

print("\n Set symmetric difference : ")
d=A^B

print(d)


