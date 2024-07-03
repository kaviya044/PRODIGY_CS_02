import re
def password_complexity_checker(password):
    # Initialize the score
    score = 0
    complexity = {
        'length': False,
        'uppercase': False,
        'lowercase': False,
        'digits': False,
        'special': False
    }

    # Check length
    if len(password) >= 8:
        score += 1
        complexity['length'] = True

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        complexity['uppercase'] = True

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        complexity['lowercase'] = True

    # Check for digits
    if re.search(r'[0-9]', password):
        score += 1
        complexity['digits'] = True

    # Check for special characters
    if re.search(r'[\W_]', password):
        score += 1
        complexity['special'] = True

    # Determine complexity level
    if score == 5:
        complexity_level = 'Very Strong'
    elif score == 4:
        complexity_level = 'Strong'
    elif score == 3:
        complexity_level = 'Moderate'
    elif score == 2:
        complexity_level = 'Weak'
    else:
        complexity_level = 'Very Weak'

    return {
        'password': password,
        'score': score,
        'complexity': complexity,
        'complexity_level': complexity_level
    }

# Test the function
if __name__ == "__main__":
    password = input("Enter a password to check its complexity: ")
    result = password_complexity_checker(password)
    print(f"Password: {result['password']}")
    print(f"Score: {result




