import random

# total given cards 13 * 8 = 104
one_set = ['K♠','Q♠','J♠','10♠','9♠','8♠','7♠', '6♠','5♠','4♠','3♠','2♠','A♠']
deck = one_set * 8

p1, p2, p3, p4, p5, p6, p7, p8 = [], [], [], [], [], [], [], []
tableau = [p1, p2, p3, p4, p5, p6, p7, p8]

f1, f2, f3, f4 = [], [], [], []
foundation = [f1, f2, f3, f4]

def draw():
     '''Draw one card for each tableau pile from the deck,
     Removing used cards to ensure no card is drawn twice,
     When all cards are drawn, there is no more "draw" move.'''

     #if deck is empty, it returns True
     if not deck:
          print('No cards left in the deck!')
          return
     #append random cards to every piles
     p1.append(random.choice(deck))
     p2.append(random.choice(deck))
     p3.append(random.choice(deck))
     p4.append(random.choice(deck))
     p5.append(random.choice(deck))
     p6.append(random.choice(deck))
     p7.append(random.choice(deck))
     p8.append(random.choice(deck))

     #remove the used cards from the deck to prevent repetition
     for pile in [p1, p2, p3, p4, p5, p6, p7, p8]:
          deck.remove(pile[-1])

def screen():
    print("Tableau:")
    for index, pile in enumerate(tableau, start=1): #goes through each tableau pile with the index (starts at 1)
        print(f"Pile {index}: {pile if pile else 'Empty'}") #if the list of pile is not empty, it prints the lists, 
                                                            #otherwise 'Empty'
    
    print("\nFoundations:")
    for index, foundation_pile in enumerate(foundation, start=1):
        print(f"Foundation {index}: {foundation_pile if foundation_pile else 'Empty'}")
    print("-------------------------")

def pile_to_pile():
     '''Move cards between piles,
     Check if it follows the order,
     If pile is empty, it is moved directly'''
     first_pile = int(each_move[0]) -1 #index of the source pile (converts to zero-based index)
     second_pile = int(each_move[1]) - 1 #index of the destination pile

     from_pile = tableau[first_pile] #exact reference to the source pile
     to_pile = tableau[second_pile] #exact reference to the destination pile

     if not from_pile: #check if the source pile is empty
          print(f'{from_pile} is empty!')
          return
     
     if not to_pile: #if the destination pile is empty, card is added directly
          to_pile.append(from_pile.pop()) #source pile's last element is removed, and this removed element added to destination pile
          return

     #check validate move according to the order
     moving_card = from_pile[-1] #the source pile's last element
     target_card = to_pile[-1] #the destination pile's last element
     one_set =['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠']

     #if moving card's index + 1 = target card's index, it is a valid move
     if one_set.index(moving_card) + 1 == one_set.index(target_card): 
          to_pile.append(from_pile.pop())   
     else:
          print('invalid move, try again')
          return


def move_to_foundation():
     '''Move cards from piles to foundations,
     If the foundation is empty, it only starts with A♠,
     Checks the order'''
     first_pile = int(each_move[0]) - 1 #index of the source pile (converts to zero-based index)
     from_pile = tableau[first_pile] #index of the destination pile
     moving_card = from_pile[-1] #the source pile's last element
     if not from_pile: #check if the source pile is empty
          print(f'Pile {each_move[0]} is empty!')
          return
     
     if not f1: #checks if f1 is empty
          if moving_card == 'A♠':  #only an Ace can start a foundation
               f1.append(from_pile.pop())  #card can be directly added
               return
     elif not f2:
          if moving_card == 'A♠': 
               f2.append(from_pile.pop()) 
               return
     elif not f3:
          if moving_card == 'A♠': 
               f3.append(from_pile.pop()) 
               return
     elif not f4:
          if moving_card == 'A♠':
               f4.append(from_pile.pop()) 
               return
          
     one_set = ['K♠','Q♠','J♠','10♠','9♠','8♠','7♠', '6♠','5♠','4♠','3♠','2♠','A♠']
     try:
          if each_move[1] == 'f1': #if second input is f1
               #the index of the last element in the foundation1 = the index of moving card + 1
               if one_set.index(f1[-1]) == one_set.index(moving_card) + 1:
                    f1.append(from_pile.pop())
          elif each_move[1] == 'f2':
               if one_set.index(f2[-1]) == one_set.index(moving_card) + 1:
                    f2.append(from_pile.pop())
          elif each_move[1] == 'f3':
               if one_set.index(f3[-1]) == one_set.index(moving_card) + 1:
                    f3.append(from_pile.pop())
          elif each_move[1] == 'f4':
               if one_set.index(f4[-1]) == one_set.index(moving_card) +1:
                    f4.append(from_pile.pop())
     except IndexError:
          print('invalid move!')
          return

def win():
     #if all four foundations' last elements are K♠, returns True, otherwise False
     if f1 and f1[-1] == 'K♠' and f2 and f2[-1] == 'K♠'and f3 and f3[-1] == 'K♠' and f4 and f4[-1] == 'K♠':
          return True
     return False

def main_flow():
     draw() #initial card draw
     screen() #display initial screen
     while True: #infinite loop until quit or win
          try:
               global move #to use it across all functions
               move = input("""'1 2' to move card from Pile1 to Pile2, or '1 f1' to move card from Pile1 to Foundation1, or 'draw', or 'quit'
                         Enter your move: """)
               if move == 'quit':
                    print("-- Enkhkhuslen's Simplified Salitaire --")
                    break
               elif move == 'draw':
                    draw() #goes to the draw() function
                    screen() #update the game state
               elif ' ' in move:
                    global each_move
                    each_move = move.split() #desperate input into list

                    if 'f' in move:
                         move_to_foundation()
                         screen()  #update the game state

                    elif int(each_move[0]) in range(1, 9) and int(each_move[1]) in range(1, 9): #check if input as int is in range 8
                         pile_to_pile() #goes to the pile_to_pile() function
                         screen() #update the game state

               if win(): #if win() is True, the game stops
                    break


          except ValueError:
               print('Invalid move! Try again!')
main_flow()