defaults = {"theme": "light",
            "audio": "on"}
user_pref = {"theme": "dark"}
print(f"User default value: {defaults}")
print(f"User prefer value:{user_pref}")
defaults.update(user_pref)
print(f"Updated Value with user pref: {defaults}")

