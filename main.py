import os

while True:

    print("\n===== AI FITNESS COACH =====")
    print("1. Bicep Curl Counter")
    print("2. Squat Counter")
    print("3. Push-Up Counter")
    print("4. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":

        os.system(
            "python pose_test.py"
        )

    elif choice == "2":

        os.system(
            "python squat_counter.py"
        )

    elif choice == "3":

        os.system(
            "python pushup_counter.py"
        )

    elif choice == "4":

        print("Goodbye!")
        break

    else:

        print("Invalid Choice")