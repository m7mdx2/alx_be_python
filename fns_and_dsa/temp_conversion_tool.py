def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty shopping list
    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ")  # Get the user's choice

        if choice == '1':
            # Adding an item to the shopping list
            item_to_add = input("Enter the item to add: ")
            shopping_list.append(item_to_add)  # Add the item to the list
            print(f"'{item_to_add}' has been added to the shopping list.")

        elif choice == '2':
            # Removing an item from the shopping list
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)  # Remove the item if it exists
                print(f"'{item_to_remove}' has been removed from the shopping list.")
            else:
                print(f"'{item_to_remove}' not found in the shopping list.")

        elif choice == '3':
            # Viewing the shopping list
            if shopping_list:
                print("Current shopping list:")
                for item in shopping_list:
                    print(f"- {item}")  # Print each item in the list
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            # Exiting the program
            print("Goodbye!")
            break  # Exit the loop, ending the program

        else:
            # Handling invalid choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
