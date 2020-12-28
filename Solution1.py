from logic import TruthTable

myTable = TruthTable(['a'], ['-a'])
myTable.display()
print("")

myTable = TruthTable(['a','b'], ['a and b'])
myTable.display()
print("")

myTable = TruthTable(['a','b'], ['a or b'])
myTable.display()
print("")

myTable = TruthTable(['a','b'], ['a -> b'])
myTable.display()
print("")

myTable = TruthTable(['a','b'], ['a <-> b'])
myTable.display()
print("")


