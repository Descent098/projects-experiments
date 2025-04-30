from user_library import User


k = User.create_user("Kieran", 26, "kieran@canadiancoding.ca")
print(f"Here is me: {k}")

r:list[User] = []
for i in range(10):
    r.append(User.create_random_user())

from pprint import pprint
pprint(r)

