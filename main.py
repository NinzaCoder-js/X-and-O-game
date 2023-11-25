y = 0
x = 0
check = True
while check:
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(f"""
      {n[0]} | {n[1]} | {n[2]}
      ----------
      {n[3]} | {n[4]} | {n[5]}
      ----------
      {n[6]} | {n[7]} | {n[8]}
    """)
    for i in n:
        x = int(input(f"Add X in your own place : => "))

        while x==y:
            print("It isn't free enter x again")
            x = int(input(f"Add X in your own place : => "))
        n.pop(x - 1)
        n.insert(x - 1, "X")
        print(f"""
          {n[0]} | {n[1]} | {n[2]}
          ----------
          {n[3]} | {n[4]} | {n[5]}
          ----------
          {n[6]} | {n[7]} | {n[8]}
        """)
        if n[0] == n[1] == n[2] == "X" or n[3] == n[4] == n[5] == "X" or n[6] == n[7] == n[8] == "X" or n[0] == n[3] == n[6] == "X" or n[1] == n[4] == n[7] == "X" or n[2] == n[5] == n[8] == "X" or n[0] == n[4] == n[8] == "X" or n[2] == n[4] == n[6] == "X":
            print('X comand is win')
            break

        y = int(input(f"Add O in your own place : => "))
        while x==y:
            print("It isn't free enter y again")
            y = int(input(f"Add O in your own place : => "))

        n.pop(y - 1)
        n.insert(y - 1, "O")
        print(f"""
          {n[0]} | {n[1]} | {n[2]}
          ----------
          {n[3]} | {n[4]} | {n[5]}
          ----------
          {n[6]} | {n[7]} | {n[8]}
        """)
        if n[0] == n[1] == n[2] == "O" or n[3] == n[4] == n[5] == "O" or n[6] == n[7] == n[8] == "O" or n[0] == n[3] == n[6] == "O" or n[1] == n[4] == n[7] == "O" or n[2] == n[5] == n[8] == "O" or n[0] == n[4] == n[8] == "O" or n[2] == n[4] == n[6] == "O":
            print('O comand is win')
            break

    playAgain = input("Do you want play again (yes or no) => ")
    if playAgain == 'no':
        check = False
        print("Thank you for your playing")
        break









