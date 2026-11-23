def cat_speak(phrase, mood="обычный"):
    if mood == "голодный":
        return phrase + " - МЯУ! Покорми!"
    elif mood == "довольный":
        return phrase + " - мур-мур..."
    else:
        return phrase
pass
print(cat_speak("Я проснулся", mood= "голодный"))
