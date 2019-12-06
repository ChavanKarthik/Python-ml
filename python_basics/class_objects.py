class user:
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday


user = user("Ram", '18830101')
print(user.name)
print(user.birthday)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
p2 = Person("Benny", 45)
p3 = Person("aston", 24)

print(p1.name)


class Sports:
    def __init__(self, name, number_of_players):
        self.name = name
        self.number_of_players = number_of_players
        self.type_of_event = 'Indoor game'


game1 = Sports('Badminton', 2)

print(f'name : {game1.name} \nnumber_of_players : {game1.number_of_players} \ntype_of_event : {game1.type_of_event}')
