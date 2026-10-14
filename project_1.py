
Player_1_name = input("Player 1 Name: ")
Player_1_at_bats = int(input("Player 1 At bats: "))
Player_1_hits = int(input("Player 1 Hits: "))
Player_1_AVE = Player_1_hits/Player_1_at_bats

Player_2_name = input("Player 2 Name: ")
Player_2_at_bats = int(input("Player 2 At bats: "))
Player_2_hits = int(input("Player 2 Hits: "))
Player_2_AVE = Player_2_hits/Player_2_at_bats

Player_3_name = input("Player 3 Name: ")
Player_3_at_bats = int(input("Player 3 At bats: "))
Player_3_hits = int(input("Player 3 Hits: "))
Player_3_AVE = Player_3_hits/Player_3_at_bats

Player_4_name = input("Player 4 Name: ")
Player_4_at_bats = int(input("Player 4 At bats: "))
Player_4_hits = int(input("Player 4 Hits: "))
Player_4_AVE = Player_4_hits/Player_4_at_bats

Player_5_name = input("Player 5 Name: ")
Player_5_at_bats = int(input("Player 5 At bats: "))
Player_5_hits = int(input("Player 5 Hits: "))
Player_5_AVE = Player_5_hits/Player_5_at_bats

team_AVE_step_1 = Player_1_AVE + Player_2_AVE + Player_3_AVE + Player_4_AVE + Player_5_AVE
team_AVE = team_AVE_step_1/5

player_AVEs = [Player_1_AVE, Player_2_AVE, Player_3_AVE, Player_4_AVE, Player_5_AVE]

print( )
print("NAME          AB          HITS           AVE")
print("---           --------    -----------    -----------")
print(f".{Player_1_name}          {Player_1_at_bats}        {Player_1_hits}          {Player_1_AVE}")
print(f".{Player_2_name}          {Player_2_at_bats}        {Player_2_hits}          {Player_2_AVE}")
print(f".{Player_3_name}          {Player_3_at_bats}        {Player_3_hits}          {Player_3_AVE}")
print(f".{Player_4_name}          {Player_4_at_bats}        {Player_4_hits}          {Player_4_AVE}")
print(f".{Player_5_name}          {Player_5_at_bats}        {Player_5_hits}          {Player_5_AVE}")
print( )

if Player_1_AVE < team_AVE:
    print(f"{Player_1_name} is below average")
else:
    print(f"{Player_1_name} is above average")

if Player_2_AVE < team_AVE:
    print(f"{Player_2_name} is below average")
else:
    print(f"{Player_2_name} is above average")

if Player_3_AVE < team_AVE:
    print(f"{Player_3_name} is below average")
else:
    print(f"{Player_3_name} is above average")

if Player_4_AVE < team_AVE:
    print(f"{Player_4_name} is below average")
else:
    print(f"{Player_4_name} is above average")

if Player_5_AVE < team_AVE:
    print(f"{Player_5_name} is below average")
else:
    print(f"{Player_5_name} is above average")

if team_AVE < 0.245:
    print("The team has a lower average than the MLB")
else:
    print("The team has a higher average than the MLB")