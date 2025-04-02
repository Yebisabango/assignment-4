def handle_file_error():
    # Ask the user for a filename
    filename = input("Please enter the filename you want to read: ")
    
    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("File content read successfully:")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

