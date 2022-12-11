import dataSet1
import dataSet2

while True:
    i = 0
    choice = input("Would you like to use the dataset of characters from:\n1- The Office\n2- Marvel\n")
    while choice != "1" and choice != "2":
        choice = input("Please enter 1 for Yes or 2 for No\n")
    if choice == "1":
        data = dataSet1
        print("Think of a main character from 'The Office' and I will try and guess it \nFor your answer please select 1 or 2, based on what answer best fits your character")
    else:
        data = dataSet2
        print("Pick a character out of:\nThor\nCaptain America\nIronman\nHulk\nand I will try and guess it \nFor your answer please select 1 or 2, based on what answer best fits your character")
    for node in data.graph.nodes:
        if data.graph.nodes[i].name == "I WIN":
            print(data.graph.nodes[i].name)
            break
        print(data.graph.nodes[i].name)
        for edge in data.graph.nodes[i].edges:
            print(edge.answer)
        answer = input()
        while answer != '1' and answer != '2':
            answer = input("Please enter 1 for Yes or 2 for No\n")
        test = 0
        if int(answer) == 1:
            test = data.graph.nodes[i].edges[0].node
            i = test.key
            continue
        test = data.graph.nodes[i].edges[1].node
        i = test.key
    answer = input("\n\nWant to play again\n1- Yes\n2- No thanks\n")
    while int(answer) != 1 and int(answer) != 2:
        answer = input("Please enter 1 for Yes or 2 for No\n")
    if int(answer) == 1:
        print("Please pick a new character")
        i = 0
    else:
        print("Thanks for playing!")
        break

