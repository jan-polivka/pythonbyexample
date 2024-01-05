# Sometimes, you have to make decisions based on some condition
likes_ice_cream = True

if likes_ice_cream:
    print("I like ice cream")
else:
    print("I don't like ice cream")

# Sometimes, you like one flavour more than the other
ice_cream_flavour = "vanilla"

if ice_cream_flavour == "vanilla":
    print("I would like two scoops, please")
elif ice_cream_flavour == "chocolate":
    print("One scoop, please")
else:
    print("None for me, thank you")
# keyword elif allows you to specify further conditions
# and can be used multiple times

# You can also use the match-case matching
match ice_cream_flavour:
    case "vanilla":
        print("I would like two scoops, please")
    case "chocolate":
        print("One scoop, please")
    case _:
        print("None for me, thank you")
# the last case, _, is the default case, when there is no other match