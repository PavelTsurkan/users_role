import setup
from managment_roles.models import *


users = []

role = Role()
user = User()

admin = Role.objects.get(id=1)
user = Role.objects.get(id=2)

while True:
    ans = int(input("1 - add role\n2 - add user\n"))

    if ans == 1:
        # admin = Role(name='admin')
        # user = Role(name='user')
        

        admin.save()
        user.save()

    elif ans == 2:
        users.append(User(name=input("Name: "), email=input("Email: "), role=admin))

    else:
        break


for user in users:
    user.save()


print(users)
    