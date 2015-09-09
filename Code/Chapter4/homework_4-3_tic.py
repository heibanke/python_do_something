#!/usr/bin/env python
# coding: utf-8
#copyRight by heibanke
import sys
import random

def console (color):
    if sys.platform[:3] == 'win':
        try: import ctypes
        except: return 0
        kernel32 = ctypes.windll.LoadLibrary('kernel32.dll')
        GetStdHandle = kernel32.GetStdHandle
        SetConsoleTextAttribute = kernel32.SetConsoleTextAttribute
        GetStdHandle.argtypes = [ ctypes.c_uint32 ]
        GetStdHandle.restype = ctypes.c_size_t
        SetConsoleTextAttribute.argtypes = \
            [ ctypes.c_size_t, ctypes.c_uint16 ]
        SetConsoleTextAttribute.restype = ctypes.c_long
        handle = GetStdHandle(0xfffffff5)
        if color < 0: color = 7
        result = 0
        if (color & 1): result |= 4
        if (color & 2): result |= 2
        if (color & 4): result |= 1
        if (color & 8): result |= 8
        if (color & 16): result |= 64
        if (color & 32): result |= 32
        if (color & 64): result |= 16
        if (color & 128): result |= 128
        SetConsoleTextAttribute(handle, result)
    else:
        if color >= 0:
            foreground = color & 7
            background = (color >> 4) & 7
            bold = color & 8
            sys.stdout.write(" \033[%s3%d;4%dm"%(bold \
                and "01;" or "", foreground, background))
            sys.stdout.flush()
        else:
            sys.stdout.write(" \033[0m")
            sys.stdout.flush()
    return 0
    
    
def drawQi(s):
    """
    # 9:red, 10:green, 13:purple
    """
    if s=='X':
        console(13)
    elif s=='O':
        console(10)
    else:
        console(-1)
    print "%2s"%s,
    console(-1)
    print " |",
    
    
def drawBoard(board):    
    # "board" is a list of 10 strings representing the board (ignore index 0)
    blank_board = '|     '*3+'|'
    edge_board = '+-----'*3+'+'
    def drawLine(board_line):
        insert_sym = '|'
        print blank_board
        print insert_sym,
        for i in range(3):
            drawQi(board_line[i])
        print ''
        #print "|%3s%3s%3s%3s%3s  |"%(board_line[0],insert_sym,board_line[1],insert_sym,board_line[2])
        print blank_board
        print edge_board
        
    print edge_board
    drawLine(board[7:10])
    drawLine(board[4:7])
    drawLine(board[1:4])

def inputPlayerLetter():
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print u'你想用 X or O?'
        letter = raw_input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def playerMove(board,letter):
    # Let the player type in his move.
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split():
        print u'你的下一步是什么? (1-9)'
        move = raw_input()
        try:
            if not isSpaceFree(board, int(move)):
                print u'棋盘上在%s这个位置已经有棋子了！'%move
                move=''
                continue
        except:
            print u'输入不合规则，请输入有效数字（1-9）'
            continue
        
    board[int(move)] = letter 
    
    return isWinner(board,letter)
    
def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print u'你想再玩一次吗? (yes or no)'
    return raw_input().lower().startswith('y')


def isWinner(bo, le):
    # Given a board and a player's letter, this function returns True if that player has won.
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal


def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' ' or board[move] in '1 2 3 4 5 6 7 8 9'.split()


def isBoardFull(board):
    # Return True if every space on the board has been taken. Otherwise return False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True

def chooseRandomMoveFromList(board,movesList):
    # Returns a valid move from the passed list on the passed board.
    # Returns None if there is no valid move.
    possibleMoves = []
    for i in movesList:
        if board[i]==str(i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def computerMove(board,letter):
    move = None
    # 首先看自己是否能赢
    copy = board[:]
    for i in range(1, 10):
        if copy[i]==str(i):
            copy[i] = letter
            if isWinner(copy, letter):
                move = i
                break
            else:
                copy[i]=str(i)

    if letter=='X':
        player = 'O'
    else:
        player = 'X'

    # 然后看是否应该阻止对方赢
    if move == None:
        copy = board[:]
        for i in range(1, 10):
            if copy[i]==str(i):
                copy[i] = player
                if isWinner(copy, player):
                    move = i
                    break
                else:
                    copy[i]=str(i)


    # 优先占据中心                
    if move == None:
        if board[5]=='5':
            move = 5

    # 优先占据角落
    if move == None:
        move = chooseRandomMoveFromList(board,[1, 3, 7, 9])
    
    # 剩下的位置
    if move == None:
        move = chooseRandomMoveFromList(board,[2, 4, 6, 8]) 

        
    board[move] = letter 
    
    return isWinner(board,letter)



if __name__=="__main__":
    print u'欢迎来玩井字棋--Tic Tac Toe!'

    while True:
        # Reset the board
        theBoard = '0 1 2 3 4 5 6 7 8 9'.split()
        player_letter, computer_letter = inputPlayerLetter()
        Letter = (player_letter, computer_letter)
        print u' ' +Letter[0] + u'先走.'
        turn = 0
        gameIsPlaying = True

        while gameIsPlaying:
            
            # Player's turn.
            drawBoard(theBoard)
            current_letter = Letter[turn]
            
            print u"轮到 "+current_letter+u" 走了"
            
            if current_letter==player_letter:
                #is_win = playerMove(theBoard,current_letter)
                is_win = computerMove(theBoard,current_letter)
            else:
                is_win = computerMove(theBoard,current_letter)

            if is_win:
                drawBoard(theBoard)
                print u'哇! '+current_letter+u' 赢了!'
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print u'Game over，棋力相当，平局!'
                    break
                else:
                    turn = (turn+1)%2

        if not playAgain():
            break
