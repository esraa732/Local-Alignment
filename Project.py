
class LocalAlignment :

    def __init__(self ,A , B ,Match ,Mismatch ,Gap):
        self.A = A
        self.B = B
        self.m = len(A)
        self.n = len(B)
        self.Match = Match 
        self.Mismatch = Mismatch 
        self.Gap = Gap


    def scoring (self , x , y):
        if x == y :
            return self.Match
    
        else:
            return self.Mismatch

    def positive (self , num):
        x = num
        if  x < 0 :
            return 0
        else :
            return x


    def Local (self):

        #zero matrix
        Matrix  = [ [ 0 for i in range (self.n+1)] for j in range (self.m+1) ]

        #initialize first (row & coloumn)
        x = self.Gap 
        for i in range (1 , self.m+1):
              y = self.positive( x)
              Matrix[i][0] = y
              x= x + self.Gap

        x = self.Gap 
        for j in range (1 , self.n+1):
             Matrix[0][j] = self.positive( x)
             x= x + self.Gap
 

        for i in range (1 , self.m+1):

             for j in range (1 , self.n+1):

                 Matrix[i][j] =  max(self.positive(Matrix[i-1][j-1] + self.scoring(self.A[i-1] , self.B[j-1])) ,self.positive( Matrix[i-1][j] + self.Gap) ,self.positive( Matrix[i][j-1] +self.Gap) , 0)
        for line in Matrix:
            print(line)
                                   
        print("The score is  :  " ,  Matrix[self.m][self.n])



        #Backtracking


        Maximum = 0
        for index1 in range (1 , self.m+1):
                      for index2 in range (1 , self.n+1):
                          if  (Maximum < Matrix[index1][index2]) :
                            Maximum = Matrix[index1][index2]
                            i = index1
                            j = index2

       
        BacktrackingList = []
        IndexOfI = []
        IndexOfJ = []
        k = 0

        while (i != 0 or j != 0) :

            
             BacktrackingList.append (max(self.positive(Matrix[i-1][j-1] + self.scoring(self.A[i-1] , self.B[j-1])) ,self.positive( Matrix[i-1][j] + self.Gap) ,self.positive( Matrix[i][j-1] +self.Gap) , 0) )
             
             if ( BacktrackingList[k] == 0 ):


                 BacktrackingList.pop()
                 #IndexOfI.pop()
                 #IndexOfJ.pop()
                 break
                

             if ( BacktrackingList[k] == self.positive(Matrix[i-1][j-1] + self.scoring(self.A[i-1] , self.B[j-1])) ):
                # IndexOfI[k] = i-1
                # IndexOfJ[k] = j-1
                 i -= 1 
                 j -= 1

             elif  ( BacktrackingList[k] == self.positive( Matrix[i-1][j] + self.Gap) ):
                 #IndexOfI[k] = i-1
                # IndexOfJ[k] = j
                 i -= 1

             else:
                 j -=1

             k += 1

        
        print("The Backtracking Array is   :   " , BacktrackingList)
        querySeq1='CGTGAATTGCGCGCGCATCGTGAAATATATATATTTCA'
        aminoAcids = 'ARNDCQEGHILKMFPSTWYV'
        for i in range(len(querySeq1)-2):
            if i+3> len(querySeq1):
                #l = [seq1[i]]
                #print(l)
                break;
            else:
                l=[querySeq1[i:i+3]]
                print(l)
                print("=======")
                for z in l:
                    for j in range(len(aminoAcids)):
                        l2=[aminoAcids[j]+z[1:]]
                
                        l3=[z[0]+aminoAcids[j]+z[2]]
                
                        l4=[z[0:2]+aminoAcids[j]]
                
                        print(l2,l3,l4)
                print("*_*"*8)

      ###Replacing 
"""X =IndexOfI.count
        for i in range (1 , self.m+1):

             for j in range (1 , self.n+1):
                if (IndexOfI[ X] == i):
                    if(IndexOfJ[X] == j ):
                        Matrix[i][j] = "X"
                        X -=1 
                        """
        

def main ():

    Match = int(input("The Match Score is : "))  
    Mismatch = int(input("The Mismatch Score is : "))   
    Gap = int(input("The Gap Score is : "))  
    Repeated = ["GCGCGCG","ATATATATAT"]
    A = "CGTGAATTGCGCGCGCATCGTGAAATATATATATTTCA"
    B = Repeated[0]
    for i in range (0 , 2):
        B = Repeated[i]
        obj = LocalAlignment(A , B , Match , Mismatch , Gap )
        obj.Local() 
        print("-------------------------")


if __name__=="__main__":
    main()
