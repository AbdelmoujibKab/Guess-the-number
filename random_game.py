import random
print('⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀ \n⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀ \n⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀ \n⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀ \n⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀ \n⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀ \n⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀ \n⠀⣿⣿⠀⠀⠀⣿⣿⡇guess the number⢸⣿⣿⠀⠀ \n⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀ \n⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀ \n⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀ \n⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀')
diff = input('Choose difficulty : \n[0] easy \n[1] Medium \n[2] Hard: \n ')
if diff == "0" :
    ops = 5
    num = random.randrange(0, 11)
    while ops > 0 :
        choice = input("weak \n Choose a number from 0 to 10 : \n")
        if int(choice) == num : print("▬▬▬.◙.▬▬▬\n═▂▄▄▓▄▄▂\n◢◤ █▀▀████▄▄▄◢◤\n█▄ █ █▄ ███▀▀▀▀▀▀╬\n◥█████◤\n══╩══╩═\n╬═╬\n╬═╬\n╬═╬    Just dropped down to say\n╬═╬   You won \n╬═╬   \n╬═╬ ☻/\n╬═╬/▌\n╬═╬/ \\")
        elif int(choice) != num :
            print("try again")
            ops -= 1
    print('LOSER')
elif diff == "1" :
    ops = 3
    num = random.randint(0, 100)
    while ops > 0:
        choice = input("weak \n Choose a number from 0 to 100 : \n ")
        if int(choice) == num:
            print(
                "▬▬▬.◙.▬▬▬\n═▂▄▄▓▄▄▂\n◢◤ █▀▀████▄▄▄◢◤\n█▄ █ █▄ ███▀▀▀▀▀▀╬\n◥█████◤\n══╩══╩═\n╬═╬\n╬═╬\n╬═╬    Just dropped down to say\n╬═╬    You won \n╬═╬   \n╬═╬ ☻/\n╬═╬/▌\n╬═╬/ \\")
        elif int(choice) != num:
            print("try again")
            ops -= 1
    print('LOSER but it\'s alright')
elif diff == '2' :
    ops = 1
    num = random.randint(0, 100)
    num = num / 100
    while ops > 0:
        choice = input("weak \n Choose a number from 0 to 1: \n")
        if float(choice) == num:
            print(
                "▬▬▬.◙.▬▬▬\n═▂▄▄▓▄▄▂\n◢◤ █▀▀████▄▄▄◢◤\n█▄ █ █▄ ███▀▀▀▀▀▀╬\n◥█████◤\n══╩══╩═\n╬═╬\n╬═╬\n╬═╬    Just dropped down to say\n╬═╬    You won \n╬═╬   \n╬═╬ ☻/\n╬═╬/▌\n╬═╬/ \\")
        elif float(choice) != num:
            print("try again")
            ops -= 1
    print('it\'s ok but u should try NEVER EVER AGAIN \n ⠟⠿⠛⠉⠉⠉⠉⠛⠛⠛⠛⠻⢿⣿⣿⣿⡿⠿⠿⠛⠛⠛⠉⠉⠉⠉⠓⠭⡙⢿\n⢁⣤⣶⣶⡿⠿⠷⠶⠶⠶⠄⣤⣾⣿⣿⣿⣿⣦⡤⠤⠶⠶⠶⠶⠿⣿⣶⣦⣄⡑\n⣿⣿⠿⣋⡍⠉⠉⠉⣉⢙⣻⡈⢻⣿⣿⣿⣿⠃⣼⣋⢉⡉⠉⠉⡉⣍⡛⢿⣿⣿\n⣿⣧⣬⣛⣃⣀⣀⣀⣚⣂⣻⣧⣿⣿⣿⣿⣿⣧⣽⣃⣚⣂⣀⣀⣀⣛⣩⣤⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢁⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⣿⣿⢡⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠟⢛⣛⣉⣡⣴⣾⣿⣿⠇⣾⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢠⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿ ')