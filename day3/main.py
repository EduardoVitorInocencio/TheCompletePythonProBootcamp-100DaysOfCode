from sys import exit

print("""
      
                                                                       #####
                                                                #######
                   #                                            ##O#O##
  ######          ###                                           #VVVVV#
    ##             #                                          ##  VVV  ##
    ##         ###    ### ####   ###    ###  ##### #####     #          ##
    ##        #  ##    ###    ##  ##     ##    ##   ##      #            ##
    ##       #   ##    ##     ##  ##     ##      ###        #            ###
    ##          ###    ##     ##  ##     ##      ###       QQ#           ##Q
    ##       # ###     ##     ##  ##     ##     ## ##    QQQQQQ#       #QQQQQQ
    ##      ## ### #   ##     ##  ###   ###    ##   ##   QQQQQQQ#     #QQQQQQQ
  ############  ###   ####   ####   #### ### ##### #####   QQQQQ#######QQQQQ
      
      """)

print("Welcome to Tresure Island")
print("Your mission is to find the treasure.")


direction = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"")

if direction.lower() == 'left':
    swimWait = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")

    if swimWait.lower() == 'swim':
        
        print("GAME OVER!")
        
    elif swimWait.lower() == 'wait':
        
        door = input("You're arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        
        if door.lower() in ['blue', 'red']:
            
            print("GAME OVER!")
            
        elif door.lower() == 'yellow':
            
            print("YOU WIN!")
else:
    print("GAME OVER!")