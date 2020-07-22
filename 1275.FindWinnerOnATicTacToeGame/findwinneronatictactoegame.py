class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        m = [[0] * 3 for _ in range(3)]
        for i in range(len(moves)):
            if i % 2 == 0:
                m[moves[i][0]][moves[i][1]] = 'A'
            else:
                m[moves[i][0]][moves[i][1]] = 'B'

        all_x = ['A']*3
        all_o = ['B']*3

        triples = [
					 m[0], m[1], m[2],
                     [m[0][0], m[1][0], m[2][0]], [m[0][1], m[1][1], m[2][1]], [m[0][2], m[1][2], m[2][2]],
                     [m[0][0], m[1][1], m[2][2]], [m[0][2], m[1][1], m[2][0]]
					 ]

        if all_x in triples:
            return 'A'
        elif all_o in triples:
            return 'B'

        if len(moves) < 9:
            return 'Pending'
        else:
            return 'Draw'
