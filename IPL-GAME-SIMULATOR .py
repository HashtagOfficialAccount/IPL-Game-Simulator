#import time and random module 
import random
import time

#teams and options
teams = ["MI","CSK","SRH","KKR","PBKS","DC","RR","RCB"]
options = ["Bowl","Bat"]

#option to bat or bowl
choice = random.choice(options)

#picks teams to play
team1 = random.choice(teams)
team2 = random.choice(teams)

#list of both the teams playing
teams_playing = [team1,team2]

#if both the teams are same, the match is canceled, else the code is run
if team1 == team2:
    print("The Match was Canceled due to rain.")
else:
    print(team1," vs ",team2)
    time.sleep(2)
    toss_winner = random.choice(teams_playing)
    print(toss_winner, "won by the toss and chose to",choice)
    time.sleep(2)
    if choice == "Bat":
        cheese = random.randint(90,220)
        print(toss_winner,"scored",cheese,"runs")
        time.sleep(2)
        if team1 == toss_winner:
            a = random.randint(90, 220)
            print(team2,"scored",a,"runs")
        if team2 == toss_winner:
            b = random.randint(90, 220)
            print(team1, "scored",b, "runs")
    if choice == "Bowl":
        if team1 == toss_winner:
            c = random.randint(90, 220)
            m = random.randint(90, 220)
            pie = random.randint(90, 220)
            print(team2,"scored",c,"runs")
            time.sleep(2)
            print(team1, "scored", m, "runs")

        if team2 == toss_winner:
            d = random.randint(90, 220)
            k = random.randint(90, 220)
            print(team1, "scored",d, "runs")
            time.sleep(2)
            print(team2,"scored",k,"runs")



