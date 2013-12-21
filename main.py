import csv , os , random
from termcolor import colored , cprint

problems = []
csvfile = open("words.csv")
for row in csv.reader(csvfile):
    problems.append(row)
csvfile.close()
random.shuffle(problems)

for problem in problems:
    chance = 2
    while chance > 0:
        print "\nNo."+problem[0]
        os.system( "say "+ problem[1] )
        reply = raw_input(">")
        if reply == (problem[1]):
            os.system( "say say kai death" )
            cprint( problem[1] +" "+ problem[2] , "white" , "on_blue")
            break
        else:
            os.system( "say chee guide math" )
            chance -= 1
            cprint(" incorrect :( " , "white" , "on_grey")
    else:
        cprint( "Answer " + problem[1] +" "+ problem[2] , "white","on_red")
        os.system( "say say cay wa ")
        os.system( "say "+ problem[1] )
        os.system( "say death ")
    os.system( "say next problem" )
