def countWords() :
    fileName = input("Enter Your File Name Here :- ")
    count = 0
    file = open(fileName,'r')
    for item in file :
        words = item.split()
        count = count + len(words)
    print("Number Of Words In Your File Are :- ", count)
  
countWords()