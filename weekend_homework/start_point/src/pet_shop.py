# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]

def get_total_cash(sum):
    return sum["admin"]["total_cash"]

def add_or_remove_cash(shop,pets_to_add):
    shop["admin"]["total_cash"] += pets_to_add

def increase_pets_sold(shop,pets_increase):
    shop["admin"]["pets_sold"] += pets_increase

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def get_stock_count(shop):
    return len(shop["pets"])

def get_pets_by_breed(shop, breed):
    pets =[]

    for pet in shop["pets"]:
        if pet["breed"] == breed:
            pets.append(pet)
    return pets

def find_pet_by_name(shop, name):

    for pet_name in shop["pets"]:
        if pet_name["name"] == name:  
            return pet_name
        
# def remove_pet_by_name(pet_shop, name):
#     name = find_pet_by_name(pet_shop,name)

#     for pet_name in pet_shop["pets"]:
#         if pet_name["name"] == name:
#             ["pet"].remove(name)

# def remove_pet_by_name(shop, name):

#     for pet_name in shop["pets"]:
#         if pet_name["name"] == name:  
#             return ["pet"].remove(name)..

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    return pet_shop, new_pet
      
def get_customer_cash(get_customer_cash):
    return get_customer_cash["cash"]

def remove_customer_cash(customer,cash):
    customer["cash"] -= cash
    return customer,cash

def customer_pet_count(number_of_pets):
    return len(number_of_pets["pets"])  

def add_pet_to_customer(pet):
    pet["pets"].append(pet)
    return len(get_customer_pet_count('pet'))

def customer_can_afford_pet(customer_money, cost_pet):
    for item in customer_money:
        if customer_money ["cash"] >= cost_pet["price"]:
            return True 
        else:
            return False