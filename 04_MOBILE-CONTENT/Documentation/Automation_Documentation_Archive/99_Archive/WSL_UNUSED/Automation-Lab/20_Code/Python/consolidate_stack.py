import os, shutil

# Automation Stack Consolidation Script
# Safely organizes all automation files into unified structure

BASE_DIR = "Automation-Stack"

# Create the full directory structure
dirs_to_create = [
    "00_Docs",
    "01_Scripts/python",
    "01_Scripts/powershell",
    "02_n8n/workflows",
    "02_n8n/backups",
    "03_Docker/volumes",
    "03_Docker/compose",
    "04_Logs",
    "99_Archive"
]

for dir_path in dirs_to_create:
    full_path = os.path.join(BASE_DIR, dir_path)
    os.makedirs(full_path, exist_ok=True)
    print(f"✅ Created: {full_path}")

# Safe move function
def safe_move(src, dest_dir):
    if not os.path.exists(src):
        print(f"⚠️  Source not found: {src}")
        return

    filename = os.path.basename(src)
    dest_path = os.path.join(dest_dir, filename)

    # Handle duplicates
    counter = 1
    original_dest = dest_path
    while os.path.exists(dest_path):
        name, ext = os.path.splitext(filename)
        dest_path = os.path.join(dest_dir, f"{name}_{counter}{ext}")
        counter += 1

    shutil.move(src, dest_path)
    print(f"📁 Moved: {src} -> {dest_path}")
    return dest_path

print("\n🚀 Starting consolidation...")

# Move Python scripts
safe_move("Automation-Lab/20_Code/Python/file_organizer.py", os.path.join(BASE_DIR, "01_Scripts/python"))
safe_move("Automation-Lab/20_Code/Python/safe_cleanup.py", os.path.join(BASE_DIR, "01_Scripts/python"))
safe_move("n8n_discovery.py", os.path.join(BASE_DIR, "01_Scripts/python"))

# Move PowerShell scripts
safe_move("file_organizer.ps1", os.path.join(BASE_DIR, "01_Scripts/powershell"))

# Move n8n notes to docs
n8n_notes_dir = os.path.join(BASE_DIR, "02_n8n/notes")
if os.path.exists(n8n_notes_dir):
    for file in os.listdir(n8n_notes_dir):
        src = os.path.join(n8n_notes_dir, file)
        safe_move(src, os.path.join(BASE_DIR, "00_Docs"))
    os.rmdir(n8n_notes_dir)  # Remove empty notes dir

# Move logs from Safe_Cleanup
safe_cleanup_logs = "C:/Safe_Cleanup/logs"
if os.path.exists(safe_cleanup_logs):
    for file in os.listdir(safe_cleanup_logs):
        src = os.path.join(safe_cleanup_logs, file)
        safe_move(src, os.path.join(BASE_DIR, "04_Logs"))

# Move other Safe_Cleanup items to archive
safe_cleanup_base = "C:/Safe_Cleanup"
if os.path.exists(safe_cleanup_base):
    for item in os.listdir(safe_cleanup_base):
        if item != "logs":  # Already moved logs
            src = os.path.join(safe_cleanup_base, item)
            if os.path.isdir(src):
                # Move directory contents
                for file in os.listdir(src):
                    file_src = os.path.join(src, file)
                    safe_move(file_src, os.path.join(BASE_DIR, "99_Archive"))
            else:
                safe_move(src, os.path.join(BASE_DIR, "99_Archive"))

# Move Automation-Lab docs to 00_Docs
automation_docs = "Automation-Lab"
if os.path.exists(automation_docs):
    for root, dirs, files in os.walk(automation_docs):
        for file in files:
            if file.endswith(('.md', '.txt', '.pdf')):
                src = os.path.join(root, file)
                safe_move(src, os.path.join(BASE_DIR, "00_Docs"))

print(f"\n✅ Consolidation complete!")
print(f"📁 All files organized in: {BASE_DIR}")
print("🛡️  SAFETY: Files moved safely with duplicate handling")