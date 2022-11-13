
# Online Python - IDE, Editor, Compiler, Interpreter
class Match:
    def calculate_win(self, n, *T):
        global Winsum
        global WinTeamcount
        global Losssum
        global LossTeamcount



        #Two consecutive losses 
        for i in range (2,8-n):
            if n == 2:
                if T[i] == 1:
                    if T[i] == T[i+1]:
                        Winsum += T[1]
                        WinTeamcount += 1
                        print(T[0], "has", n ,"consecutive Win")
                        break
        for i in range (2,8-n):
            if n ==2:
                if T[i] == 0:
                    if T[i] == T[i+1]:
                        Losssum += T[1]
                        LossTeamcount += 1
                        print(T[0], "has", n ,"consecutive Loss") 
                        break
                        
        #Three consecutive losses 
        for i in range (2,8-n):
            if n == 3:
                if T[i] == 1:
                    if T[i] == T[i+1] == T[i+2]:
                        Winsum += T[1]
                        WinTeamcount += 1
                        print(T[0], "has", n ,"consecutive Win")
                        break
        for i in range (2,8-n):
            if  n == 3:
                if T[i] == 0:
                    if T[i] == T[i+1] == T[i+2]:
                        Losssum += T[1]
                        LossTeamcount += 1
                        print(T[0], "has", n ,"consecutive Loss")  
                        break

        #Four consecutive losses 
        for i in range (2,8-n):
            if n == 4:
                if T[i] == 1:
                    if T[i] == T[i+1] == T[i+2] == T[i+3]:
                        Winsum += T[1]
                        WinTeamcount += 1
                        print(T[0], "has", n ,"consecutive Win")
                        break
        for i in range (2,8-n):
            if n == 4:
                if T[i] == 0:
                    if T[i] == T[i+1] == T[i+2] == T[i+3]:
                        Losssum += T[1]
                        LossTeamcount += 1
                        print(T[0], "has", n ,"consecutive Loss")  
                        break
        #Five consecutive losses 
        for i in range (2,8-n):
            if n == 5:
                if T[i] == 1:
                    if T[i] == T[i+1] == T[i+2] == T[i+3] == T[i+4]:
                        Winsum += T[1]
                        WinTeamcount += 1
                        print(T[0], "has", n ,"consecutive Win")
                        break
        for i in range (2,8-n):
            if n ==5:
                if T[i] == 0:
                    if T[i] == T[i+1] == T[i+2] == T[i+3] == T[i+4]:
                        Losssum += T[1]
                        LossTeamcount += 1
                        print(T[0], "has", n ,"consecutive Loss")  
                        break
n = int(input('Enter the number to find n consecutive Loss/Win: '))
Winsum=0
WinTeamcount=0
Losssum=0
LossTeamcount=0

T1 = ['GT', 20, 1, 1, 0, 0, 1]
Team1 = Match()
Team1.calculate_win(n, *T1)

T2 = ['LSG', 18, 1, 0, 0, 1, 1]
Team2 = Match()
Team2.calculate_win(n, *T2)

T3 = ['RR', 16, 1, 0, 1, 0, 0]
Team3 = Match()
Team3.calculate_win(n, *T3)


T4 = ['DC', 14, 1, 1, 0, 1, 0]
Team4 = Match()
Team4.calculate_win(n, *T4)



T5 = ['RCB', 14, 0, 1, 1, 0, 0]
Team5 = Match()
Team5.calculate_win(n, *T5)


T6 = ['KKR', 12, 0, 1, 1, 0, 1]
Team6 = Match()
Team6.calculate_win(n, *T6)



T7 = ['PBKS', 12, 0, 1, 0, 1, 0]
Team7 = Match()
Team7.calculate_win(n, *T7)



T8 = ['SRH', 12, 1, 0, 0, 0, 0]
Team8 = Match()
Team8.calculate_win(n, *T8)


T9 = ['CSK', 8, 0, 0, 1, 0, 1]
Team9 = Match()
Team9.calculate_win(n, *T9)


T10 = ['MI', 6, 0, 1, 0, 1, 1]
Team10 = Match()
Team10.calculate_win(n, *T10)


if WinTeamcount == 0:
    print ("No team has won", n ,"times consecutively")
else:
    WinAvg = Winsum/WinTeamcount
    print (" Average points of teams that have won", n ,"consecutive times is", WinAvg)
    
if LossTeamcount == 0:
    print ("No team has lost", n ,"times consecutively")
    
else:
    LossAvg = Losssum/LossTeamcount
    print (" Average points of teams that have lost", n ,"consecutive times is", LossAvg)
