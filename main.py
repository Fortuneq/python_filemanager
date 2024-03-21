import os
import shutil
import zipfile
import tarfile
from settings import WORKING_DIRECTORY
#
#
def create_folder(folder_name):
    folder_path = os.path.join(WORKING_DIRECTORY, folder_name)
    os.mkdir(folder_path)


def delete_folder(folder_name):
    folder_path = os.path.join(WORKING_DIRECTORY, folder_name)
    os.rmdir(folder_path)


def move_to_folder(folder_name):
    global WORKING_DIRECTORY
    new_path = os.path.join(WORKING_DIRECTORY, folder_name)
    if os.path.isdir(new_path) and new_path.startswith(WORKING_DIRECTORY):
        WORKING_DIRECTORY = new_path
    else:
        print("Folder not found or outside working directory.")


def list_files():
    files = os.listdir(WORKING_DIRECTORY)
    for file in files:
        print(file)


def create_file(file_name):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    with open(file_path, "w") as file:
        pass


def write_to_file(file_name, text):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    with open(file_path, "w") as file:
        file.write(text)


def read_file(file_name):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    with open(file_path, "r") as file:
        print(file.read())


def delete_file(file_name):
    file_path = os.path.join(WORKING_DIRECTORY, file_name)
    os.remove(file_path)


def copy_file(source_file, destination_folder):
    source_path = os.path.join(WORKING_DIRECTORY, source_file)
    destination_path = os.path.join(WORKING_DIRECTORY, destination_folder, source_file)
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)


def move_file(source_file, destination_folder):
    source_path = os.path.join(WORKING_DIRECTORY, source_file)
    destination_path = os.path.join(WORKING_DIRECTORY, destination_folder, source_file)
    if os.path.exists(source_path):
        shutil.move(source_path, destination_path)


def rename_file(old_name, new_name):
    old_path = os.path.join(WORKING_DIRECTORY, old_name)
    new_path = os.path.join(WORKING_DIRECTORY, new_name)
    os.rename(old_path, new_path)


def archive_files(files_to_archive, archive_name):
    with zipfile.ZipFile(archive_name + '.zip', 'w') as zipf:
        for file in files_to_archive:
            zipf.write(os.path.join(WORKING_DIRECTORY, file), file)


def extract_archive(archive_name):
    with zipfile.ZipFile(archive_name + '.zip', 'r') as zipf:
        zipf.extractall(WORKING_DIRECTORY)


def disk_quota():
    total, used, free = shutil.disk_usage(WORKING_DIRECTORY)
    print(f"Total space: {total} bytes")
    print(f"Used space: {used} bytes")
    print(f"Free space: {free} bytes")
#
#
# if __name__ == "__main__":
#     while True:
#         try:
#             print("File Manager Menu:")
#             print("1. Create Folder")
#             print("2. Delete Folder")
#             print("3. Move to Folder")
#             print("4. List Files")
#             print("5. Create File")
#             print("6. Write to File")
#             print("7. Read File")
#             print("8. Delete File")
#             print("9. Copy File")
#             print("10. Move File")
#             print("11. Rename File")
#             print("12. Archive Files")
#             print("13. Extract Archive")
#             print("14. Disk Quota")
#             print("15. Exit")
#
#             choice = input("Enter your choice: ")
#
#             if choice == "1":
#                 folder_name = input("Enter folder name: ")
#                 create_folder(folder_name)
#             elif choice == "2":
#                 folder_name = input("Enter folder name: ")
#                 delete_folder(folder_name)
#             elif choice == "3":
#                 folder_name = input("Enter folder name: ")
#                 move_to_folder(folder_name)
#             elif choice == "4":
#                 list_files()
#             elif choice == "5":
#                 file_name = input("Enter file name: ")
#                 create_file(file_name)
#             elif choice == "6":
#                 file_name = input("Enter file name: ")
#                 text = input("Enter text to write to the file: ")
#                 write_to_file(file_name, text)
#             elif choice == "7":
#                 file_name = input("Enter file name: ")
#                 read_file(file_name)
#             elif choice == "8":
#                 file_name = input("Enter file name: ")
#                 delete_file(file_name)
#             elif choice == "9":
#                 source_file = input("Enter source file name: ")
#                 destination_folder = input("Enter destination folder name: ")
#                 copy_file(source_file, destination_folder)
#             elif choice == "10":
#                 source_file = input("Enter source file name: ")
#                 destination_folder = input("Enter destination folder name: ")
#                 move_file(source_file, destination_folder)
#             elif choice == "11":
#                 old_name = input("Enter current file name: ")
#                 new_name = input("Enter new file name: ")
#                 rename_file(old_name, new_name)
#             elif choice == "12":
#                 files_to_archive = input("Enter files to archive (comma separated): ").split(',')
#                 archive_name = input("Enter archive name: ")
#                 archive_files(files_to_archive, archive_name)
#             elif choice == "13":
#                 archive_name = input("Enter archive name to extract: ")
#                 extract_archive(archive_name)
#             elif choice == "14":
#                 disk_quota()
#             elif choice == "15":
#                 break
#             else:
#                 print("Invalid choice. Please try again.")
#         except Exception as e:
#             print(f"An error occurred: {e}")


