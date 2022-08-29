def fiblst(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result += [a]
        a, b = b, a+b
    return result

fib = fiblst(1000)
evenlist = []
for i in fib:
    if i % 2 == 0:
        evenlist.append(i)
    if evenlist[-1] > 4000000:
        evenlist.remove(evenlist[-1])
        break

evenlist.remove(0) # entfernt 0 aus der Liste
print(evenlist)
print(sum(evenlist))
