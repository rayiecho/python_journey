product = {
    "name" : "Shirt",
    "price" : 200,
    "in_stock" : "yes",
    "colour" : "white"
}

print(product["name"])
print(product["price"])
product["place"] = "Nairobi"
product["price"] = "350"
print(product.get("price"))
print(product["colour"])
product["design"] = "smart"
print(product["design"])