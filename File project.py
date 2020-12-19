fname = input("Enter a file name : ") # Enter the name with Extension.       

try:
    txt = open(fname,'r')
    fil = txt.read()
    print('\nTotal number of Charecter in text :',len(fil))

    lines = fil.split("\n")  # its split the text when a newline is arrive.And creat a list of lines
    words = fil.split()     # its split the text depends on blank-space..And creat a list of words

    ptr = 0
    for j in words:          # For counting the word.
        ptr = ptr + 1

    counter = 0
    for i in lines:
        counter = counter + 1   # For counting the line.

    print('The line which start with vowel :\n')
    for k in lines:
        if k[0] in 'aeiouAEIOU':  # its check the first index of the list and when vowel is arrive it assign to it.
             print('\t',k)
    
    print('\nThe Odd lines are : ')  # print the odd number of line.
    for m in range(len(lines)):
        if (m%2) != 0:
            print('\t',m,'-->',lines[m])
    
    print('\nThe number of lines in the text :',counter)
    print('\nThe number of words :',ptr)
    print('\nThe text is :\n\n'+fil)

except:
    print('\aThe file is not present in directory.')
    print('Enter the proper name.Not forget to write extension.')
   
