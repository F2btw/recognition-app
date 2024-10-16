import tkinter as tk
from tkinter import filedialog

def get_file_path():
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open the file dialog and get the file path
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("All Files", "*.*")]  # You can specify file types here
    )

    # Check if a file was selected
    if file_path:
        print(f"Selected file: {file_path}")
    else:
        print("No file selected.")

    return file_path

# Example usage
file_path = get_file_path()

if __name__ == "__main__":
    print(file_path)




