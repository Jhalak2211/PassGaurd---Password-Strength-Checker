# password_checker.py
from utils import evaluate_strength, calculate_entropy, check_breach, suggest_improvements

def main():
    print("\n🔐 Password Strength Checker + Breach Check 🔐\n")
    password = input("Enter your password: ")

    strength, rules = evaluate_strength(password)
    entropy = calculate_entropy(password)
    breach_count = check_breach(password)

    print(f"\nPassword Strength: {strength}")
    print(f"Entropy Score: {entropy} bits")

    if breach_count == -1:
        print("⚠️ Could not check for breaches. API error.")
    elif breach_count == 0:
        print("✅ This password has NOT been found in known breaches.")
    else:
        print(f"❌ This password has been found in {breach_count:,} breaches!")

    suggestions = suggest_improvements(rules)
    if suggestions:
        print("\nSuggestions to Improve:")
        for s in suggestions:
            print(f"- {s}")

if __name__ == '__main__':
    main()
