word1=input('Input a word: ').split()
word2=input('Input a word: ').split()
for i in range(len(word1)):
  if word1[i] in word2:
    print(i)