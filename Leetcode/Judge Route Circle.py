class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        posx = 0
        posy = 0
        for move in moves:
            if move is 'U':
                posy = posy + 1
            elif move is 'D':
                posy = posy - 1
            elif move is 'L':
                posx = posx - 1
            else:
                posx = posx + 1
        if posx == posy == 0:
            return True
        else:
            return False
