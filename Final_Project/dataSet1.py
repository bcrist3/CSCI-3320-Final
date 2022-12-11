import main
# Dataset 1 consists of characters from the office

# 1 = Left and 2 = Right
# So left121 = left right left of the node 'left'
start = main.Node("Is your character male?", 0)
left = main.Node("Was your character ever a manager of the scranton branch?", 1)
left1 = main.Node("Was your character a main character in the pilot episode?", 2)
left11 = main.Node("Was your character in the sales department for most of the show?", 3)
Michael = main.Node("Is your character Michael", 4)
left111 = main.Node("Does your character own a farm?", 5)
Dwight = main.Node("Is your character Dwight?", 6)
Jim = main.Node("Is your character Jim?", 7)
left12 = main.Node("Did your character ever work in the sales department?", 8)
Andy = main.Node("Is your character Andy?", 9)
left122 = main.Node("Did your character ever fake his own death?", 10)
Creed = main.Node("Is your character Creed?", 11)
Darryl = main.Node("Is your character Darryl?", 12)
left2 = main.Node("Was your character ever in the accounting department?", 13)
left21 = main.Node("Did your character win a World Series of Poker for No-Limit Deuce-Seven Draw in 2002", 14)
Kevin = main.Node("Is your character Kevin?", 15)
Oscar = main.Node("Is your character Oscar?", 16)
left22 = main.Node("Did your character work in Human Resources?", 17)
Toby = main.Node("Is your character Toby?", 18)
left222 = main.Node("Did your character create Wuphf?", 19)
Ryan = main.Node("Is your character Ryan?", 20)
Stanley = main.Node("Is your character Stanley?", 21)

right = main.Node("Did your character get married to someone that worked in the office building during the show?", 22)
right1 = main.Node("Did your character ever work in the sales department?", 23)
right11 = main.Node("Is your character married to Bob Vance of Vance Refrigeration?", 24)
Phyllis = main.Node("Is your character Phyllis?", 25)
Pam = main.Node("Is your character Pam?", 26)
right12 = main.Node("Did your character ever get kidnapped by Mose?", 27)
Angela = main.Node("Is your character Angela?", 28)
Holly = main.Node("Is your character Holly?", 29)
right2 = main.Node("Is your character's first name Kelly?", 30)
right21 = main.Node("Does your character go by Erin?", 31)
Erin = main.Node("Is your character Erin?", 32)
Kelly = main.Node("Is your character Kelly?", 33)
right22 = main.Node("Has your character ever shaved their head?", 34)
Maredith = main.Node("Is your character Maredith?", 35)
Jan = main.Node("Is your character Jan?", 36)
correct = main.Node("I WIN", 37)

