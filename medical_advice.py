def get_advice(disease):

    viral = [
        "Dengue",
        "Chicken pox",
        "Common Cold",
        "Viral Fever",
        "Hepatitis A",
        "Hepatitis B",
        "Hepatitis C"
    ]

    bacterial = [
        "Typhoid",
        "Tuberculosis",
        "Pneumonia",
        "Urinary tract infection"
    ]

    parasitic = [
        "Malaria"
    ]

    chronic = [
        "Diabetes",
        "Hypertension",
        "Hypothyroidism",
        "Hyperthyroidism"
    ]

    skin = [
        "Acne",
        "Psoriasis",
        "Impetigo",
        "Fungal infection"
    ]

    if disease in viral:
        return "This may be a viral infection. Rest, drink fluids, and consult a doctor if symptoms worsen."

    elif disease in bacterial:
        return "This may be a bacterial infection. Medical consultation and antibiotics may be required."

    elif disease in parasitic:
        return "This disease may require specific antiparasitic treatment. Please visit a doctor."

    elif disease in chronic:
        return "This is a chronic condition. Regular medical monitoring and treatment are recommended."

    elif disease in skin:
        return "This appears to be a skin condition. Keep the affected area clean and consult a dermatologist."

    else:
        return "Consult a healthcare professional for proper diagnosis and treatment."