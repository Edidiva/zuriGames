import random
def Play_again():
        while True:
            replay = input("would you like to play again? Y/N\n")
            if replay == 'Y':
                Game_on()
            elif replay == "N":
                print("bye")
                break
            else:
                print("inavalid option, pick Y/N")
X = {"R":"Rock", "S" :"Scissors", "P":"Paper"}
def Game_on():
        myList = ["R","S","P"]
        user_choice = input('Choose any of these letters:\n R for Rock\n S for Scissors\n P for paper\n')
        cpu_choice = random.choice(myList)
        N = [user_choice, cpu_choice]
        if user_choice in myList:
                if ["R","S"] == N:
                    print("Player (Rock) : CPU (Scissors): You won")
                elif ["P", "R"] == N:

                    print("Player (Paper) : CPU (Rock): You won")
                elif ["S","P"] == N:
                    print("Player (Scissors) : CPU (Paper): You won")
                elif user_choice == cpu_choice:
                    
                    print( "Player(",X[user_choice],"):CPU(", X[cpu_choice],") You have a tie ")
                    Play_again()
                else:
                    print( "Player(",X[user_choice],"):CPU(", X[cpu_choice],") You have a lost")     
        else:
            print("pls choose a correct option")
            Game_on()              
Game_on()

            
            
           




                        