start.addEdge(main.WeightedEdge(left, 1, "1- Yes they are male"))
start.addEdge(main.WeightedEdge(right, 1, "2- No they are not male"))
left.addEdge(main.WeightedEdge(left1, 1, "1- Yes they were a of the Scranton branch manager"))
left.addEdge(main.WeightedEdge(left2, 1, "2- No they were not a Scranton branch manager"))
left1.addEdge(main.WeightedEdge(left11, 1, "1- Yes they were a main character in the pilot episode"))
left1.addEdge(main.WeightedEdge(left12, 1, "2- No they were not a main character in the pilot episode"))
left12.addEdge(main.WeightedEdge(Andy, 1, "1- Yes they worked in sales"))
left12.addEdge(main.WeightedEdge(left122, 1, "2- No they did not work in sales"))
Andy.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Andy"))
Andy.addEdge(main.WeightedEdge(left, 1, "2- No my character is not Andy"))
left122.addEdge(main.WeightedEdge(Creed, 1, "1- Yes my character faked his own death"))
left122.addEdge(main.WeightedEdge(Darryl, 1, "2- No my character did not fake his own death"))
Creed.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Creed"))
Creed.addEdge(main.WeightedEdge(left, 1, "2- No my character is not Creed"))
Darryl.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Darryl"))
Darryl.addEdge(main.WeightedEdge(left, 1, "2- No my character is not Darryl"))
left11.addEdge(main.WeightedEdge(left111, 1, "1- Yes they were in sales for most of the show"))
left11.addEdge(main.WeightedEdge(Michael, 1, "2- No they were not in sales for most of the show"))
Michael.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Michael"))
Michael.addEdge(main.WeightedEdge(left, 1, "2- No my character is not Michael"))
left111.addEdge(main.WeightedEdge(Dwight, 1, "1- Yes my character owns a farm"))
left111.addEdge(main.WeightedEdge(Jim, 1, "2- No my character does not own a farm"))
Dwight.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Dwight"))
Dwight.addEdge(main.WeightedEdge(left, 1, "2- No my character is not Dwight"))
Jim.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Jim"))
Jim.addEdge(main.WeightedEdge(left, 1, "2- No my character is not Jim"))
left2.addEdge(main.WeightedEdge(left21, 1, "1- Yes my character is in the accounting department"))
left2.addEdge(main.WeightedEdge(left22, 1, "2- No my character is not in the accounting department"))
left21.addEdge(main.WeightedEdge(Kevin, 1, "1- Yes my character won a World Series of Poker for No-Limit Deuce-Seven Draw in 2002"))
left21.addEdge(main.WeightedEdge(Oscar, 1, "2- No my character did not win win a World Series of Poker for No-Limit Deuce-Seven Draw in 2002"))
Kevin.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Kevin"))
Kevin.addEdge(main.WeightedEdge(left, 1, "2- My character is not Kevin"))
Oscar.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Oscar"))
Oscar.addEdge(main.WeightedEdge(left, 1, "2- No my character is not Oscar"))
left22.addEdge(main.WeightedEdge(Toby, 1, "1- Yes my character worked in HR"))
left22.addEdge(main.WeightedEdge(left222, 1, "2- No my character did not work in HR"))
Toby.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Toby"))
Toby.addEdge(main.WeightedEdge(left, 1, "2- No my character is not Toby"))
left222.addEdge(main.WeightedEdge(Ryan, 1, "1- Yes my character created Wuphf"))
left222.addEdge(main.WeightedEdge(Stanley, 1, "2- No my character did not create Wuphf"))
Ryan.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Ryan"))
Ryan.addEdge(main.WeightedEdge(left, 1, "2- No my character is not Ryan"))
Stanley.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Stanley"))
Stanley.addEdge(main.WeightedEdge(left, 1, "2- No my character is not Stanley"))
right.addEdge(main.WeightedEdge(right1, 1, "1- Yes my character got married to someone in the office building"))
right.addEdge(main.WeightedEdge(right2, 1, "2- No my character did not get married to someone in the office building"))
right1.addEdge(main.WeightedEdge(right11, 1, "1- Yes my character was in sales at some point during the show"))
right1.addEdge(main.WeightedEdge(right12, 1, "2- Mo my character was never in sales during the show"))
right11.addEdge(main.WeightedEdge(Phyllis, 1, "1- Yes my character is married to Bob Vance of Vance Refrigeration"))
right11.addEdge(main.WeightedEdge(Pam, 1, "2- No my character is not married to Bob Vance of Vance Refrigeration"))
Phyllis.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Phyllis"))
Phyllis.addEdge(main.WeightedEdge(right, 1, "2- No my character is not Phyllis"))
Pam.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Pam"))
Pam.addEdge(main.WeightedEdge(right, 1, "2- No my character is not Pam"))
right12.addEdge(main.WeightedEdge(Angela, 1, "1- Yes my character was kidnapped by Mose"))
right12.addEdge(main.WeightedEdge(Holly, 1, "2- No my character was not kidnapped by Mose"))
Angela.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Angela"))
Angela.addEdge(main.WeightedEdge(right, 1, "2- No my character is not Angela"))
Holly.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Holly"))
Holly.addEdge(main.WeightedEdge(right, 1, "2- No my character is not Holly"))
right2.addEdge(main.WeightedEdge(right21, 1, "1- Yes my character's first name is Kelly"))
right2.addEdge(main.WeightedEdge(right22, 1, "2- No my character's first name is not Kelly"))
right21.addEdge(main.WeightedEdge(Erin, 1, "1- Yes my character went by the name Erin"))
right21.addEdge(main.WeightedEdge(Kelly, 1, "2- No my character did not go by the name Erin"))
Erin.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Erin"))
Erin.addEdge(main.WeightedEdge(right, 1, "2- No my character is not Erin"))
Kelly.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Kelly"))
Kelly.addEdge(main.WeightedEdge(right, 1, "2- No my character is not Kelly"))
right22.addEdge(main.WeightedEdge(Maredith, 1, "1- Yes my character shaved their head"))
right22.addEdge(main.WeightedEdge(Jan, 1, "2- No my character did not shave their head"))
Maredith.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Maredith"))
Maredith.addEdge(main.WeightedEdge(right, 1, "2- No my character is not Maredith"))
Jan.addEdge(main.WeightedEdge(correct, 1, "1- Yes my character is Jan"))
Jan.addEdge(main.WeightedEdge(right, 1, "2- No my character is not Jan"))
"""
start.addEdge((left))
start.addEdge(main.WeightedEdge(right,1,))
left.edges += [eMainManager, eNotMainManager]
left1.edges += [eManagerSales, eManagerNotSales]
left11.edges += [eSalesFarm, eSalesNotFarm]
left111.edges += [eFarmDwight, eFarmJim]
Dwight.edges += [eDwightRight, eDwightWrong]
Jim.edges += [eJimRight, eJimWrong]
Michael.edges += [eMichaelRight, eMichaelWrong]
left12.edges += [eSalesAndy, eSalesDeath]
Andy.edges += [eAndyRight, eAndyWrong]
left122.edges += [eDeathCreed, eDeathDarryl]
Creed.edges += [eCreedRight, eCreedWrong]
Darryl.edges += [eDarrylRight, eDarrylWrong]
left2.edges += [eAccountGamble, eAccountHR]
left21.edges += [eGambleKevin, eGambleOscar]
Kevin.edges += [eKevinRight, eKevinWrong]
Oscar.edges += [eOscarRight, eOscarWrong]
left22.edges += [eHRToby, eHRWuphf]
Toby.edges += [eTobyRight, eTobyWrong]
left222.edges += [eWuphfRyan, eWuphfStanley]
Ryan.edges += [eRyanRight, eRyanWrong]
Stanley.edges += [eStanleyRight, eStanleyWrong]
right.edges += [eMarriedSales, eMarriedName]
right1.edges += [eSalesBob, eSalesMose]
right2.edges += [eNameMiddle, eNameHead]
right11.edges += [eBobPhyllis, eBobPam]
right12.edges += [eMoseAngela, eMoseHolly]
right21.edges += [eMiddleErin, eMiddleKelly]
right22.edges += [eHeadMaredith, eHeadJan]
Phyllis.edges += [ePhyllisRight, ePhyllisWrong]
Pam.edges += [ePamRight, ePamWrong]
Holly.edges += [eHollyRight, eHollyWrong]
Angela.edges += [eAngelaRight, eAngelaWrong]
Kelly.edges += [eKellyRight, eKellyWrong]
Erin.edges += [eErinRight, eErinWrong]
Maredith.edges += [eMaredithRight, eMaredithWrong]
Jan.edges += [eJanRight, eJanWrong]
"""

