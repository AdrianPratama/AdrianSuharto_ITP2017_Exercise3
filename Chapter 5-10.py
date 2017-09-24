current_users = ["Admin","Bruno","Claris","Devina","Eric"]
for x in current_users:
    x.lower()
new_users = ["Armin","Bruno","Clementine","Dean","Erica"]
for y in new_users:
    y.lower()

for i in new_users:
    if i in current_users:
        print("The username is taken!")
    else:
        print("The username is available")

