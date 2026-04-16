
def load_data():
    languages = []
    levels = []
    num_booked = []

    try:
        with open("bookings.txt", "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    languages.append(parts[0].strip())
                    levels.append(int(parts[1].strip()))
                    num_booked.append(int(parts[2].strip()))
    except FileNotFoundError:
        print("bookings.txt not found. Starting with empty lists.")

    return languages, levels, num_booked


def save_data(languages, levels, num_booked):
    with open("bookings.txt", "w") as file:
        for i in range(len(languages)):
            file.write(f"{languages[i]},{levels[i]},{num_booked[i]}\n")


def show_languages(languages, levels):
    lang_dict = {}
    for i in range(len(languages)):
        lang = languages[i]
        lvl = str(levels[i])
        if lang not in lang_dict:
            lang_dict[lang] = []
        lang_dict[lang].append(lvl)

    print("\n--- Available Languages ---")
    for lang, lvls in lang_dict.items():
        print(f"{lang} Levels: {' '.join(lvls)}")


def answer_enquiry(languages, levels, num_booked):
    lang_interest = input("\nEnter language: ").strip().capitalize()

    available_levels = []
    has_classes = False

    for i in range(len(languages)):
        if languages[i].capitalize() == lang_interest:
            has_classes = True
            if num_booked[i] < 20:
                available_levels.append(levels[i])

    if not has_classes:
        print(f"There are currently no classes in {lang_interest}.")
    elif len(available_levels) > 0:
        print("Currently there is space in:")
        for lvl in available_levels:
            print(f"{lang_interest} Level {lvl}")
    else:
        print(f"There are classes in {lang_interest}, but they are fully booked.")


def book_place(languages, levels, num_booked):
    name = input("\nEnter student name: ").strip()
    student_id = input("Enter student id: ").strip()
    lang = input("Enter language: ").strip().capitalize()

    try:
        level = int(input("Enter level: ").strip())
    except ValueError:
        print("Invalid level. Must be a number.")
        return

    found = False
    for i in range(len(languages)):
        if languages[i].capitalize() == lang and levels[i] == level:
            found = True
            if num_booked[i] < 20:
                num_booked[i] += 1
                print("\nBooking successful!")

                filename = f"{lang}{level}_{student_id}.txt"
                with open(filename, "w") as f:
                    f.write(f"Student Name: {name}\n")
                    f.write(f"Student ID: {student_id}\n")
                    f.write(f"Class: {lang} Level {level}\n")
                    f.write("Amount Owed: 200 Euros\n")
                print(f"Invoice saved to {filename} for the secretary.")
            else:
                print("Sorry, there is no space available in this class.")
            break

    if not found:
        print("Sorry, there is no class available for that language and level combination.")


def show_menu(languages, levels, num_booked):
    while True:
        print("\n--- Menu ---")
        print("1. Show languages")
        print("2. Show levels (Answer Enquiry)")
        print("3. Show Availability (Book a place)")
        print("4. Exit")

        choice = input("Select an option (1-4): ").strip()

        if choice == '1':
            show_languages(languages, levels)
        elif choice == '2':
            answer_enquiry(languages, levels, num_booked)
        elif choice == '3':
            book_place(languages, levels, num_booked)
        elif choice == '4':
            save_data(languages, levels, num_booked)
            print("Data saved successfully. Exiting program.")
            break
        else:
            print("Invalid choice. Please select from the menu.")


def main():
    languages, levels, num_booked = load_data()
    show_menu(languages, levels, num_booked)


if __name__ == "__main__":
    main()