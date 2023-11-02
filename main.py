import scripts.csvmanip as ctd
import scripts.endecrypt as edc

HEADER = '''WELCOME TO PASSWORD MANAGER'''

MENU = '''\nX = EXIT\nN = ADD NEW USERNAME AND PASSWORD\nV = VIEW\nM = DISPLAY MENU'''

def main():

    print(HEADER)
    print(MENU)
    while True:

        inputvar = input("Enter input: \n")
        if inputvar.lower() == "x":
            break

        elif inputvar.lower() == "v":
            display = ctd.convertcsv()
            print(display)
            print()

        elif inputvar.lower() == "m":
            print(MENU + "\n")


if __name__ == "__main__":
    main()