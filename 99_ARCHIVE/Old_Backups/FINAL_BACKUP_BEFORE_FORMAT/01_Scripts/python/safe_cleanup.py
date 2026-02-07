import os, shutil, datetime

# SAFE C: Drive Cleanup Script for Windows
# RULES: Only move files, never delete. Work only in user folders.
# SAFETY: DRY_RUN disabled for actual cleanup. Backup enabled.
# CONFIRMATION: User must confirm before execution.
# WEEKLY_MODE: Enable for weekly cleanup with reporting.

DRY_RUN = False  # Set to True for dry-run only
WEEKLY_MODE = False  # Set to True for weekly cleanup with report generation

# Ask for confirmation
print("⚠️  WARNING: This will move files from your user folders to C:/Safe_Cleanup/")
print("   - Files will be backed up first")
print("   - No files will be deleted")
print("   - Review Unknown_Review folder manually after")
if WEEKLY_MODE:
    print("   - WEEKLY MODE: Will generate cleanup report")
confirm = input("Type 'YES' to proceed: ")
if confirm.upper() != 'YES':
    print("Operation cancelled.")
    exit()

print("\n🚀 Starting cleanup...")
if WEEKLY_MODE:
    print("📊 Weekly mode enabled - report will be generated")

# Define folders to scan (user-specific locations only)
home = os.path.expanduser("~")
folders_to_scan = [
    os.path.join(home, "Downloads"),
    os.path.join(home, "Desktop"),
    os.path.join(home, "Documents"),
    os.path.join(home, "Videos"),
]

# Destination base folder
DEST_BASE = "C:/Safe_Cleanup"

# Create subfolders for organization
subfolders = [
    "Old_Installers",    # .exe, .msi older than 30 days
    "Large_Videos",      # Videos > 500MB
    "Duplicate_Files",   # Files with same name and size
    "Archives",          # .zip, .rar, .7z
    "Temp_Files",        # .tmp, .log
    "Unknown_Review",    # Anything unclear
    "Important_Documents", # .pdf, .docx, .xlsx
    "Backup",            # Safety copies before moving
]

for sub in subfolders:
    os.makedirs(os.path.join(DEST_BASE, sub), exist_ok=True)

# Log file
log_file = os.path.join(DEST_BASE, "cleanup_log.txt")

# Function to generate safe names (avoid overwrites)
def safe_name(path):
    base, ext = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = f"{base}_{counter}{ext}"
        counter += 1
    return path

# Get disk space summary before
try:
    total, used, free_before = shutil.disk_usage("C:/")
    print(f"Disk space BEFORE: Total {total//(1024**3)}GB, Used {used//(1024**3)}GB, Free {free_before//(1024**3)}GB")

    # Low Disk Space Alert
    if total > 0:
        free_percent = (free_before / total) * 100
        if free_percent < 10:
            alert_msg = f"{datetime.datetime.now()} | ALERT: Low disk space! Free space: {free_percent:.1f}% ({free_before//(1024**3)}GB)\n"
            alert_file = os.path.join(LOGS, "disk_alert.txt")
            with open(alert_file, "a", encoding="utf-8") as alert:
                alert.write(alert_msg)
            print(f"⚠️  DISK ALERT: Free space below 10%! ({free_percent:.1f}%)")
            log.write(alert_msg)

except Exception as e:
    print(f"Could not get disk usage: {e}")
    free_before = 0

# Track seen files for duplicate detection (name + size)
seen_files = {}  # key: (filename, size), value: True

# Progress tracking
total_files = 0
moved_files = 0
protected_folders_count = 0
sensitive_count = 0
recent_count = 0
error_count = 0

