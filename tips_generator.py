def generate_tip(city, issue, transport, electricity):
    tips = []

    # 🌍 Climate Issue Based Tips
    if issue == "pollution":
        tips.append("Your city doesn't need another cloud of exhaust! Take a deep breath—then take the bus.")
    elif issue == "water":
        tips.append("Every drop counts. Fix that leaky tap before it forms a lake in your guilt.")
    elif issue == "heat":
        tips.append("Feeling the burn? That's not summer, it's climate karma. Get those indoor plants and trees growing.")
    elif issue == "flood":
        tips.append("Water, water everywhere? Maybe start with not clogging drains with chips packets.")
    else:
        tips.append("Mother Earth called—she’s begging for some attention. Start anywhere, but start now.")

    # 🚗 Transport Mode Tips (Expanded + Sassy)
    t = transport.lower()
    if t in ['car', 'bike', 'scooter']:
        tips.append("Engines are so last season. Pedal power is the new cool. Go cycle chic!")
    elif t in ['bus', 'metro']:
        tips.append("Public transport? You're on the right track—literally. Bonus points for minimal emissions.")
    elif t == 'airplane':
        tips.append("Flying often? Each take-off burns more fuel than your entire apartment. Choose wisely.")
    elif t == 'ship':
        tips.append("Ships aren't saints either. Offset that carbon or consider local travel next time.")
    elif t in ['cycle', 'yulu bike']:
        tips.append("Look at you, eco-warrior! Silent wheels, cleaner skies. Keep rollin’ green!")
    else:
        tips.append("Transportation mystery? Choose the kind that doesn't make the planet sweat.")

    # ⚡ Electricity Usage Tips
    try:
        usage = int(electricity)
        if usage > 500:
            tips.append("Power guzzler alert! Your home’s glowing like Vegas. Time to unplug, literally.")
        elif usage > 300:
            tips.append("High usage spotted. Try energy-saving bulbs and maybe love natural light again?")
        else:
            tips.append("Efficient and elegant! You're giving the grid a breather.")
    except ValueError:
        tips.append("Couldn't decode your electricity usage. Try entering a number, eco champ!")

    return " ".join(tips)