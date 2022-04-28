from getpass import getpass

class Credentials():
    def get_olx_credentials(self):
        print("OLX Credentials")
        self.login_olx = input("Provide your email: ")
        self.password_olx = getpass("Provide your password: ")
    
    def get_allegro_lokalnie_credentials(self):
        print("Allegro lokalnie Credentials")
        self.login_allegro_lokalnie = input("Provide your email: ")
        self.password_allegro_lokalnie = getpass("Provide your password: ")
        
    def get_sprzedajemy_credentials(self):
        print("Sprzedajemy Credentials")
        self.login_sprzedajemy = input("Provide your email: ")
        self.password_sprzedajemy = getpass("Provide your password: ")
        
    def get_vinted_credentials(self):
        print("Vinted Credentials")
        self.login_vinted = input("Provide your email: ")
        self.password_vinted = getpass("Provide your password: ")