def get_prices(price_list):
    lst1 = []
    for i in price_list:
        beginning_index = i.find("$") + 1
        ending_index = i.find(")", beginning_index)
        lst1.append(i[beginning_index:ending_index])
    print(lst1)
get_prices(["salad ($4.99)"])
get_prices([
    "artichokes ($1.99)",
    "rotisserie chicken ($5.99)",
    "gum ($0.75)"
])
get_prices([
    "ice cream ($5.99)",
    "banana ($0.20)",
    "sandwich ($8.50)",
    "soup ($1.99)"
])