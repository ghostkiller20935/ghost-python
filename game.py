theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
           

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
def game():
    turn = 'X'
    count = 0
    while count<9:
        printBoard(theBoard)
        print("Sada si ti na potezu," + turn + ".Koje polje zelis da izaberes?")
        move = input()        
        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("Polje koje ste izabrali je zauzeto.\nIzaberite drugo polje!")
            continue
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nKraj igre.\n")                
                print(" **** " +turn + " je pobedio. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                printBoard(theBoard)
                print("\nKraj igre.\n")                
                print(" **** " +turn + " je pobedio. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nKraj igre.\n")                
                print(" **** " +turn + " je pobedio. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                printBoard(theBoard)
                print("\nKraj igre.\n")                
                print(" **** " +turn + " je pobedio. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                printBoard(theBoard)
                print("\nKraj igre.\n")                
                print(" **** " +turn + " je pobedio. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nKraj igre.\n")                
                print(" **** " +turn + " je pobedio. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nKraj igre.\n")                
                print(" **** " +turn + " je pobedio. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nKraj igre.\n")                
                print(" **** " +turn + " je pobedio. ****")
                break 
        if count == 9:
            print("\nKraj igre.\n")                
            print("IGRA JE NERESENA!!")
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'   
game()     
   