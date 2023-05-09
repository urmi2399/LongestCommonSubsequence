import time
#function to make matrix for longest common subsequence
def LCSLENGTH(X, Y):
    m = len(X)
    n = len(Y)
    c=[[None for i in range(0,n+1)] for j in range(0,m+1)]
    b=[[' ' for i in range(0,n+1)] for j in range(0,m+1)]
    # intilize first row as 0
    for i in range(1,m+1):  
        c[i][0]=0
    # initilizing first column zero
    for j in range(0,n+1):
        c[0][j] = 0
    # making two matrix such that
    # one matrix contains number for maximum length of substring
    # on matrix contain pattern to trace which charter was considered 
    for i in range(1,m+1):
        for j in range(1,n+1):
            if  X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] ="\\"
            elif c[i-1][j]>= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = '^'
            else:
                c[i][j] =c[i][j-1]
                b[i][j] = '<'
    return c,b

# this is function to print longest common substring

def lcsprint(X, Y, m, n):
    L = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
                # if lenght of string is return o
            if i == 0 or j == 0:
                L[i][j] = 0
            # if \ encountered, add the charcter into string
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    lcs = ""
    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:
        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs += X[i-1]
            i -= 1
            j -= 1
 
        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    # We traversed the table in reverse order
    # LCS is the reverse of what we got
    lcs = lcs[::-1]
    return lcs
      
if __name__=="__main__":
    #reading files
    with open("LCS1.txt") as file:
        l = file.readlines()

    for i in l:
        if "\n" in i:
            i = i[:-1]
        # print(i)
        myList = i.split(',')
    
        X=(myList[0])
        Y=(myList[1])

        print('X =', '\"'+X+'\"', '  Y =', '\"'+Y+'\"')
        # print('Y =', Y)
        x=''
        y=''
        start = time.time()
        #start time at beginning of function
        a,k=LCSLENGTH(X,Y)

        for i in Y:
            x=x+i+'   '
        
        # print('---------------------------------------')
        print ('----'*(len(Y)+3))
        print('    |',end='')
        print('      ',1,end='')
        for i in range(2,len(Y)+1):
            print('  ',i,end="")
        print('\n    |   Y  ',x)
        print ('----'*(len(Y)+3))
        # print('---------------------------------------')
        X1='X'+X
        
        for i in range(1,len(X1)+1):
            s=''
            s=''+X1[i-1]+' |'
            for j in range(0,len(Y)+1):
                s=s+'  '+str(k[i-1][j])
                s=s+''+str(a[i-1][j])
            if i-1 == 0:
                print(' ',s)
            else:
                print(i-1,s)
            # print(i-1,s)
            # print(s)
            
        ans=lcsprint(X, Y,len(X),len(Y)) 
        #end time
        end = time.time()
        #printing output
        # print('---------------------------------------')
        print ('----'*(len(Y)+3))
        print("Length of the Longest Common Subsequence is: "+str(a[len(X)][len(Y)]))
        print("The Longest Common Subsequence of  "+'\"'+X+'\"'+" and "+'\"'+Y+'\"'+" is "'\"'+ans+'\"')
        # print(f"Runtime of the program is {end - start}")
        print('\n')
