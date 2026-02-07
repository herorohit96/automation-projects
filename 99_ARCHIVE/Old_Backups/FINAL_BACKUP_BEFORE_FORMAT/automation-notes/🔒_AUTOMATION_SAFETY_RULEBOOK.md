# ⚠️ READ THIS BEFORE TOUCHING DOCKER, WSL, OR N8N ⚠️

## A. ❌ NEVER TOUCH THESE (Critical Warnings)
- **Workflow Files**: Mat delete karo n8n workflows (.json files) - ye tumhari automation ka dil hai!
- **Docker Volumes**: `docker volume rm` kabhi mat run karo - saal data gayab ho jayega
- **n8n Database**: SQLite files ya database folders ko touch mat karo
- **Credentials**: API keys, passwords, tokens - ye kabhi expose mat karo
- **WSL Distros**: `wsl --unregister` ya `wsl --shutdown` avoid karo jab tak zaruri na ho
- **Docker Reset**: Factory reset button kabhi mat press karo bina backup ke

## B. ✅ SAFE TO USE & DAILY RULES
- **Start/Stop Containers**: `docker start/stop <container>` - daily use ke liye safe
- **Check Status**: `docker ps`, `docker logs <container>` - bas check karne ke liye
- **n8n UI Access**: http://localhost:5678 - workflows edit karne ke liye
- **Backup First**: Har change se pehle `docker exec n8n n8n export:workflow --all` run karo
- **Monitor Logs**: `docker logs -f n8n` - issues check karne ke liye
- **Update Images**: `docker pull n8n/n8n` - safe, data preserve karta hai

## C. 🧯 EMERGENCY RECOVERY STEPS (Docker + n8n)
1. **Docker Stuck?** Quit Docker Desktop → wait 10 sec → reopen
2. **n8n Not Loading?** `docker restart n8n` try karo
3. **Container Crashed?** `docker logs n8n` check karo, phir `docker start n8n`
4. **Port Conflict?** `netstat -ano | findstr :5678` check karo
5. **If All Fails**: `docker stop n8n` → `docker rm n8n` → recreate with preserved volumes
6. **Last Resort**: Windows restart, phir Docker reopen

## D. 📦 BACKUP SYSTEM (Exact Commands & Locations)
- **Workflow Backup**: `docker exec n8n n8n export:workflow --all > backup.json`
- **Volume Backup**: `docker run --rm -v n8n_data:/data -v $(pwd):/backup alpine tar czf /backup/n8n_backup.tar.gz -C /data .`
- **Location**: Automation-Stack/99_Archive/ ya external drive
- **Auto Backup**: Daily `docker exec n8n n8n export:credentials --all > creds_backup.json`
- **Full System**: `docker-compose down` → copy entire Automation-Stack folder
- **Restore**: `docker run --rm -v n8n_data:/data -v $(pwd):/backup alpine sh -c "cd /data && tar xzf /backup/n8n_backup.tar.gz"`

## E. 🧠 DAILY REMINDER (Why this file matters)
- **Data Loss Prevention**: Ek galti se saal ka kaam gayab ho sakta hai
- **Time Saver**: Emergency mein confuse mat ho, yahan se steps follow karo
- **Beginner Friendly**: Complex cheezein simple banayi hain
- **Automation Continuity**: Tumhari income-generating automations ko safe rakho
- **Learn from Mistakes**: Pehle galtiyon se seekho, yeh file usse prevent karti hai
- **Peace of Mind**: Confident feel karo har change mein!</content>
<parameter name="filePath">c:\Users\admin\Downloads\Automation-Lab-Advantage\Automation-Stack\00_Docs\🔒_AUTOMATION_SAFETY_RULEBOOK.md