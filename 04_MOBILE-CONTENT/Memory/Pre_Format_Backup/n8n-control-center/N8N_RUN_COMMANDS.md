# N8N Run Commands

This file stores only the final, tested Docker commands to run n8n.

## Important Rules
- Do not run untested commands.
- Test commands first and log in ACTION_LOG.md.
- Only put working commands here.

## Placeholder Commands (Not Tested Yet)

### Basic N8N Run
```
docker run -d --name n8n -p 5678:5678 n8nio/n8n
```

### With Volume for Data
```
docker run -d --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n
```

### With Local Folder
```
docker run -d --name n8n -p 5678:5678 -v C:\Users\admin\Downloads\Automation-Lab-Advantage\n8n-data:/home/node/.n8n n8nio/n8n
```

## When Commands Are Ready
- Replace placeholders with real commands.
- Test them and confirm they work.
- Update this file with the final versions.