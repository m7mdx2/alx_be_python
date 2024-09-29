
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty shopping list
    while True:
        display_menu()  # Show the menu to the user
        choice = input("Enter your choice: ")  # Get user input

        if choice == '1':
            # Prompt for and add an item
            item_to_add = input("Enter the item to add: ")
            shopping_list.append(item_to_add)  # Add item to the list
            print(f"'{item_to_add}' has been added to your shopping list.")

        elif choice == '2':
            # Prompt for and remove an item
            item_to_remove = input("Enter the item to remove: ")
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)  # Remove item from the list
                print(f"'{item_to_remove}' has been removed from your shopping list.")
            else:
                print(f"'{item_to_remove}' not found in the shopping list.")

        elif choice == '3':
            # Display the shopping list
            if shopping_list:  # Check if the list is not empty
                print("Current shopping list:")
                for item in shopping_list:
                    print(f"- {item}")  # Print each item
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            print("Goodbye!")  # Exit the program
            break  # Break out of the loop to end the program

        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    main()