import tkinter as tk
from tkinter import messagebox

def handle_choice(choice):
    if choice == "Create Folder":
        folder_name = entry.get()
        create_folder(folder_name)
    elif choice == "Delete Folder":
        folder_name = entry.get()
        delete_folder(folder_name)
    elif choice == "Move to Folder":
        folder_name = entry.get()
        move_to_folder(folder_name)
    elif choice == "List Files":
        files = list_files()
        file_list.delete(0, tk.END)
        for file in files:
            file_list.insert(tk.END, file)
    elif choice == "Create File":
        file_name = entry.get()
        create_file(file_name)
    elif choice == "Write to File":
        file_name = entry.get()
        text = text_entry.get("1.0", tk.END)
        write_to_file(file_name, text)
    elif choice == "Read File":
        file_name = entry.get()
        read_file(file_name)
    elif choice == "Delete File":
        file_name = entry.get()
        delete_file(file_name)
    elif choice == "Copy File":
        source_file = entry.get()
        destination_folder = text_entry.get("1.0", tk.END).strip()
        copy_file(source_file, destination_folder)
    elif choice == "Move File":
        source_file = entry.get()
        destination_folder = text_entry.get("1.0", tk.END).strip()
        move_file(source_file, destination_folder)
    elif choice == "Rename File":
        old_name = entry.get()
        new_name = text_entry.get("1.0", tk.END).strip()
        rename_file(old_name, new_name)
    elif choice == "Archive Files":
        files_to_archive = entry.get().split(',')
        archive_name = text_entry.get("1.0", tk.END).strip()
        archive_files(files_to_archive, archive_name)
    elif choice == "Extract Archive":
        archive_name = entry.get()
        extract_archive(archive_name)
    elif choice == "Disk Quota":
        disk_quota()

def on_button_click(choice):
    handle_choice(choice)
    messagebox.showinfo("Operation Completed", f"{choice} operation completed.")

root = tk.Tk()
root.title("File Manager")

label = tk.Label(root, text="Enter your choice:")
label.pack()

entry = tk.Entry(root)
entry.pack()

text_label = tk.Label(root, text="Enter additional information (if needed):")
text_label.pack()

text_entry = tk.Text(root, height=5, width=30)
text_entry.pack()

choices = [
    "Create Folder",
    "Delete Folder",
    "Move to Folder",
    "List Files",
    "Create File",
    "Write to File",
    "Read File",
    "Delete File",
    "Copy File",
    "Move File",
    "Rename File",
    "Archive Files",
    "Extract Archive",
    "Disk Quota"
]
for choice in choices:
    button = tk.Button(root, text=choice, command=lambda c=choice: on_button_click(c))
    button.pack()

file_list_label = tk.Label(root, text="Files in the selected folder:")
file_list_label.pack()

file_list = tk.Listbox(root, height=10, width=50)
file_list.pack()

root.mainloop()



root.mainloop()
