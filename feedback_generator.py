def analyze_confession(text):
    feedback = []

    confession = text.lower()

    if "ac" in confession or "air conditioner" in confession:
        feedback.append("Running the AC 24/7? Congratulations, you've personally cooled the North Pole 🥶.")

    if "meat" in confession or "chicken" in confession or "mutton" in confession or "bacon" in confession:
        feedback.append("Meat every day? The cows have started a petition against you. 🐄🌍")

    if "plastic" in confession or "bottle" in confession or "bag" in confession:
        feedback.append("Still using plastic? Even sea turtles are side-eyeing you right now 🐢👀.")

    if "car" in confession and "alone" in confession:
        feedback.append("Driving alone? Why not just adopt a smokestack at this point 🚗💨.")

    if "lights" in confession and ("on" in confession or "leave" in confession):
        feedback.append("Leaving the lights on? Wow, Edison must be so proud ⚡💸.")

    if "fan" in confession and "on" in confession:
        feedback.append("Leaving the fan on for ghosts, are we? 👻 They appreciate the breeze.")

    if "water" in confession and ("waste" in confession or "long shower" in confession):
        feedback.append("Taking hour-long showers? Aquaman called. He wants a word 🚿🐠.")

    if "fast fashion" in confession or "shopping" in confession or "sale" in confession:
        feedback.append("Retail therapy is fun — until the planet sends you the bill 🛍️🌡️.")

    if "food waste" in confession or "throw" in confession and "food" in confession:
        feedback.append("Wasting food? The planet’s crying and so is your fridge 🥲🥬.")

    if not feedback:
        feedback.append("You're either a climate angel 😇 or you're hiding something... confess more!")

    # Add a closing punch
    feedback.append("Start making amends today 🌍. The penguins are watching 🐧.")

    return "\n".join(feedback)