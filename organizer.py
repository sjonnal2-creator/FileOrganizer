import os
import shutil

LOG_FILE = "undo_log.txt"

# 🔹 File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg"],
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


# 🔹 Organize + LOG moves
def organize(folder, mode):
    if not os.path.exists(folder):
        print("❌ Folder does not exist")
        return

    files = os.listdir(folder)

    print("\nFiles found:")
    for f in files:
        print("-", f)

    confirm = input("Move files? (y/n): ")
    if confirm.lower() != "y":
        return

    log_entries = []

    for file in files:
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            category = get_category(file, mode)

            if not category:
                continue

            dest_folder = os.path.join(folder, category)

            if not os.path.exists(dest_folder):
                os.mkdir(dest_folder)

            new_path = os.path.join(dest_folder, file)

            shutil.move(path, new_path)

            # 🔹 Save move
            log_entries.append(f"{new_path}|{path}")

    # 🔹 Write log
    with open(LOG_FILE, "w") as f:
        for entry in log_entries:
            f.write(entry + "\n")

    print("✅ Done! (Undo available)")


# 🔹 Undo function
def undo():
    if not os.path.exists(LOG_FILE):
        print("❌ No undo data found")
        return

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()

    for line in lines:
        new_path, original_path = line.strip().split("|")

        if os.path.exists(new_path):
            shutil.move(new_path, original_path)

    os.remove(LOG_FILE)
    print("↩️ Undo completed!")


# 🔹 Menu
def menu():
    while True:
        print("\n1. Auto Sort")
        print("2. Custom Sort")
        print("3. Undo Last Operation")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            organize(input("Folder path: "), "auto")
        elif choice == "2":
            organize(input("Folder path: "), "custom")
        elif choice == "3":
            undo()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice")


menu()
