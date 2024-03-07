import os

def list_dir_contents(path):
  """Lists directories and files in a specified path."""
  try:
    for entry in os.listdir(path):
      full_path = os.path.join(path, entry)
      if os.path.isdir(full_path):
        print(f"Directory: {entry}")
      else:
        print(f"File: {entry}")
  except FileNotFoundError:
    print(f"Error: Path '{path}' does not exist.")

def check_access(path):
  """Checks existence, readability, writability, and executability of a path."""
  if os.path.exists(path):
    print(f"Path '{path}' exists.")
    if os.access(path, os.R_OK):
      print(f"Path is readable.")
    if os.access(path, os.W_OK):
      print(f"Path is writable.")
    if os.access(path, os.X_OK):
      print(f"Path is executable.")
  else:
    print(f"Path '{path}' does not exist.")

def test_path_and_parts(path):
  """Tests path existence and gets filename/directory parts."""
  if os.path.exists(path):
    print(f"Path '{path}' exists.")
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
  else:
    print(f"Path '{path}' does not exist.")

def count_lines(file_path):
  """Counts the number of lines in a text file."""
  if os.path.exists(file_path):
    with open(file_path, "r") as file:
      lines = file.readlines()
      line_count = len(lines)
      print(f"Number of lines: {line_count}")
  else:
    print(f"Error: File '{file_path}' does not exist.")

def write_list_to_file(list_data, file_path):
  """Writes a list to a file."""
  with open(file_path, "w") as file:
    for item in list_data:
      file.write(f"{item}\n")

def generate_text_files():
  """Generates 26 text files named A.txt to Z.txt."""
  for letter in string.ascii_uppercase:
    file_path = f"{letter}.txt"
    with open(file_path, "w") as file:
      file.write(f"This is file {letter}.txt\n")

# Example usage (replace with your desired operations)
# list_dir_contents("/path/to/your/directory")
# check_access("/path/to/your/file")
# test_path_and_parts("/path/to/your/file.txt")
# count_lines("/path/to/your/text_file.txt")
# write_list_to_file(["Item 1", "Item 2", "Item 3"], "my_list.txt")
# generate_text_files()  # Uncomment to generate files

