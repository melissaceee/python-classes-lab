class Game():
   def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
    def play_game(self):
        print('Tic-Tac-Toe')
        while not self.tie and not self.winner:
            self.render()
            self.get_move()
            self.check_for_winner()            
            self.check_for_tie()            
            self.switch_turn()
            print(self.tie, self.winner)
        self.render()


game_instance = Game()
game_instance.play_game()