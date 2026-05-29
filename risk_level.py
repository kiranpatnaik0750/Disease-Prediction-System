def detect_risk(symptoms):

    score = sum(symptoms)

    if score >= 8:
        return "HIGH"

    elif score >= 4:
        return "MEDIUM"

    else:
        return "LOW"