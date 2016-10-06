print(2 ** 16)

print(2 // 5)

print("spam" + "eggs")

S = "ham"
print("eggs" + S)

print(S * 5)

print(S[:0])

print("green %s and %s" % ("eggs", S))

print('green {0} and {2}'.format('eggs', S, 'asparagus'))

print(('x',)[0])

print(('x', 'y')[1])

L = [1, 2, 3] + [4, 5, 6]
print(L, L[:], L[:0], L[-2], L[-2:])

print(([1, 2, 3] + [4, 5, 6])[2:4])

print([L[2], L[3]])

L.reverse()
print(L)

L.sort()
print(L)

print(L.index(2))

print({'a': 1, 'b': 2}['b'])

D = {'x': 1, 'y': 2, 'z': 3}
D['w'] = 0
print(D['w'] + D['x'])

D[(1, 2, 3)] = 4
print(list(D.keys()), list(D.values()), (1, 2, 3) in D)
