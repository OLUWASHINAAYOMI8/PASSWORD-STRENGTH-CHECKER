import re

def check_password_strength(password):
    """Checks the strength of a password and provides feedback."""
    strength = 0
    feedback = []

    # Check password criteria
    if len(password) >= 12:
        strength += 1
    else:
        feedback.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Add a number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add a special character.")

    # Determine password strength level
    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }
    strength_description = strength_levels[strength]

    return strength, strength_description, feedback

# Example usage
password = input("Enter your password: ")
strength, description, feedback = check_password_strength(password)

print(f"Password Strength: {strength}/5 ({description})")
if feedback:
    print("Suggestions to improve your password:")
    for suggestion in feedback:
        print("-", suggestion)