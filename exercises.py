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
       
                

game_instance = Game()
game_instance.play_game()