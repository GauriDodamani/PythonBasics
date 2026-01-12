#count the vowel in the string

string = input("Enter the string : ").lower()

vowels =["a","e","i","o","u"]


vowel_count=0
result= dict()

for char in string:
    if char in vowels:
        vowel_count = vowel_count + 1
        result[char] = result.get(char, 0) + 1

print("The vowel count is: ",vowel_count)

# for v in vowels:
#     print(f"{v}: {result.get(v, 0)}")


# ensure all vowels appear (even if count is 0)
for v in vowels:
    result.setdefault(v, 0)

print(result)

#input string
# o/p: a: , e:, i:, o:, u:


