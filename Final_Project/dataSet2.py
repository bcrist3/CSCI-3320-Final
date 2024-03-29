import main
# Dataset 2 consists of Ironman, Captain America, Thor, and Hulk

start = main.Node("Did your character use all the infinity stones at once?", 0)
gamma = main.Node("Did your character do research on gamma radiation?", 1)
lightning = main.Node("Was your character the Norse god of lightning?", 2)
Hulk = main.Node("Is your character Bruce Banner, aka The Hulk?", 3)
Ironman = main.Node("Is your character Tony Stark, aka Ironman?", 4)
Thor = main.Node("Is your character Thor Odinson, aka Thor?", 5)
Captain = main.Node("Is your character Steve Rodgers, aka Captain America?", 6)
correct = main.Node("I WIN", 7)

start.addEdge(main.WeightedEdge(gamma, 1, "1- Yes my character used all the infinity stones at once"))
start.addEdge(main.WeightedEdge(lightning, 1, "2- No my character did not use all the infinity stones at once"))
gamma.addEdge(main.WeightedEdge(Hulk, 1, "1- Yes my character did research on gamma radiation"))
gamma.addEdge(main.WeightedEdge(Ironman, 1, "2- No my character did not do research on gamma radiation"))
lightning.addEdge(main.WeightedEdge(Thor, 1, "1- Yes my character is the Norse god of lightning"))
lightning.addEdge(main.WeightedEdge(Captain, 1, "2- No my character is not the Norse god of lightning"))
Hulk.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Bruce Banner aka The Hulk"))
Hulk.addEdge(main.WeightedEdge(start, 1, "2- No my character is not Bruce Banner aka The Hulk"))
Ironman.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Tony Stark aka Ironman"))
Ironman.addEdge(main.WeightedEdge(start, 1, "2- No my character is not Tony Stark aka Ironman"))
Thor.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Thor Odinson, aka Thor"))
Thor.addEdge(main.WeightedEdge(start, 1, "2- No my character is not Thor Odinson, aka Thor"))
Captain.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Steve Rodgers, aka Captain America"))
Captain.addEdge(main.WeightedEdge(start, 1, "2- No my character is not Steve Rodgers, aka Captain America"))

graph = main.Graph([start, gamma, lightning, Hulk, Ironman, Thor, Captain, correct])
graph2 = main.Graph([start, gamma, lightning, Hulk, Ironman, Thor, Captain, correct])

dictionary = {start: 0, gamma: 1000, lightning: 1000, Hulk: 1000, Ironman: 1000, Thor: 1000, Captain: 1000, correct: 1000}
finalizedNodes = [start]
