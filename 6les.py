users = [
    {"name": "Alex","age":34},
    {"name": "Nick", "age": 35},
    {"name": "Sasha", "age": 21},
    {"name": "Max", "age": 55},
    ]
users.sort(key=lambda x: x.get("age"))
print(users)