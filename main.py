from password_manager import *

def main():
    while True:
        print("1. Add a new password")
        print("2. Get a password")
        print("3. Update a password")
        print("4. Clear all existing passwords")
        print("5. Exit\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            
            print_existing_websites()
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_status = add_password(website, username, password)
            if (add_status):
                print("Password added successfully.\n")
           
        elif choice == '2':

            print_existing_websites()
            website = input("Enter website: ")
            password = get_password(website)
            if password:
                print(f"Password for {website}: {password}\n")
            else:
                print(f"No password found for {website}\n")
        
        elif choice == '3':
            print_existing_websites()
            website_to_update = input("\nEnter the website you wish to change the password for: ")
            if (website_exists(website_to_update)):
                new_password = input("\nEnter the new password: ")
                update_password(website_to_update, new_password)
                print("\nPassword updated succesfully.")
                
            else:
                print("This website does not exist in the database.\n")


        elif choice == '4':

            confirm = input("Are you sure you want to clear all passwords? (Input Y or N): ")
            confirm = confirm.lower()
            if confirm == "y":
                clear_table()
                print("All passwords cleared\n")
            elif confirm == "n":
                print("Operation cancelled, passwords were NOT cleared\n")
            else:
                print("Invalid input, passwords were NOT cleared\n")


        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()