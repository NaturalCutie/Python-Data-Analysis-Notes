def price_counting(cart):
    total_price = 0
    for price in cart:
        total_price += price
    discounted_price = 0.8 * total_price
    return total_price, discounted_price


result = price_counting([50, 30, 25, 15, 40])
print(result)
print(f"""
原价:{result[0]}元
优惠后:{result[1]}元""")
