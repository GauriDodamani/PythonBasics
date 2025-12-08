#list
grocery_list =["bread","butter","paneer","milk"]
grocery_list[1]="cheese"   # replacing the item / updating
print(grocery_list)


#Tuples:
my_tuple=("tta.com","sdet.com")
print(my_tuple)                     #('tta.com', 'sdet.com')

#converting tuple to list
tuple_to_list=list(my_tuple)
tuple_to_list.append("google.com")      #added element
print(tuple_to_list)                #['tta.com', 'sdet.com', 'google.com']

#converting list to tuple
list_to_tuple=tuple(tuple_to_list)
print(list_to_tuple)                #('tta.com', 'sdet.com', 'google.com')



#empty tuple
t=()
print(t)     #()


# Real case, where we Tuples
API_URLSs = ("https://sdet.live/python0x", "https://awesomeqa.com", "https://thetestingacademy.com")
print(API_URLSs[0])      # https://sdet.live/python0x  -> index of 0
print(API_URLSs[1])      # https://awesomeqa.com   -> index of 1




#conversion of list to tuple
t1=tuple([123,456,789])
print(t1)     #(123, 456, 789)   -> round bracket


#matrix format:

t1=("Gauri","Dodamani")
t2=("Vinit"," Vilas","Ganpati")
new_tuple=(t1,t2)
print(new_tuple)        #(('Gauri', 'Dodamani'), ('Vinit', ' Vilas', 'Ganpati'))
print(new_tuple[0])     #('Gauri', 'Dodamani')
print(new_tuple[0][1])  # Dodamani
print(new_tuple[1][0])  # Vinit