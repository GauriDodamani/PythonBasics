# Pizza Lovers
# Toppings - corn, paneer, olives, cheese, pineapple, jalapeno, capsicum


def pizza_lover(*toppings):
    print(toppings)

cust1 = pizza_lover("corn","cheese")
cust2 = pizza_lover("vegetable","cheese","olives","capsicum")
cust3 = pizza_lover("tomato")
cust4 = pizza_lover("pineapple","cheese")

'''
('corn', 'cheese')
('vegetable', 'cheese', 'olives', 'capsicum')
('tomato',)
('pineapple', 'cheese')

'''

