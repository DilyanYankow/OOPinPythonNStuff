from datetime import datetime


wins = 0
losses = 0
avrg = 0
gambles = " "
while result := gambles[-1] != "Q":
    gambles = gambles + input("Did you win or lose?: ").upper()
    if gambles[-1] == "L":
        losses += 1
    else:
        wins += 1

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    avrg = wins - losses

    try:
        with open("history.txt", "a") as file:
            file.writelines("\n---------------\n")
            file.writelines("Total Wins: " + str(wins))
            file.writelines("\nTotal Losses: " + str(losses))
            file.writelines("\nTotal Wins - Losses: " + str(avrg))
            file.writelines(("\nCurrent Time =", current_time))
            file.writelines("\n---------------")
    except FileNotFoundError:
        print("File not found: ")
    avrg = wins - losses
    print("---------------")
    print(gambles)
    print("Total Wins: " + str(wins))
    print("Total Losses: " + str(losses))
    print("Total Wins - Losses: " + str(avrg))
    print("Current Time =", current_time)
    print("---------------")



