def footwork1():
    print('Footwork should be like a spring')


class Badminton:
    def __init__(self):
        print('init of Badminton')

    def fitness(self):
        print('Fitness is the one of the important parameter')


class Football(Badminton):
    def __init__(self):
        print('init of Football')

    def footwork(self, email, age):
        self.email = email
        self.age = age
        print('I like footwork', self.email, self.age)

    def stamina(self):
        print('Should be able to run for longer time')


class VolleyBall(Football):
    def __init__(self):
        print('init of VolleyBall')

    def jumping(self):
        print('jump smash parameter')


kashyup = VolleyBall()
kashyup.jumping()
