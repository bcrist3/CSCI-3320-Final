import dataSet1
import dataSet2

choice = input("Would you like to use the dataset of characters from:\n1- The Office\n2- Marvel\n")
while choice != "1" and choice != "2":
    choice = input("Please enter 1 for Yes or 2 for No\n")
if choice == "1":
    data = dataSet1
else:
    data = dataSet2
madeChange = True
while madeChange:
    madeChange = False
    base = data.finalizedNodes[-1]
    for node in data.graph.nodes:
        if node in data.finalizedNodes:
            continue
        if base.hasEdgeTo(node):
            edge = base.getEdgeTo(node)
            weight = edge.weight
            if weight < data.dictionary[node]:
                data.dictionary[node] = weight + data.dictionary[base]
    shortest = 100
    shortestNode = None
    for node in data.graph.nodes:
        if node in data.finalizedNodes:
            continue
        if data.dictionary[node] < shortest:
            shortest = data.dictionary[node]
            shortestNode = node
    if shortestNode is not None:
        madeChange = True
        data.finalizedNodes += [shortestNode]
print("The least amount of guesses possible is: " + str(data.dictionary[data.correct]))