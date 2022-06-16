admin="jason"

def deco1(username):
    def deco2(func):
        def wrapper():
            if username==admin:
                return func()
            else:
                print("Accès refusée")
        return wrapper
    return deco2

@deco1("jason")
def profile():
    print("Mon profil")

help(profile)