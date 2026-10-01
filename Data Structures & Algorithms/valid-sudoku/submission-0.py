class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        collumndict = defaultdict(list)
        rowdict = defaultdict(list)
        squaresdict = defaultdict(list)

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                    try:
                        num_to_int = int(num)
                        if num in collumndict[j]:
                            return False
                        else:
                            collumndict[j].append(num)
                        if num in rowdict[i]:
                            return False
                        else:
                            rowdict[i].append(num)
                        if num in squaresdict[(i // 3) * 3 + (j // 3)]:
                            return False
                        else:
                            squaresdict[(i // 3) * 3 + (j // 3)].append(num)
                    except:
                        continue

        return True

