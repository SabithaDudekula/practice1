# 1. Reverse a string without slicing
s=input("Enter the string:")
a=""
for ch in s:
    a=ch+a
print(a)

# 2. Check if a string is a palindrome
s="sabitha"
a=""
for ch in s:
    a=ch+a
if s==a:
    print("Palindrome")
else:
    print("Not a palindrome")

# 3. Count vowels and consonants in a string.
s="python programming"
vowels=""
consonants=""
for ch in s:
    if ch in "aeiouAEIOU":
        vowels+=ch
    else:
        consonants+=ch
print("vowels:",vowels)
print("consonants:",consonants)

# 4. Remove duplicates from a string.
s="Programming"
unique_one=""
for ch in s:
    if ch not in unique_one:
        unique_one+=ch
print("Unique:",unique_one)

# 5. Find the most frequent character in a string.
s="programming"
frequent=""
max_count=0
for ch in s:
    if s.count(ch)>max_count:
        max_count=s.count(ch)
        frequent=ch
print("Frequent character:",frequent)
print("count:",max_count)

# 6. Remove all spaces from a string.
s="Python is a hybrid programming language"
no_space=""
for ch in s:
    if ch!=" ":
        no_space+=ch
print(no_space)

# 7. Check if a string contains only digits.
s="123456"
digits=True
for ch in s:
    if ch<'0' or ch>'9':
        digits=False
        break
if digits:
    print("string contains digits")
else:
    print("strings do not contain digits")

# 8. Find longest word in a sentence
s="Python is a hybrid programming language"
longest=""
for ch in s.split():
    if len(ch)>len(longest):
        longest=ch
print(longest)

# 9. Find first non-repeating character
s="programming"
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
non_repeating=None
for ch in s:
    if freq[ch]==1:
        non_repeating=ch
        break
if non_repeating:
    print(non_repeating)
else:
    print("no")

# 10. Replace all occurrences of a character in a string.
s = "python programming"
freq = {}
for ch in s:
    if ch != " ":  # optional: ignore spaces
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
result = ""
for ch in s:
    if ch != " " and freq[ch] > 1:  # replace if occurs more than once
        result += "*"
    else:
        result += ch

print("Modified string:", result)

# 11. Convert a sentence to title case manually.
s="python is fun language"
capitalize=True
result=""
for ch in s:
    if ch==" ":
        result+=ch
        capitalize=True
    elif capitalize:
        result+=ch.upper()
        capitalize=False
    else:
        result+=ch.lower()
print(result)

# 12. Check if two strings are anagrams.
a="madam"
b="damma"
res1={}
res2={}
for x in a:
    res1.setdefault(x,0)
    res1[x]+=1
for x in b:
    res2.setdefault(x,0)
    res2[x]+=1
if res1==res2:
    print("anagrams")
else:
    print("Not anagrams")

# 13. Reverse words in a sentence.
s="Python is a hybrid programming language"
word=''
result=''
for ch in s+" ":
    if ch!=" ":
        word+=ch
    else:
        result=word+" "+result
        word=''
print(result.strip())

# 14. Count the number of words in a string without split().
s="Python is a hybrid programming language"
count=1
for ch in s:
    if ch==" ":
        count+=1
print("No.of words=",count)

# 15.Implement atoi() (string to integer conversion).
s="123456"
result=0
for ch in s:
    if '0'<=ch<='9':
        digit=ord(ch)-ord('0')
        result=result*10+digit
    else:
        print("Invalid",ch)
        break
print(result)
