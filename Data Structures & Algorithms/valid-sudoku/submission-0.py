class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxes = {}
        for i in range(0,9):
            sett = set()
            sett2 = set()
            for j in range(0,9):
                element = board[i][j]
                print(element)
                print(sett)
                if (element in sett and element != "."):
                    return False
                sett.add(element)

                element2 = board[j][i]
                if (element2 in sett2 and element2 != "."):
                    return False
                sett2.add(element2)

                box_key = (i//3,j//3)
                if box_key not in boxes:
                    boxes[box_key] = set()
                if (element in boxes[box_key] and element != "."):
                    return False
                boxes[box_key].add(element)
        return True
       