graph = main.Graph([start, left, left1, left11, Michael, left111, Dwight, Jim, left12, Andy, left122, Creed, Darryl, left2, left21, Kevin, Oscar, left22, Toby, left222, Ryan, Stanley, right, right1, right11, Phyllis, Pam, right12, Angela, Holly, right2, right21, Erin, Kelly, right22, Maredith, Jan, correct])
graph2 = main.Graph([start, left, left1, left11, Michael, left111, Dwight, Jim, left12, Andy, left122, Creed, Darryl, left2, left21, Kevin, Oscar, left22, Toby, left222, Ryan, Stanley, right, right1, right11, Phyllis, Pam, right12, Angela, Holly, right2, right21, Erin, Kelly, right22, Maredith, Jan, correct])

dictionary = {start: 0, left:1000, left1:1000, left11:1000, Michael:1000, left111:1000, Dwight:1000, Jim:1000, left12:1000, Andy:1000, left122:1000, Creed:1000, Darryl:1000, left2:1000, left21:1000, Kevin:1000, Oscar:1000, left22:1000, Toby:1000, left222:1000, Ryan:1000, Stanley:1000, right:1000, right1:1000, right11:1000, Phyllis:1000, Pam:1000, right12:1000, Angela:1000, Holly:1000, right2:1000, right21:1000, Erin:1000, Kelly:1000, right22:1000, Maredith:1000, Jan:1000, correct:1000}
finalizedNodes = [start]