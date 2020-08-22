
def add(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] == '1' or b[i] == '1':
            c += 1
    return c



# Complete the acmTeam function below.
def acmTeam(topic):
    a = []
    for i in range(len(topic) - 1):
        for j in range(i + 1, len(topic)):
            a.append(add(topic[i], topic[j]))
    x = max(a)
    return [x, a.count(x)]

x = "10101"
y = "11110"
z = "00010"
bitString = [x, y, z]

a = []


print(acmTeam(bitString))
