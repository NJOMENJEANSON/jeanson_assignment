# COMMON_PASSWORDS = [
#     'password', '123456', '123456789', '12345', 'qwerty',
#     'abc123', 'password1', 'admin', 'welcome', 'letmein',
#     'monkey', 'football', 'iloveyou', '1234567', '123123',
#     'sunshine', 'master', 'hello', 'shadow', 'ashley',
#     'ninja', 'passw0rd', '1234', '12345678', '123456a'
# ]

# SPECIAL_CHARS = set('!@#$%^&*')

# def has_uppercase(password):
#     return any(c.isupper() for c in password)

# def has_lowercase(password):
#     return any(c.islower() for c in password)

# def has_number(password):
#     return any(c.isdigit() for c in password)

# def has_special_char(password):
#     return any(c in SPECIAL_CHARS for c in password)

# def analyze_password(password):
#     score = 0
#     feedback = []
#     suggestions = []
    
#     # Length check
#     if len(password) >= 8:
#         score += 20
#         feedback.append("✅ Length requirement (8+ chars)")
#     else:
#         feedback.append("❌ Too short (minimum 8 characters)")
#         suggestions.append("- Make your password at least 8 characters long")
    
#     # Character type checks
#     checks = [
#         (has_uppercase, "uppercase letters", "Add at least one uppercase letter"),
#         (has_lowercase, "lowercase letters", "Add at least one lowercase letter"),
#         (has_number, "numbers", "Include at least one number"),
#         (has_special_char, "special characters (!@#$%^&*)", "Add at least one special character (!@#$%^&*)")
#     ]
    
#     for check, description, suggestion in checks:
#         if check(password):
#             score += 20
#             feedback.append(f"✅ Contains {description}")
#         else:
#             feedback.append(f"❌ Missing {description}")
#             suggestions.append(f"- {suggestion}")
    
#     # Common password check
#     if password.lower() not in COMMON_PASSWORDS:
#         score += 20
#         feedback.append("✅ Not a common password")
#     else:
#         feedback.append("❌ Common password detected")
#         suggestions.append("- Avoid using common passwords")
#         suggestions.append("- Consider using a passphrase instead")
    
#     # Determine strength level
#     strength_levels = [
#         (40, "Weak"),
#         (60, "Fair"),
#         (80, "Good"),
#         (100, "Strong"),
#         (120, "Excellent")
#     ]
    
#     strength = next((level for threshold, level in strength_levels if score <= threshold), "Excellent")
    
#     return {
#         'score': score,
#         'strength': strength,
#         'feedback': feedback,
#         'suggestions': suggestions
#     }

# def main():
#     print("\n=== PASSWORD SECURITY ANALYZER ===")
#     password = input("Enter password to analyze: ")
    
#     results = analyze_password(password)
    
#     print("\n🔒 SECURITY ANALYSIS RESULTS")
#     print(f"Password: {password}")
#     print(f"Score: {results['score']}/120 ({results['strength']})")
#     print("\n".join(results['feedback']))
    
#     if results['suggestions']:
#         print("\n💡 SUGGESTIONS:")
#         print("\n".join(results['suggestions']))

# if __name__ == "__main__":
#     main()