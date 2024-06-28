import re


def check_password_strength(password):
    # Define the criteria for a strong password
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Calculate the strength score
    strength_score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_criteria
    ])

    # Provide feedback based on the strength score
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should contain at least one lowercase letter.")
    if not digit_criteria:
        feedback.append("Password should contain at least one digit.")
    if not special_criteria:
        feedback.append("Password should contain at least one special character (!@#$%^&*(),.?\":{}|<>).")

    return {
        "length_criteria": length_criteria,
        "uppercase_criteria": uppercase_criteria,
        "lowercase_criteria": lowercase_criteria,
        "digit_criteria": digit_criteria,
        "special_criteria": special_criteria,
        "strength": strength,
        "feedback": feedback
    }


def main():
    while True:
        password = input("Enter a password to check its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break
        result = check_password_strength(password)
        print(f"Password Strength: {result['strength']}")
        print("Criteria met:")
        print(f" - Length (>= 8 characters): {'Yes' if result['length_criteria'] else 'No'}")
        print(f" - Uppercase Letter: {'Yes' if result['uppercase_criteria'] else 'No'}")
        print(f" - Lowercase Letter: {'Yes' if result['lowercase_criteria'] else 'No'}")
        print(f" - Digit: {'Yes' if result['digit_criteria'] else 'No'}")
        print(f" - Special Character: {'Yes' if result['special_criteria'] else 'No'}")
        if result['feedback']:
            print("\nFeedback to improve your password:")
            for feedback in result['feedback']:
                print(f" - {feedback}")
        print("\n")


if __name__ == "__main__":
    main()
