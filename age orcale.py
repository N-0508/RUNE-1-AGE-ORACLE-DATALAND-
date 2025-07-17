from datetime import datetime

def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    today = datetime.today()

    # Calculate the age
    age_years = today.year - birthdate.year
    age_months = today.month - birthdate.month
    age_days = today.day - birthdate.day

    # Adjust if birthday hasn't occurred yet this year
    if age_days < 0:
        age_months -= 1
        age_days += 30  # Approximate correction
    if age_months < 0:
        age_years -= 1
        age_months += 12

    return age_years, age_months, age_days

# 👇 Welcome to Dataland! Input your birthdate in DD-MM-YYYY format
user_birthdate = input("🧭 Welcome to Dataland! Enter your birthdate (DD-MM-YYYY): ")
years, months, days = calculate_age(user_birthdate)

print(f"🎂 You are {years} years, {months} months, and {days} days old in Dataland! 🧠")















