SENTENCE_START : str = "Code in Place is fun. I learned to program and used Python to make my "

def main():

    adjective = input("Enter an adjective and press enter : ")
    noun = input("Enter an noun and press enter : ")
    verb = input("Enter an verb and press enter : ")

    print(SENTENCE_START + adjective + " " + noun  + " " + verb )

if __name__ == "__main__":
    main()    