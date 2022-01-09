import numpy as np

def Initialize(seq):
    
    seqLength = len(seq)
    Matrix = np.zeros((seqLength,seqLength))
    for i in range (0 , seqLength):
        for j in range (0 , seqLength):
            Matrix[i][i] = 0
            Matrix[j][j-1] = 0
            
    return Matrix


def Score(Xi, Xj):
    match = 0
    tup = ((Xi, Xj))
    if tup in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C'),('G','U'),('U','G')]:
        match = 1

    return match

def FindMaxK(i ,j , Matrix):
    MaxScore1 = 0
    for k in range(i+1 , j):
        MaxScore2 = (Matrix[i][k] + Matrix[k+1][j])
        if(MaxScore2 > MaxScore1):
            MaxScore1 = MaxScore2
    return MaxScore1
        


def Comparison(seq):
    Matrix = Initialize(seq)
    for i in range (0 , len(seq)):
        for j in range (2 , len(seq)):
            if (i > j ):
                continue
            if(i == j):
                continue
             
            else:
                for x in range (1 , len(seq)):
                    for i in range (0 , len(seq)-x):
                        j = i+x
                        Matrix[i][j] = max(Matrix[i+1][j], Matrix[i][j-1], max((Matrix[i+1][j-1]+Score(seq[i],seq[j])), FindMaxK(i , j,Matrix)))
    
    print(Matrix)
    return Matrix



def recursion (i,j,stack , Matrix ):
    RecordStack = []
    stack.pop()
    if( i > j ):
        return 0
    elif (Matrix[i+1][j] == Matrix [i][j]):
        stack.insert(i+1 , j)
    elif (Matrix[i][j-1] == Matrix [i][j]):
        stack.insert(i , j-1)
    elif (Matrix[i+1][j-1] == Matrix [i][j] + Score(seq[i], seq[j])):
        RecordStack.insert(i,j)
        stack.insert(i+1 , j-1)
    else:
        for k in range (i+1 , j):
            if((Matrix[i][k]+Matrix[k+1][j]) == Matrix[i][j]):
                stack.insert(k+1,j)
                stack.insert(i,k)
                break
    return stack
            
def DotsBrackets(sequence, Stack):
    dot_bracket = ["." for _ in range(len(sequence))]
    for s in Stack:
        dot_bracket[min(s)] = "("
        dot_bracket[max(s)] = ")"
    return "".join(dot_bracket)


print("Done")

seq ="GGGAAAUCC"
Matrix = Comparison(seq)
stack =[]
for i in range (len(seq)):
    stack.append('.')
print("Done")

#while len(stack) != 0 :
stack = recursion(0, len(seq)-1, stack, Matrix )

#DotsBrackets(seq, stack)

print("Done")
