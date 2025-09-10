'''
	centering the menu'
'''
from os import system
def main()->None:
    system('cls')
    for i in range(1,5):print(" "*73)    
    print("       MAIN MENU        ".center(73," "))
    print(" -----------------------".center(73," "))
    print(" 1. ADD STUDENT         ".center(73," "))
    print(" 2. FIND STUDENT        ".center(73," "))
    print(" 3. DELETE STUDENT      ".center(73," "))
    print(" 4. UPDATE STUDENT      ".center(73," "))
    print(" 5. DISPLAY ALL STUDENT ".center(73," "))
    print(" 0. QUIT/END            ".center(73," "))
    
    for i in range(1,5):print(" "*73)
    
if __name__=="__main__":
    main()