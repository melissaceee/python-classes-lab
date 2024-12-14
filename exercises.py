class Game():
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def play_game(self):
        print('Welcome to Tic-Tac-Toe')
        while not self.tie and not self.winner:
            self.render()
            self.get_move()
            self.check_for_winner()            
            self.check_for_tie()            
            self.switch_turn()
            print(self.tie, self.winner)
        self.render()

    def print_board(self):
        b = self.board
        print(f"""
              A   B   C
          1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
              ----------
          2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
              ----------
          3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if (self.tie):
            print('This game is a tie!')
        elif (self.winner):
            print(f'{self.winner} wins the gamne')
        else:
            print(f'It\'s players {self.turn}\'s turn')    
    
    def render(self):
        self.print_board()
        self.print_message()
    
    def get_move(self):
        if (not self.tie) or (self.winner == None):  
        
            move = input(f"Enter a valid move (example: A1): ").lower()
        if move in self.board and not self.board[move]:
            self.board[move] = self.turn
            print(f'You picked {move}')
        else:
            print(f"{move} is not a valid input please try again!")
            

    def check_for_winner(self):
        if self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']):
            self.winner = self.turn
        elif self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']):
            self.winner = self.turn        
        elif self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']):
            self.winner = self.turn 
        elif self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']):
            self.winner = self.turn 
        elif self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']):
            self.winner = self.turn 
        elif self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']):
            self.winner = self.turn 

    def check_for_tie(self):
        
        board_full = 9
        spaces_filled = 0        
        for space in self.board:
            if self.board[space] == None and not self.winner:
                pass
            else:
                spaces_filled += 1       
          
            
        if spaces_filled == 9 and not self.winner:
            self.tie = True
        
        
                
    def switch_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        elif self.turn == 'O':
            self.turn = 'X'
                
                

game_instance = Game()
game_instance.play_game()