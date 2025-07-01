def generate_tip(city, issue, transport, electricity, language):
    tips = []

    if issue == "pollution":
        tips.append("Use public transport or carpool to reduce pollution.")
        tips.append("Wear masks and avoid peak hour travel.")
    elif issue == "water":
        tips.append("Fix leaking taps and limit shower time.")
        tips.append("Harvest rainwater if possible.")
    elif issue == "heat":
        tips.append("Plant trees or install reflective window covers.")
        tips.append("Stay hydrated and avoid daytime exposure.")
    elif issue == "flood":
        tips.append("Don’t litter; it blocks drainage.")
        tips.append("Raise electric sockets if you live in flood-prone areas.")
    else:
        tips.append("Be conscious of your daily carbon footprint.")

    if transport.lower() in ['car', 'bike']:
        tips.append("Try using bicycles or walking for nearby places.")
    elif transport.lower() in ['bus', 'metro']:
        tips.append("Great! Public transport lowers carbon emissions.")

    if int(electricity) > 300:
        tips.append("Reduce appliance use. Try LED bulbs and solar panels.")
    else:
        tips.append("Nice! Your electricity use is within safe limits.")

    tips.append("Small steps lead to a greener tomorrow! 🌱")

    return " ".join(tips)
