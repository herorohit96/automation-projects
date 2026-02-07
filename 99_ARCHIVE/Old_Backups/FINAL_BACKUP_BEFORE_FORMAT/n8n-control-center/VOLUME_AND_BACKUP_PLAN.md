# Volume and Backup Plan

This explains how to save your n8n data safely.

## What Data Must Persist
- Workflows: The automation flows you build.
- Credentials: Passwords and API keys for services.
- Settings: Your n8n configuration.
- Logs: Records of what n8n did.

Without saving this data, you lose your work when the container stops.

## How Volumes Will Be Created

### Docker Volumes
- Docker can create special storage called "volumes".
- Volumes survive even if the container is deleted.
- Command: `docker volume create n8n_data`

### Local Folders
- Map a folder on your computer to the container.
- Use the -v flag in docker run.
- Example: `-v C:\n8n-data:/home/node/.n8n`

## How Backups Will Be Taken

### Manual Backup
1. Stop n8n: `docker stop n8n`
2. Copy volume data: `docker run --rm -v n8n_data:/data -v C:\backup:/backup alpine tar czf /backup/n8n-backup.tar.gz -C /data .`
3. Start n8n again: `docker start n8n`

### Folder Backup
1. If using local folder, just copy the folder.
2. Use Windows File Explorer to copy `C:\n8n-data` to a safe place.

### Regular Backup Plan
- Backup every week.
- Keep 3 recent backups.
- Store backups on a different drive or cloud.

## Safety Rules
- Always backup before making big changes.
- Test restore from backup.
- Keep backups in multiple places.