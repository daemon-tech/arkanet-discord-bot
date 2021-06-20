try:
    import os
    from time import sleep
except ModuleNotFoundError:
    print('Python3 missiing default modules!:')

def modules():  
    try:
        import dotenv
        import discord
        from time import sleep
        from dotenv import load_dotenv
        from discord.utils import get
        from discord.utils import get
        from dotenv import load_dotenv
        from discord.ext import commands
        from discord.utils import get
    except ModuleNotFoundError:
        try:
            if os.name == "nt":
                os.system("pip install discord.py")
                os.system("pip install python-dotenv")
            else:
                os.system("python3 -m pip install -U discord.py ")
                os.system("python3 -m pip install python-dotenv ")
            import dotenv
            import discord
            from time import sleep
            from dotenv import load_dotenv
            from discord.utils import get
            from discord.utils import get
            from dotenv import load_dotenv
            from discord.ext import commands
            from discord.utils import get
        except:
            modules()
modules()
print("Modules: Initialized") 
            
        