from logic import TruthTable

prop1 = input("Enter proposition 1: ")
prop2 = input("Enter proposition 2: ")
print(" ")

myTable = TruthTable(['p','q'], [prop1, prop2])
myTable.display()

mylist = myTable.table

equivalent = 1
for row in mylist:
    last_element = row[-1]

    if(last_element[0] != last_element[1]):
        equivalent = 0

if(equivalent == 1):
    print("The propositions are equivalent.")
else:
    print("The propositions are not equivalent")
