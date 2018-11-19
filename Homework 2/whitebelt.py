shopping_cart=[]
Guitar=1000
Pick_box=5
Guitar_Strings=10
def checkout(shopping_cart):
    if len(shopping_cart)==0:
        return("The list is empty")
    else:
        return sum(shopping_cart)

