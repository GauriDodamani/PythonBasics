# Find the first non-repeating character in a string using sets.
# swiss -> s -No , w - Answer
# string="swiss"
# print(string.count("s"))
# print(string.count("w"))
# print(string.count("i"))
#
# print("annushree".count("a"))
# print("annushree".count("n"))
# print("annushree".count("u"))  #another way to print the string for count etc


s = set()
#define/ declare the function
def non_repeating_char(string):
#logic:
    for char in string:
        if string.count(char) == 1 :
            s.add(char)
            return char

    return None

#calling the function
print("First non repeating character is : ",non_repeating_char("swiss"))    #w
print(non_repeating_char("annushree"))  #a
print(s)            #{'w', 'a'}