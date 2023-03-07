# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop_name):
    return pet_shop_name["name"]

def get_total_cash(sum):
    return sum["admin"]["total_cash"]

def add_or_remove_cash(shop,amount):
    shop["admin"]["total_cash"] += amount
    # shop["admin"]["total_cash"] = shop["admin"]["total_cash"] + amount

def get_pets_sold(pets_shop):
    return pets_shop["admin"]["pets_sold"]

def increase_pets_sold(shop,pets_increase):
    shop["admin"]["pets_sold"] += pets_increase

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
     # return none -could also be used here to display none if that bed want found
        
def remove_pet_by_name(pet_shop, name):
    
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)
    # return pet_shop, new_pet not needed here
      
def get_customer_cash(get_customer_cash):
    return get_customer_cash["cash"]

def remove_customer_cash(customer,cash):
    customer["cash"] -= cash
    return customer,cash

def get_customer_pet_count(number_of_pets):
    return len(number_of_pets["pets"])  

def add_pet_to_customer(get_customer_pet_count,new_pet):
    get_customer_pet_count["pets"].append(new_pet)
    return len(get_customer_pet_count["pets"])

# def add_pet_to_customer(customer, pet):
#     customer["pets"].append(pet)

# solution provided by codeclan

def customer_can_afford_pet(customer_money, cost_pet):
    for item in customer_money:
        if customer_money ["cash"] >= cost_pet["price"]:
            return True 
        else:
            return False

# return customer_money ["cash"] >= cost_pet["price"]
# codeclan solution compared to mine