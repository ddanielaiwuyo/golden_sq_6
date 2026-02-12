from datetime import date

def check_user_age(dob):
    date_of_birth = date.fromisoformat(dob)
    today = date.today()
    
    age = today - date_of_birth
    just_age = age.days // 365

    if just_age >= 16:
        return "Access granted"
    else:
        return f"Access denied. Your current age is {just_age} but the required age is 16."