# shopping_list_manager.py

def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    
def add_item(shopping_list):
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in your shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("\nYour shopping list:")
        for index, item in enumerate(shopping_list, 1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is empty.")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting the shopping list manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
