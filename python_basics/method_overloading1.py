class Signup:

    def via_email(self, name='default name', contact='default contact', email='default email'):
        print("name = ", name, "contact = ", contact, "email = ", email)


obj = Signup()
obj.via_email()
obj.via_email('HI', 'Hello', 'World')
