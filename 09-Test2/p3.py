def f(array2D):
    row=0
    col=0
    for i,v in enumerate(array2D):
        for j,w in enumerate(v):
            row+=array2D[i][j]
            col+=array2D[j][i]
        print(row)
        print(col)
        if row!=col:
            return False
        row=0
        col=0
    return True
            
            
        
    
if __name__=="__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))
        
