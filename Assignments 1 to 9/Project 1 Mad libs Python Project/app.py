def mad_lib():
    print("Wellcome to the Mad Libs Generator!")

    adjective_1 = input("Enter an adjective : ")
    noun_1 = input("Enter a noun : ")
    verb_1 = input("Enter a verb : ")
    place = input("Enter a place : ")
    noun_2 = input("Enter another noun : ")
    adjective_2 = input("Enter another adjective : ")

    story = (
        f"One {adjective_1} morning, a {noun_1} woke up and decided to {verb_1}.\n"
        f"But instead of doing it at home, the {noun_1} rushed to {place} wearing a {adjective_2} hat!\n"
        f"On the way, the {noun_1} found a talking {noun_2} who offered them a free ride.\n"
        f"Everyone in {place} was shocked to see a {noun_1} and a {noun_2} singing and dancing together.\n"
        f"Since then, the {noun_1} became the superstar of {place}, and they lived happily, dancing every day!"
    )

    print(story)

if __name__ == "__main__":
    mad_lib()