import os

def create_files():
    # Get the number of files to create from the user
    num_files = int(input("Enter the number of files to create: "))

    # Get file extension from the user
    file_extension = input("Enter the file extension (e.g., txt, csv, etc.): ")

    # Create the specified number of files
    for i in range(1, num_files + 1):
        # Generate the file name
        file_name = str(i)

        # Combine file name and extension to create the full file name
        full_file_name = f"{file_name}.{file_extension}"

        # Check if the file already exists
        if os.path.exists(full_file_name):
            print(f"The file '{full_file_name}' already exists.")
        else:
            # Create the file
            with open(full_file_name, 'w') as file:
                print(f"File '{full_file_name}' created successfully.")

# Call the function to create files
create_files()

