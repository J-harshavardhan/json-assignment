import json

# ==================================================
# Task 1 — Build a JSON Structure
# ==================================================

print("\n==================== Task 1 ======================\n")

user_profile = {
    "name": "J Harsha Vardhan",
    "age": 19,
    "email": "jharshavardhan28@gmail.com",
    "is_active": True,
    "skills": ["Python", "Machine Learning", "Artificial Intelligence"]
}

# Convert dictionary to formatted JSON string
user_json = json.dumps(user_profile, indent=4)

print("Task 1 Output:")
print(user_json)

print("\n==================================================\n")


# ==================================================
# Task 2 — Parse an API Response
# ==================================================

print("==================== Task 2 ======================\n")

api_response = '''
{
    "status": "success",
    "data": {
        "user_id": 101,
        "username": "alex99",
        "score": 87.5
    }
}
'''

# Convert JSON string to Python dictionary
parsed_data = json.loads(api_response)

username = parsed_data["data"]["username"]
score = parsed_data["data"]["score"]

print("Task 2 Output:")
print("Username:", username)
print("Score:", score)
print(f"User {username} scored {score} points")

print("\n==================================================\n")


# ==================================================
# Task 3 — Handle Nested JSON
# ==================================================

print("==================== Task 3 ======================\n")

nested_json = {
    "name": "Priya",
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka",
        "zip": "560001"
    }
}

# Extract city and zip
city = nested_json["address"]["city"]
zip_code = nested_json["address"]["zip"]

print("Task 3 Output:")
print("City:", city)
print("Zip Code:", zip_code)

# Add new key inside address
nested_json["address"]["country"] = "India"

print("\nUpdated JSON:")
print(json.dumps(nested_json, indent=4))

print("\n==================================================\n")