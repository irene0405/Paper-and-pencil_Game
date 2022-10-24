"""
four in a line
6 * 7
cells[row][col]
connect 4 pieces in a row or column or diagonally to win
"""


class FourInALine:
    __space = " "
    __column = None
    __row = None
    __cells = None
    __player = {'player1': '●', 'player2': '○'}

    def __init__(self, row, col):
        self.__column = col
        self.__row = row
        self.__cells = [[self.__space] * self.__column for i in range(self.__row)]
        self.__drawBoard()
        print('Hello!')

    def __drawBoard(self):
        print('\n' * 300)
        # 棋盤7*6 >>> 實際含框線共 15 col and 13 row 不含編號 >> 去掉開頭結尾的框線後剩下 13*11
        print(' ', end = '')
        for col in range(self.__column):
            print(col + 1, end = self.__space)
        print()
        print('┌', end = "")  # first column
        for col in range(self.__column * 2 - 1):  # 共 13 個 column [0]~[12]
            print('─', end = "")
        print('┐')  # last column
        for row in range(self.__row * 2 - 1):  # 共 11 個 row [0]~[10]
            if row % 2 == 0:
                # 印出棋子
                j = int((row + 1) / 2)  # 棋盤的棋格列數編號
                print('│', end = '')
                for col in range(self.__column * 2 - 1):
                    if col % 2 == 0:
                        i = int((col + 1) / 2)
                        print(self.__cells[j][i], end = '')
                    else:
                        print('│', end = '')
                print('│', 6 - int(row / 2))
            else:  # 印每顆棋子之間的分隔線
                print('├', end = '')
                for col in range(self.__column * 2 - 1):
                    if col % 2 == 0:
                        print('─', end = '')
                    else:
                        print('┼', end = '')
                print('┤')
        # 印最後一列框線
        print('└', end = "")
        for col in range(self.__column * 2 - 1):
            print('─', end = "")
        print('┘')

    def putChess(self, player, col):
        row = self.__cells.__len__() - 1  # 取得最下面的 row
        emptyRow = self.__getEmptyRow(row, col)  # 找空的 row
        if emptyRow == 'FULL':
            self.__drawBoard()
            return 'FULL'
        else:
            self.__cells[emptyRow][col] = self.__player[player]
            self.__drawBoard()
            print('Nice!  ({},{}): {}'.format(6 - emptyRow, col + 1, self.getIcon(player)))
            # 下完棋之後檢查棋盤是否還有空位（是否平手）
            if not (self.__space in self.__cells[0]):
                return 'GAME DRAW'
        if self.__isWin():
            win = {'winner': player}
            return win

    def __getEmptyRow(self, row, col):
        if self.__cells[row][col] == self.__space:  # 遞迴結束條件（找到空列）
            return row
        elif row == 0:  # 遞迴結束條件（沒有空列 該欄已滿）
            return 'FULL'
        else:  # 遞迴方法
            return self.__getEmptyRow(row - 1, col)

    def __isWin(self):
        # 檢查 row
        for row in range(self.__row):
            for col in range(self.__column - 3):
                if self.__checkFour('right', row, col):
                    return True
        # 檢查 column
        for col in range(self.__column):
            for row in range(self.__row - 3):
                if self.__checkFour('down', row, col):
                    return True
        # 檢查 diagonal
        for col in range(self.__column - 3):
            for row in range(self.__row - 3):
                if self.__checkFour('lowerRight', row, col):
                    return True
        for col in range(self.__column - 3):
            for row in range(self.__row - 3):
                if self.__checkFour('lowerLeft', row, self.__column - col - 1):
                    return True
        return False

    def __checkFour(self, direction, row, col):
        # 檢查是否四顆棋子相連（獲勝）
        if direction == 'right':
            if self.__cells[row][col] == self.__cells[row][col + 1] == \
                    self.__cells[row][col + 2] == self.__cells[row][col + 3] != self.__space:
                return True
        elif direction == 'down':
            if self.__cells[row][col] == self.__cells[row + 1][col] == \
                    self.__cells[row + 2][col] == self.__cells[row + 3][col] != self.__space:
                return True
        elif direction == 'lowerLeft':
            if self.__cells[row][col] == self.__cells[row + 1][col - 1] == \
                    self.__cells[row + 2][col - 2] == self.__cells[row + 3][col - 3] != self.__space:
                return True
        elif direction == 'lowerRight':
            if self.__cells[row][col] == self.__cells[row + 1][col + 1] == \
                    self.__cells[row + 2][col + 2] == self.__cells[row + 3][col + 3] != self.__space:
                return True
        else:
            return False

    def getIcon(self, player):
        return self.__player[player]

    def isValid(self, num):
        try:
            num = int(num)
            if num >= 1 and num <= self.__column:
                return True
            else:
                self.__drawBoard()
                print('Column out of range! [1]-[{}]'.format(self.__column))
                return False
        except Exception:
            self.__drawBoard()
            print('Value error! You need to type a integer')
            return False
