class motech:
    def __init__(self):
        print('init of motech')

    def states(self):
        print('states')

    def districts(self):
        print('districts')


class data:
    def __init__(self):
        print('init of data')

    def blocks(self):
        print('blocks')

    def talukas(self):
        print('talukas')


class services(motech, data):
    def __init__(self):
        super().__init__()  # initializes first parent __init__(uses 'super()')
        print('init of services')

    def facilities(self):
        print('facilities')

    def sub_facilities(self):
        print('sub_facilities')

    def heirarchy(self):
        super().states()
        super().districts()  # can call parent methods by super()
        self.talukas()  # or directly by self
        self.blocks()
        self.facilities()
        self.sub_facilities()


obj1 = services()
obj1.heirarchy()
