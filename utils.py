# utils.py
import re
import hashlib
import requests
import math

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password):
        charset += 26
    if re.search(r'[A-Z]', password):
        charset += 26
    if re.search(r'[0-9]', password):
        charset += 10
    if re.search(r'[^a-zA-Z0-9]', password):
        charset += 32
    if charset == 0:
        return 0
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

def check_breach(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    url = f'https://api.pwnedpasswords.com/range/{prefix}'
    response = requests.get(url)
    if response.status_code != 200:
        return -1
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

def evaluate_strength(password):
    score = 0
    rules = {
        'length': len(password) >= 12,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'[0-9]', password)),
        'symbol': bool(re.search(r'[^a-zA-Z0-9]', password))
    }
    for rule in rules.values():
        if rule:
            score += 1

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, rules

def suggest_improvements(rules):
    suggestions = []
    if not rules['length']:
        suggestions.append("Use at least 12 characters.")
    if not rules['uppercase']:
        suggestions.append("Add uppercase letters.")
    if not rules['lowercase']:
        suggestions.append("Add lowercase letters.")
    if not rules['digit']:
        suggestions.append("Include numbers.")
    if not rules['symbol']:
        suggestions.append("Use special characters.")
    return suggestions
