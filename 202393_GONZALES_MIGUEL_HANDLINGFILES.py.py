products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

#Problem 1: Product Information Lookup
def get_product(code):
    if code in products:
        return products [code]
    else:
        return "Invalid Input"

get_product("americano")

#Problem 2: Product Property Lookup
def get_property (code,property):
    if code in products and property in products [code]:
        return products [code][property]
    else:
        return "Inavalid Input"

get_property("frappuccino","price")

# Problem 3:The Point-of-Sale Terminal
def main():
    f=open("receipt.txt","w")

    while True:
        code = input("{product_code},{quantity}")
        if code == "/":
            break
        elif code.split(",")[0] in products:
            get_product(code.split(",")[0]).setdefault("amount", 0)
            get_product(code.split(",")[0])["amount"] += int(code.split(",")[1])
        else:
            f.write("invalid input please try again")
    total = 0
    f.write("==")
    f.write("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL")
    for coffees in products:
        get_product(coffees).setdefault("amount", 0)
    for coffees in products:
        if get_product(coffees)["amount"] != 0:
            f.write(coffees + " \t\t"+ get_property(coffees, "name") + " \t\t" + str(get_property(coffees, "amount")) + "\t\t\t\t" +  str(get_property(coffees, "price") * get_property(coffees, "amount")))
            total += get_property(coffees, "amount") * get_property(coffees, "price")
    f.write("\nTotal:\t\t\t\t\t\t\t\t\t\t" + str(total))
    f.write("==")



main()
