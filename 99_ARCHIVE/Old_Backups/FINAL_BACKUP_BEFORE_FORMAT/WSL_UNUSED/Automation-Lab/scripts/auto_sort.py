import os, shutil, datetime

SOURCE = r"C:\Users\admin\Downloads\Automation-Lab-Advantage"
DEST = r"C:\Users\admin\Downloads\Automation-Lab-Advantage\Automation-Lab"
BACKUP = os.path.join(DEST, "99_Backup")
LOGS = os.path.join(DEST, "logs")

os.makedirs(BACKUP, exist_ok=True)
os.makedirs(LOGS, exist_ok=True)

log_file = os.path.join(LOGS, "file_sort_log.txt")
error_log = os.path.join(LOGS, "error_log.txt")

def safe_name(path):
    base, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = f"{base}_{counter}{ext}"
        counter += 1
    return path

rules = {
    ".pdf": "10_Assets/PDFs",
    ".jpg": "10_Assets/Images",
    ".png": "10_Assets/Images",
    ".mp4": "10_Assets/Videos",
    ".docx": "10_Assets/Docs",
    ".py": "20_Code/Python",
}

try:
    with open(log_file, "a") as log:
        for file in os.listdir(SOURCE):
            src_path = os.path.join(SOURCE, file)
            if not os.path.isfile(src_path):
                continue

            ext = os.path.splitext(file)[1].lower()
            target_folder = rules.get(ext, "90_Unknown")
            dest_path = os.path.join(DEST, target_folder)

            os.makedirs(dest_path, exist_ok=True)

            # backup
            backup_dest = os.path.join(BACKUP, file)
            safe_backup = safe_name(backup_dest)
            shutil.copy2(src_path, safe_backup)

            # move
            dest_file = os.path.join(dest_path, file)
            safe_dest = safe_name(dest_file)
            shutil.move(src_path, safe_dest)

            log.write(f"{datetime.datetime.now()} | {file} -> {target_folder}\n")
except Exception as e:
    with open(error_log, "a") as err_log:
        err_log.write(f"{datetime.datetime.now()} | ERROR: {str(e)}\n")