# Process files
with open(log_file, "a", encoding="utf-8") as log:
    for folder in folders_to_scan:
        if not os.path.exists(folder):
            print(f"Skipping {folder} (does not exist)")
            continue

        print(f"Scanning {folder}...")
        for root, dirs, files in os.walk(folder):
            # Skip protected folders
            protected_folders = ['Work', 'Clients', 'Courses']
            if any(protected in root for protected in protected_folders):
                protected_folders_count += len(files)  # Count files in protected folders
                print(f"Skipping protected folder: {root} ({len(files)} files)")
                continue

            for file in files:
                filepath = os.path.join(root, file)

                try:
                    # Get file info
                    stat = os.stat(filepath)
                    size = stat.st_size
                    mtime = datetime.datetime.fromtimestamp(stat.st_mtime)
                    age_days = (datetime.datetime.now() - mtime).days
                    ext = os.path.splitext(file)[1].lower()

                    # PROTECTION LAYER
                    # Skip files modified in last 7 days
                    if age_days <= 7:
                        recent_count += 1
                        print(f"PROTECTED (recent): {file} ({age_days} days old)")
                        continue

                    # Skip sensitive files by name
                    sensitive_keywords = ['aadhaar', 'pan', 'id', 'invoice', 'client']
                    if any(keyword in file.lower() for keyword in sensitive_keywords):
                        sensitive_count += 1
                        print(f"PROTECTED (sensitive): {file}")
                        continue

                    # Determine category
                    category = "Unknown_Review"

                    if ext in ['.exe', '.msi'] and age_days > 30:
                        category = "Old_Installers"
                    elif ext in ['.mp4', '.avi', '.mkv', '.mov'] and size > 500 * 1024 * 1024:  # 500MB
                        category = "Large_Videos"
                    elif ext in ['.zip', '.rar', '.7z']:
                        category = "Archives"
                    elif ext in ['.tmp', '.log']:
                        category = "Temp_Files"
                    elif ext in ['.pdf', '.docx', '.xlsx']:
                        category = "Important_Documents"

                    # Check for duplicates (same name and size)
                    key = (file, size)
                    if key in seen_files:
                        category = "Duplicate_Files"
                    else:
                        seen_files[key] = True

                    # Destination path
                    dest_path = os.path.join(DEST_BASE, category, file)
                    safe_dest = safe_name(dest_path)

                    # Backup path
                    backup_path = os.path.join(DEST_BASE, "Backup", file)
                    safe_backup = safe_name(backup_path)

                    # Perform actions
                    if not DRY_RUN:
                        # Create backup first
                        shutil.copy2(filepath, safe_backup)
                        # Then move
                        shutil.move(filepath, safe_dest)
                        moved_files += 1
                        action = "MOVED"
                    else:
                        action = "DRY-RUN MOVE"

                    total_files += 1

                    # Progress print every 100 files
                    if total_files % 100 == 0:
                        print(f"Progress: {total_files} files processed...")

                    # Log and print
                    log_entry = f"{datetime.datetime.now()} | {action} | {file} ({size//1024}KB) from {filepath} to {safe_dest}"
                    log.write(log_entry + "\n")
                    print(f"{action}: {file} -> {category}")

                except Exception as e:
                    error_count += 1
                    error_msg = f"{datetime.datetime.now()} | ERROR processing {filepath}: {str(e)}"
                    log.write(error_msg + "\n")
                    print(f"ERROR: {filepath} - {e}")

# Get disk space summary after
try:
    total, used, free_after = shutil.disk_usage("C:/")
    print(f"Disk space AFTER: Total {total//(1024**3)}GB, Used {used//(1024**3)}GB, Free {free_after//(1024**3)}GB")
    freed_gb = (free_after - free_before) / (1024**3)
    print(f"Freed disk space: {freed_gb:.2f} GB")
except Exception as e:
    print(f"Could not get disk usage: {e}")

print(f"\n✅ Cleanup complete! {moved_files} files moved out of {total_files} total files.")
print("Check C:/Safe_Cleanup/ for organized files.")
print("Review Unknown_Review folder manually before deleting anything.")

# Generate weekly report if in weekly mode
if WEEKLY_MODE:
    reports_dir = os.path.join(DEST_BASE, "Cleanup_Reports")
    os.makedirs(reports_dir, exist_ok=True)
    report_filename = f"weekly_cleanup_report_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    report_path = os.path.join(reports_dir, report_filename)

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("Weekly Cleanup Report\n")
        report.write("=" * 50 + "\n")
        report.write(f"Date & Time: {datetime.datetime.now()}\n\n")
        report.write(f"Total files scanned: {total_files}\n")
        report.write(f"Total files moved: {moved_files}\n\n")
        report.write("Total files protected:\n")
        report.write(f"  - Protected folders: {protected_folders_count}\n")
        report.write(f"  - Sensitive files: {sensitive_count}\n")
        report.write(f"  - Recent files: {recent_count}\n\n")
        freed_mb = (free_after - free_before) / (1024**2) if free_after and free_before else 0
        report.write(f"Total disk space freed: {freed_mb:.2f} MB\n\n")
        report.write(f"Errors encountered: {error_count}\n")
        if error_count == 0:
            report.write("Status: No errors - Clean run\n")
        else:
            report.write("Status: Some errors occurred - Check logs\n")

    print(f"📊 Weekly report generated: {report_path}")
    log.write(f"{datetime.datetime.now()} | WEEKLY REPORT GENERATED: {report_path}\n")

    # Update Disk Health Summary
    health_file = os.path.join(DEST_BASE, "disk_health_summary.txt")
    total_gb = total / (1024**3) if total else 0
    free_gb = free_after / (1024**3) if free_after else 0
    used_percent = ((total - free_after) / total) * 100 if total and free_after else 0

    with open(health_file, "w", encoding="utf-8") as health:
        health.write("Disk Health Summary\n")
        health.write("=" * 30 + "\n")
        health.write(f"Total disk size: {total_gb:.2f} GB\n")
        health.write(f"Free space: {free_gb:.2f} GB\n")
        health.write(f"Used space percentage: {used_percent:.1f}%\n")
        health.write(f"Last cleanup run date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        health.write(f"Last weekly report filename: {report_filename}\n")

    print(f"💾 Disk health summary updated: {health_file}")
    log.write(f"{datetime.datetime.now()} | DISK HEALTH SUMMARY UPDATED\n")

print("\nWEEKLY CLEANUP COMPLETED SAFELY" if WEEKLY_MODE else "CLEANUP COMPLETED SAFELY")