s = [x for x in range(2, 100) if len([y for y in range(2,x) if x % y == 0]) == 0]
print(s)

f = [(seq.append(seq[i - 1] + seq[i - 1]), seq[i - 2])[1] for seq in [[0, 1]]]
