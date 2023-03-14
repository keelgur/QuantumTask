
row_num,col_num=map(int,input("Input: ").split())
map_mat=[]
for j in range(row_num):
    tmp=[]
    for i in input("Input: ").split():
        tmp.append(int(i))
    map_mat.append(tmp)
def islandNum(mat: list[list[int]]) -> int:
    rws = len(mat)
    cls = len(mat[0])

    cnt = 0
    def dfs(row, col):
        if col==cls or row==rws or row<0 or col<0:
            return
        if map_mat[row][col]!=1:
            return

        map_mat[row][col] = -1

        dfs(row-1, col)
        dfs(row+1, col)
        dfs(row, col-1)
        dfs(row, col+1)
    for n in range(rws):
        for m in range(cls):
            if map_mat[n][m] == 1:
                dfs(n, m)
                cnt+=1
    return cnt
print("Output: ",islandNum(map_mat))
