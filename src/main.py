
def main():
    #reading from file
    try:
        #parsing
        with open("data/example.in","r") as file:
            #reads each line into list
            lines= [line.strip() for line in file if line.strip()]
        #1st line becomes int k (alphabet length)
        k=int(lines[0])
        #empty dictionary
        values={}
        for i in range(1,k+1):
            char,value = lines[i].split()
            values[char]=int(value)
        A=lines[k+1]
        B=lines[k+2]
        #testing below
        #print(values)
        #print(A)
        #print(B)

        #strings length, for dynamic programming table
        stringALen=len(A)
        stringBLen=len(B)
        #creating 2D dynamic prog array
        dynamicProg=[]
        for i in range(stringALen+1):
            row=[]
            for j in range(stringBLen+1):
                row.append(0)
            dynamicProg.append(row)

        #filling array
        #skips base case row & column
        for i in range(1,stringALen+1):
            for j in range(1,stringBLen+1):
                #checks if current chars match
                if A[i-1]==B[j-1]:
                    #3 options, skips char A, char B, or uses matching char and adds its value
                    dynamicProg[i][j]=max(
                        dynamicProg[i-1][j],
                        dynamicProg[i][j-1],
                        dynamicProg[i-1][j-1]+values[A[i-1]]
                    )
                    #if they don't match, skips 1 char (uses max)
                else:
                    dynamicProg[i][j]=max(
                        dynamicProg[i-1][j],
                        dynamicProg[i][j-1]
                    )
        #print(dynamicProg)
        #is the optimal value for the 2 strings since bottom right array value stores this
        #-> max value of a common subsequence
        print(dynamicProg[stringALen][stringBLen])

        #TO DO: trace backward through 2d array for actual solution (cb)
        #so, one optimal common subsequence that achieves this value. 
        #If multiple optimal subsequences exist, you may output any one of them

    except FileNotFoundError:
        print("File opening error")
        return

if __name__ == "__main__":
    main()