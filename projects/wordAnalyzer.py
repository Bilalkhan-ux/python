sentence = input("Enter a sentence: ")
sentence = sentence.lower()

words = sentence.split()
print("Words: ",len(words))

vowels = 0
for ch in sentence:
    if ch in 'aeiou':       
        vowels +=1

print("Vowels: ", vowels)

consonant = 0

for ch in sentence:
    if ch.isalpha() and ch not in 'aeiou':
            consonant +=1

print("Consonants: ",consonant)    

longestWord = 'a'
for word in words:
     if len(word) > len(longestWord):
          longestWord = word
     

print("Longest word: ", longestWord)

uniqueWords = set(words)
uniqueWordsCount = len(uniqueWords)
print("Unique Words: ",uniqueWordsCount)
print("Repeated Words: ",len(words) - uniqueWordsCount)

