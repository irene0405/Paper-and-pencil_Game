import random


class Minimax(object):
    board = None
    color = ['O', 'X']

    def __init__(self, board):
        self.board = board

    def bestMove(self, depth, state, curr_player):

        if curr_player == self.color[0]:
            opp_player = self.color[1]
        else:
            opp_player = self.color[0]

        legalMoves = {}
        for i in range(9):
            if self.isLegalMove(i, state):
                temp = self.makeMove(state, i, curr_player)
                legalMoves[i] = -self.search(depth - 1, temp, opp_player)

        best_alpha = -99999999
        best_move = None
        moves = legalMoves.items()
        random.shuffle(list(moves))
        for move, alpha in moves:
            if alpha >= best_alpha:
                best_alpha = alpha
                best_move = move

        return best_move, best_alpha

    def search(self, depth, state, curr_player):
        legal_moves = []
        for i in range(9):
            if self.isLegalMove(i, state):
                temp = self.makeMove(state, i, curr_player)
                legal_moves.append(temp)

        if depth == 0 or len(legal_moves) == 0 or self.gameIsOver(state):
            return self.value(state, curr_player)

        if curr_player == self.color[0]:
            opp_player = self.color[1]
        else:
            opp_player = self.color[0]

        alpha = -99999999
        for child in legal_moves:
            if child is None:
                print('child == None (search)')
            alpha = max(alpha, -self.search(depth - 1, child, opp_player))
        return alpha

    def isLegalMove(self, i, state):
        if state[i] == '-':
            return True
        return False

    def gameIsOver(self, state):
        if self.checkForStreak(state, self.color[0], 3) >= 1:
            return True
        elif self.checkForStreak(state, self.color[1], 3) >= 1:
            return True
        else:
            return False

    def makeMove(self, state, i, color):
        temp = [x[:] for x in state]
        if temp[i] == '-':
            temp[i] = color
            return temp

    def value(self, state, color):
        if color == self.color[0]:
            o_color = self.color[1]
        else:
            o_color = self.color[0]

        my_threes = self.checkForStreak(state, color, 3)
        my_twos = self.checkForStreak(state, color, 2)
        opp_threes = self.checkForStreak(state, o_color, 3)
        opp_twos = self.checkForStreak(state, o_color, 2)
        if opp_threes > 0:
            return - (10000000 * opp_threes + 100 * opp_twos)
        else:
            return my_threes * 10000000 + my_twos * 10

    def checkForStreak(self, state, color, streak):
        count = 0

        for i in range(9):
            if state[i].lower() == color.lower():
                count += self.verticalStreak(i, state, streak)
                count += self.horizontalStreak(i, state, streak)
                count += self.diagonalCheck(i, state, streak)

        return count

    def verticalStreak(self, pt, state, streak):
        consecutiveCount = 0

        for i in range(2):
            if i == 0:
                pt_check = (pt + 3) % 9
            elif i == 1:
                pt_check = (pt + 6) % 9
            if state[pt].lower() == state[pt_check].lower():
                consecutiveCount += 1

        if consecutiveCount >= streak:
            return 1
        else:
            return 0

    def horizontalStreak(self, pt, state, streak):
        consecutiveCount = 0

        if pt < 3:
            for i in range(2):
                if i == 0:
                    pt_check = (pt + 1) % 3
                elif i == 1:
                    pt_check = (pt + 2) % 3
                if state[pt].lower() == state[pt_check].lower():
                    consecutiveCount += 1
        elif pt > 2 and pt < 6:
            for i in range(2):
                if i == 0:
                    pt_check = ((pt + 1) % 3) + 3
                elif i == 1:
                    pt_check = ((pt + 2) % 3) + 3
                if state[pt].lower() == state[pt_check].lower():
                    consecutiveCount += 1
        else:
            for i in range(2):
                if i == 0:
                    pt_check = ((pt + 1) % 3) + 6
                elif i == 1:
                    pt_check = ((pt + 2) % 3) + 6
                if state[pt].lower() == state[pt_check].lower():
                    consecutiveCount += 1

        if consecutiveCount >= streak:
            return 1
        else:
            return 0

    def diagonalCheck(self, pt, state, streak):
        total = 0
        consecutiveCount = 0

        if pt == 4:
            for i in range(2):
                if i == 0:
                    pt_check = 0
                elif i == 1:
                    pt_check = 8
                if state[pt].lower() == state[pt_check].lower():
                    consecutiveCount += 1
            if consecutiveCount >= streak:
                total += 1

            consecutiveCount = 0
            for i in range(2):
                if i == 0:
                    pt_check = 2
                elif i == 1:
                    pt_check = 6
                if state[pt].lower() == state[pt_check].lower():
                    consecutiveCount += 1
            if consecutiveCount >= streak:
                total += 1

        elif pt == 0 or pt == 8:
            for i in range(2):
                if i == 0:
                    pt_check = (pt + 4) % 12
                elif i == 1:
                    pt_check = (pt + 8) % 12
                if state[pt].lower() == state[pt_check].lower():
                    consecutiveCount += 1
            if consecutiveCount >= streak:
                total += 1
        elif pt == 2 or pt == 6:
            for i in range(2):
                if i == 0:
                    pt_check = (pt + 2) % 6
                elif i == 1:
                    pt_check = (pt + 4) % 6
                if state[pt].lower() == state[pt_check].lower():
                    consecutiveCount += 1
            if consecutiveCount >= streak:
                total += 1

        return total
