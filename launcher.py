from os import system

def load_modules():
    system("python3 lib/modules.py")
    print("Modules: Loaded")
    
def bot():
    system("python3 lib/db/arkanet.py")

if __name__ == "__main__":
    load_modules()
    bot()
    