# 1. Count the number of vowels in a string.
a="sabitha"
vowels="AEIOUaeiou"
count=0
for ch in a:
    if ch in vowels:
        count+=1
print("No of vowels in a string:",count)

# 2. Count the number of consonants in a string.
b="programming"
vowels="AEIOUaeiou"
count=0
for ch in b:
    if ch.isalpha() and ch not in vowels:
        count+=1
print("No.of consonants:",count)

# 3. Count uppercase and lowercase letters separately.
c="HelloO PrograMmerS"
upper=0
lower=0
for ch in c:
    if ch.isupper():
        upper+=1
    if ch.islower():
        lower+=1
print("Count of upper letters:",upper)
print("Count of lower letters:",lower)

# 4. Reverse a string without using slicing.
d="Pythonprogramming"
reverse=""
for ch in d:
    reverse=ch+reverse
print(reverse)

# 5. Check if a string is a palindrome.
e="madam"
reverse=""
for ch in e:
    reverse=ch+reverse
if reverse==e:
    print("String is a palindrome")
else:
    print("String is  not a palindrome")

# 6. Find the frequency of each character in a string.
f="Developers"
freq={}
for ch in f:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print("The frequency of each character in a string:",freq)

# 7. Remove all duplicate characters from a string.
g="pythonprogramming"
duplicates=""
for ch in g:
    if ch not in duplicates:
        duplicates+=ch
print("duplicate characters from a string:",duplicates)
        
# 8. Find the longest word in a sentence.
f="Python is an interpreted programming language"
words=f.split()
longest=""
for ch in words:
    if len(ch)>len(longest):
        longest=ch
print("The longest word:",longest)

# 9. Count how many times each word appears in a string.
text="Python is a general purpose programming language known for its readability."
words=text.split()
freq={}
for ch in words:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

# 10. Replace all spaces in a string with -
h="Replace all spaces in a string with"
replace=""
for ch in h:
    if ch==" ":
        replace+="-"
    else:
        replace+=ch
print(replace)