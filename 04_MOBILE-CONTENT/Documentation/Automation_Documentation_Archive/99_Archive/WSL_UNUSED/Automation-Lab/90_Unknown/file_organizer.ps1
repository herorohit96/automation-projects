$SOURCE = "C:\Users\admin\Downloads\Automation-Lab-Advantage"
$DEST = "C:\Users\admin\Downloads\Automation-Lab-Advantage\Automation-Lab"
$BACKUP = Join-Path $DEST "99_Backup"
$LOGS = Join-Path $DEST "logs"

# Create directories if they don't exist
if (!(Test-Path $BACKUP)) { New-Item -ItemType Directory -Path $BACKUP -Force }
if (!(Test-Path $LOGS)) { New-Item -ItemType Directory -Path $LOGS -Force }

$logFile = Join-Path $LOGS "file_sort_log.txt"

$rules = @{
    ".pdf" = "10_Assets/PDFs"
    ".jpg" = "10_Assets/Images"
    ".png" = "10_Assets/Images"
    ".mp4" = "10_Assets/Videos"
    ".docx" = "10_Assets/Docs"
    ".py" = "20_Code/Python"
}

Get-ChildItem $SOURCE -File | ForEach-Object {
    $file = $_.Name
    $ext = $_.Extension.ToLower()
    $targetFolder = if ($rules.ContainsKey($ext)) { $rules[$ext] } else { "90_Unknown" }
    $destPath = Join-Path $DEST $targetFolder

    if (!(Test-Path $destPath)) { New-Item -ItemType Directory -Path $destPath -Force }

    # Backup first
    Copy-Item $_.FullName -Destination $BACKUP

    # Then move
    Move-Item $_.FullName -Destination $destPath

    # Log the action
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$timestamp | $file -> $targetFolder" | Out-File -FilePath $logFile -Append
}