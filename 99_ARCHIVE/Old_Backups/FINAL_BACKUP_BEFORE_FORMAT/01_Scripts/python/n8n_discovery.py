import os, shutil, datetime

# N8N File Discovery & Consolidation Script
# SAFE: Copies only, no deletions, no modifications
# Scans user folders for n8n-related files and organizes them

# Target directory structure
BASE_DIR = "Automation-Stack"
N8N_DIR = os.path.join(BASE_DIR, "02_n8n")
WORKFLOWS_DIR = os.path.join(N8N_DIR, "workflows")
BACKUPS_DIR = os.path.join(N8N_DIR, "backups")
NOTES_DIR = os.path.join(N8N_DIR, "notes")

# Create directories
for dir_path in [WORKFLOWS_DIR, BACKUPS_DIR, NOTES_DIR]:
    os.makedirs(dir_path, exist_ok=True)

# Report file
REPORT_FILE = os.path.join(N8N_DIR, "discovery_report.txt")

# Locations to scan (user-accessible only)
home = os.path.expanduser("~")
scan_locations = [
    os.path.join(home, "Documents"),
    os.path.join(home, "Downloads"),
    os.path.join(home, "Desktop"),
    "Automation-Lab",  # Assuming in current directory
]

# WSL Ubuntu home (if accessible)
wsl_home = r"\\wsl$\Ubuntu\home"
if os.path.exists(wsl_home):
    # Find the user directory
    try:
        for item in os.listdir(wsl_home):
            if os.path.isdir(os.path.join(wsl_home, item)):
                scan_locations.append(os.path.join(wsl_home, item))
                break
    except:
        pass  # Skip if not accessible

# Keywords for n8n-related files
n8n_keywords = ['n8n', 'workflow', 'automation', 'node', 'docker-compose']

def is_n8n_related(filepath):
    filename = os.path.basename(filepath).lower()
    # Check extension
    if filename.endswith('.json'):
        return True
    # Check keywords in filename
    for keyword in n8n_keywords:
        if keyword in filename:
            return True
    return False

def categorize_file(filepath):
    filename = os.path.basename(filepath).lower()
    if filename.endswith('.json') and any(k in filename for k in ['n8n', 'workflow']):
        return WORKFLOWS_DIR
    elif any(k in filename for k in ['backup', 'old', 'copy', 'duplicate']):
        return BACKUPS_DIR
    elif any(filename.endswith(ext) for ext in ['.txt', '.md', '.readme']):
        return NOTES_DIR
    else:
        return BACKUPS_DIR  # Default

# Safe copy function (avoid overwrites)
def safe_copy(src, dest_dir):
    filename = os.path.basename(src)
    dest_path = os.path.join(dest_dir, filename)
    counter = 1
    while os.path.exists(dest_path):
        name, ext = os.path.splitext(filename)
        dest_path = os.path.join(dest_dir, f"{name}_{counter}{ext}")
        counter += 1
    shutil.copy2(src, dest_path)
    return dest_path

# Discovery and consolidation
discovered_files = []
duplicates = []

print("🔍 Starting n8n file discovery and consolidation...")
print(f"📁 Target: {N8N_DIR}")
print(f"📂 Scanning locations: {scan_locations}")

with open(REPORT_FILE, "w", encoding="utf-8") as report:
    report.write("N8N File Discovery Report\n")
    report.write("=" * 50 + "\n")
    report.write(f"Generated: {datetime.datetime.now()}\n\n")
    report.write("Original Path | Copied To | Type | Duplicate\n")
    report.write("-" * 80 + "\n")

    for location in scan_locations:
        if not os.path.exists(location):
            print(f"⚠️  Skipping {location} (not found)")
            continue

        print(f"📂 Scanning {location}...")
        for root, dirs, files in os.walk(location):
            for file in files:
                filepath = os.path.join(root, file)
                if is_n8n_related(filepath):
                    category_dir = categorize_file(filepath)
                    copied_path = safe_copy(filepath, category_dir)

                    # Check for duplicates (same filename)
                    is_duplicate = "YES" if copied_path != os.path.join(category_dir, file) else "NO"

                    file_type = "JSON" if file.endswith('.json') else "OTHER"

                    report.write(f"{filepath} | {copied_path} | {file_type} | {is_duplicate}\n")

                    discovered_files.append({
                        'original': filepath,
                        'copied': copied_path,
                        'type': file_type,
                        'duplicate': is_duplicate
                    })

                    print(f"✅ Copied: {file} -> {os.path.basename(category_dir)}")

    report.write(f"\nTotal files discovered: {len(discovered_files)}\n")

print(f"\n📊 Discovery complete!")
print(f"📄 Report saved: {REPORT_FILE}")
print(f"📁 Organized in: {N8N_DIR}")
print(f"   - Workflows: {len([f for f in discovered_files if 'workflows' in f['copied']])}")
print(f"   - Backups: {len([f for f in discovered_files if 'backups' in f['copied']])}")
print(f"   - Notes: {len([f for f in discovered_files if 'notes' in f['copied']])}")

print("\n🛡️  SAFETY CONFIRMED: All files COPIED, originals preserved!")