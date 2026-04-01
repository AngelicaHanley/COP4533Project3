

def main():
    #reading from file
    try:
        #alphabet parsing
        with open("data/example.in","r") as file:
            #reads each line into array lines
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
        print(values)
        print(A)
        print(B)

        #strings length, for dynamic programming table
        n=len(A)
        m=len(B)
        #creating 2D dynamic prog array
        dynamicProg=[]
        for i in range(n+1):
            row=[]
            for j in range(m+1):
                row.append(0)
            dynamicProg.append(row)
        print(dynamicProg)
    except FileNotFoundError:
        print("File opening error")
        return

if __name__ == "__main__":
    main()