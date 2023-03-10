import numpy as np


class ConnectFour():
    def __init__(self,player1,player2):
        self.player1=player1
        self.player2=player2

    def create_board(self):
        #Creating a board which is a numpy array with zero elements of shape 6,7
        board=np.zeros(shape=(6,7))
        self.board=board
        return board 

    def update_board(self, col, player):
        '''
        Players input into board
        args: col=integer; column of input 
              player=integer; player1 or player2

        returns: self.board=array; uupdated board
        '''
        col=int(col)
        for i in range(5,1,-1):
            if self.board[i][col-1]!=0:
                continue
            elif self.board[i][col-1]==0:
                self.board[i][col-1]=player
                return self.board 

    def get_winner(self, player, board):
        '''
        Determining winning move
        args: col=integer; column of input 
              board=array; connect four board
        returns True=boolean

        '''
        #check for horizontal fours
        for c in range(board.shape[1]-3):
            for r in range(board.shape[0]):
                if  board[r][c]==player and board[r][c+1]==player and board[r][c+2]==player and board[r][c+3]==player:
                    return True
        #check for vertical fours
        for c in range(board.shape[1]):
            for r in range(board.shape[0]-3):
                if  board[r][c]==player and board[r+1][c]==player and board[r+2][c]==player and board[r+3][c]==player:
                    return True
        # check for positively sloped fours
        for c in range(board.shape[1]-3):
            for r in range(board.shape[0]-3):
                if board[r][c]==player and board[r+1][c+1]==player and board[r+2][c+2]==player and board[r+3][c+3]==player:
                    return True
        # check for negatively sloped fours 
        for c in range(board.shape[1]-3):
            for r in range(board.shape[0]-3):
                if board[r][c]==player and board[r-1][c+1]==player and board[r-2][c+2]==player and board[r-3][c+3]==player:
                    return True


    def play_connect(self, player, col):
        '''
        Main method that brings all methods together 
        args: col=integer; column of input 
              player=integer; player1 or player2
        returns: board=array; updated connect four board 
        '''
        board=self.update_board(col,player)
        if self.get_winner(player, board):
            print('WINNER!!')
        return board
        
        

        







