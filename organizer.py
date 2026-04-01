import os
import shutil

# 🔹 File type categories
file_types = {
    "Images": [".jpg", ".png",".jpeg"],
    "Videos": [".mp4"],
    "Documents": [".pdf", ".txt"]
}

# 🔹 Custom keywords
keywords = {
    "Math": ["math", "algebra"],
    "Science": ["physics", "chemistry"]
}

# 🔹 Get category
def get_category(file, mode):
    file = file.lower()

    if mode == "auto":
        for cat, exts in file_types.items():
            for ext in exts:
                if file.endswith(ext):
                    return cat
        return "Others"

    if mode == "custom":
        for cat, words in keywords.items():
            for word in words:
                if word in file:
                    return cat
    return None


# 🔹 Organize
def organize(folder, mode):
    files = os.listdir(folder)

    print("\nFiles found:")
    for f in files:
        print("-", f)

    confirm = input("Move files? (y/n): ")
    if confirm != "y":
        return

    for file in files:
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            category = get_category(file, mode)

            if not category:
                continue

            dest = os.path.join(folder, category)

            if not os.path.exists(dest):
                os.mkdir(dest)

            shutil.move(path, os.path.join(dest, file))

    print("✅ Done!")


# 🔹 Menu
def menu():
    print("\n1. Auto Sort")
    print("2. Custom Sort")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        organize(input("Folder path: "), "auto")
    elif choice == "2":
        organize(input("Folder path: "), "custom")
    elif choice == "3":
        return
    else:
        print("Invalid")

    menu()


menu()