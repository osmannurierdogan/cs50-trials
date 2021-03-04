def announce(f):
    def wrapper():
        print("About to run the function...")
        f() # Buraya @ işaretinden sonra çağırdığımız hello() fonksiyonu geliyor.
        print("Done with the function.")
    return wrapper

@announce
def hello():
    print("Hello, World")

hello()