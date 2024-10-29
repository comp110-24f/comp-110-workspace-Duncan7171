"""Examples of dictionary syntax with Ice Cream Shop order tallies."""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}


print(len(ice_cream))

ice_cream["mint"] = 10

mint_orders: int = ice_cream["mint"]
print(mint_orders)


# These mean the exact same thing
# changing mints value
ice_cream["mint"] = ice_cream["mint"] + 1
ice_cream["mint"] += 1

# Getting rid of value
ice_cream.pop("strawberry")

# Test if a key is in the dictionary
print("strawberry" in ice_cream)
print("vannilla" in ice_cream)

for flavor in ice_cream:
    tally: int = ice_cream[flavor]
    print(f"{flavor}: {tally}")
