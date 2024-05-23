
class IPL:

    no_teams = 10

    def __init__(self,year,winner):

        self.year = year
        self.winner = winner

    def ipl_win(self):

        print("""list of teams according to points are:
                1)RCB
                2)CSK
                3)MI
                4)SRH
                5)GT
                6)LKN
                7)PBKS
                8)RR
                9)KKR
                10)DD
                """)

        print(f"In year {self.year} the IPL cup winner team is {self.winner}")


year= int(input("enter the year"))
team = input("enter the team name")
rest = IPL(year,team)
rest.ipl_win()







