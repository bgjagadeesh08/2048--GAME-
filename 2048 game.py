import random
#logic
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat
def add_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    
    while  mat[r][c] !=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2

def curr(mat):
    for  i in range(4):
        for j in range(4):
            if ((mat[i][j])==2048):
                return "WON"
    for  i in range(4):
        for j in range(4):
            if (mat[i][j])==0:
                return "GAME NOT OVER"
    for  i in range(3):
        for j in range(3):
            if (mat[i][j]) == mat[i][j+1]   or (mat[i][j]) == mat[i+1][j]:
                return "GAME NOT OVER"
    
            
    for j in range(3):
        if mat[3][j] ==mat[3][j+1]:
            return "GAME NOT OVER"
    for i in range(3):
        if mat[i][3] ==mat[i+1][3]:
            return "GAME NOT OVER"
    return "LOSE"
def reverse(mat):
    new=[]
    
    for i in range(4):
        new.append([])
        for j in range(4):
            new[i].append(mat[i][4-j-1])
    return new
            
def transpose(mat):
    new=[]
    for i in range(4):
        new.append([])
        for j in range(4):
            new[i].append(mat[j][i])
    return new
            
        
        
            
def merge(mat):
    changed=False
    for i in range(4):
        for j in range(3):
            if mat[i][j] ==mat[i][j+1] and mat[i][j]!=0 :
                mat[i][j]=2*mat[i][j]
                mat[i][j+1]=0
                changed=True
    return mat          
    
    
            
def compress(mat):
    new=[]
    
    for  i in range(4):
        new.append([0]*4)
    for i in range(4):
        
        pos=0
        for j in range(4):
            if mat[i][j] !=0:
                new[i][pos]=mat[i][j]
                
                pos+=1
                
    return new 
def move_up(mat):
    new=transpose(mat)
    new=compress(new)
    new=merge(new)
    
    new=compress(new)
    final=transpose(new)
    return final 

def move_down(mat):
    new=transpose(mat)
    new=reverse(new)
    new=compress(new)
    new=merge(new)
    
    new=compress(new)
    
    new=reverse(new)
    new=transpose(new)
    return new
def move_right(mat):
    new=reverse(mat)
    new=compress(new)
    new=merge(new)
    
    new=compress(new)
    new=reverse(new)
    return new 
 

def move_left(mat):
    
    new=compress(mat)
    new=merge(new)
   
    new=compress(new)
    return new 

#main
mat = start_game()
mat[1][3] = 2
mat[2][2] = 2
mat[3][0] = 4
mat[3][1] = 8
mat[2][1] = 4
inputs = [int(ele) for ele in input().split()]
for ele in inputs:
    if ele == 1:
        mat = move_up(mat)
    elif ele == 2:
        mat = move_down(mat)
    elif ele == 3:
        mat = move_left(mat)
    else:
        mat = move_right(mat)
    print(mat)
