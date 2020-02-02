import math

print("1A")
print("--------------------------------------------------------")

names = ["Ditlev", "Rasmus", "Herlev", "Henning"]
result = []
print(names)
for name in names:

    if name[0] == 'H':
        print(name)

print(result)
print("--------------------------------------------------------")
print("1B")
print("--------------------------------------------------------")
numList = range(0,100)

def power(numList):
    return [ x**3 for x in numList ]

print(power(numList))

print("--------------------------------------------------------")
print("1c")
print("--------------------------------------------------------")
names = ["Ditlev", "Rasmus", "Herlev", "Henning"]
res = []
for name in names:
    res.append((len(name), name))
print(res)

print("--------------------------------------------------------")
print("1D")
print("--------------------------------------------------------")
string = "qwelqjke123123awæsljqr"


for c in string:
    if c.isdigit():
        print(c)

print("--------------------------------------------------------")
print("E")
print("--------------------------------------------------------")

print("--------------------------------------------------------")
print("2 Dictionarys")
print("--------------------------------------------------------")

name_list = ["Peter", "Ingolf", "Mads"]
res = [];
for name in name_list:
    res.append((name, len(name)));
print(res);

numbers = [(19, math.sqrt(19)), (1112, math.sqrt(1112)), (123, math.sqrt(123))]
print(numbers);




print("--------------------------------------------------------")
print("Dice it up")
print("--------------------------------------------------------")

dices = set((x,y) for x in range(1,6) for y in range(1,6))

res = [];
for die in dices:
    res.append((die, (float(die[1])/6) * (float(die[1])/6)*100));
print(res);
