# README — Upload `C:\automation-lab` to Google Drive (rclone)

Ye guide step-by-step batata hai kaise aap local `C:\automation-lab` folder ko Google Drive pe upload karoge using `rclone`.

Important notes:
- `rclone config` opens a browser to authenticate your Google account. Complete that step.
- If you put rclone in `C:\Windows\System32`, you can run `rclone` from any terminal.
- The script `upload_to_gdrive.ps1` will help download rclone and run the config step.

Steps (quick):

1) Open PowerShell as Administrator

```powershell
# Run the helper script (one-line):
PowerShell -ExecutionPolicy Bypass -File "C:\automation-lab\scripts\upload_to_gdrive.ps1"
```

2) When the script finishes the interactive config, note the remote name you created (e.g., `gdrive`).

3) Run the upload command (either in PowerShell or the script prompt):

```powershell
# If rclone is in PATH
rclone copy "C:\automation-lab" gdrive:"Automation Business" --progress

# If rclone is NOT in PATH (use full path to executable)
"C:\Users\<you>\Downloads\rclone\rclone-*-windows-amd64\rclone.exe" copy "C:\automation-lab" gdrive:"Automation Business" --progress
```

4) Verify upload in Google Drive: drive.google.com -> check `Automation Business` folder.

Troubleshooting

- Permission denied when copying `rclone.exe` to `C:\Windows\System32`: run PowerShell as Administrator or skip copying and use the full path to `rclone.exe` (the script prints the path).
- `rclone config` browser auth fails: make sure browser allows popups and you authorize the correct Google account.
- Large uploads paused: re-run the same `rclone copy` command — rclone will skip already-uploaded files and resume.

Security

- Do not commit your Google OAuth tokens or `rclone` config to public repos.
- Keep `rclone` config in your user profile (default). If you need to move it, protect it properly.

Want me to run the copy now? If yes, say "run upload" and give the rclone remote name (e.g. `gdrive`).
