# Operações em elementos de uma lista

#um jeito
l=[10,20,30,40,50]

l= [i*2 for i in l]

print(l)



# outro jeito
m = [1,2,3,4,5]

for i in range(len(l)):
    m[i]=m[i]*2

print(m)