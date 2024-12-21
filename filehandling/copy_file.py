def copy_file(src_path, dest_path):
    with open(src_path, 'r') as src:  # Open the source file in read mode
        with open(dest_path, 'w') as dest:  # Open the destination file in write mode
            for line in src:  # Iterate through each line in the source file
                dest.write(line)  # Write the line to the destination file

    print(f"Contents copied from '{src_path}' to '{dest_path}'.")

# Example usage
src = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\src.txt.txt"
dest = r"C:\Users\Y.Rakesh Yadav\OneDrive\Desktop\dest.txt.txt"
copy_file(src, dest)
