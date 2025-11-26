print("Hello world this is my first program")

# print(self, *args, sep=' ', end='\n', file=None):

#by default it will add space in btwn each arguments
print("Gauri",123,3.14,True,"ABC")

#sep='' it is always added in the end of the arguments and not in fornt or in between
print("Gauri",123,3.14,True,"ABC",sep='@')

#end='\n' end of the file and next o/p will print in new line
print("Gauri",123,3.14,True,"ABC",sep=' ',end='-')
print("Gauri",123,3.14,True,"ABC",sep='@',end='\n')
# known special case of print
'''
Prints the values to a stream, or to sys.stdout by default.

  sep
    string inserted between values, default a space.
  end
    string appended after the last value, default a newline.
  file
    a file-like object (stream); defaults to the current sys.stdout.
  flush
    whether to forcibly flush the stream.
'''


#Indentation error
#    print("Gauri",123,3.14,True,"ABC")
#Right click on code file -> select reformat code

print("Gauri",123,3.14,True,"ABC")
