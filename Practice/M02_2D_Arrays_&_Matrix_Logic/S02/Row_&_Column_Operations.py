# 1351
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for row in grid:
            for num in row:
                if num<0:
                    count+=1
        return count
# count=0
# rows,cols=len(grid),len(grid[0])
# for r in range(rows):
#     for c in range(cols):
#         if grid[r][c]<0:
#             count+=(cols-c)
# return count

# 832
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            row.reverse()
            for i in range(len(row)):
                if row[i]==0:
                    row[i]=1
                else:
                    row[i]=0
                # row[i]=1 if row[i]==0 else 0
                # row[i]=1-row[i]
        return image