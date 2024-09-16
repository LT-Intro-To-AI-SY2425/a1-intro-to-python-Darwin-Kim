# Complete your individualized AI problems here

#PRIME NUMBER CHECKER:
def IsPrime(num):
    Prime=True
    if num<2:
        Prime=False
    else:
        for i in range(2, num, 1):
            if num%i==0:
                Prime=False
    return Prime
    
#PALINDROME CHECKER:
def Palindrome(word):
    IsPalindrome=False
    wordForwards=[]
    wordBackwards=[]
    for i in range(len(word)):
        wordForwards.append(word[i])
        wordBackwards.append(word[len(word)-i-1])
    if wordForwards==wordBackwards:
        IsPalindrome=True
    return IsPalindrome

#VOWEL COUNTER:
def VowelChecker(wordList):
    vowels=0
    for i in range(len(wordList)):
        print(wordList[i])    
        if wordList[i]=="a" or wordList[i]=="e" or wordList[i]=="i" or wordList[i]=="o" or wordList[i]=="u":
            vowels+=1
    return vowels
word="this sentence has nine vowels."
wordList=list(word)
print(VowelChecker(wordList))



