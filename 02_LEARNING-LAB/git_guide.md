# Git Guide - The Time Machine 🕰️

Git aapka "Save Point" system hai. Iska use karke aap code ko kabhi bhi loose nahi karoge.

## 1. Status Check Karo (Kya badla hai?)
```bash
git status
```
Ye batayega ki kaunsi file change hui hai.

## 2. Sab Kuch Add Karo (Ready to Save)
```bash
git add .
```
Iska matlab: "Saare changes ko box mein daal do."

## 3. Save Karo (Commit)
```bash
git commit -m "Jo kaam kiya uska naam"
```
Example: `git commit -m "Created financial tracker"`
Iska matlab: "Box ko seal kar do aur label laga do."

## 4. History Dekho (Purane versions)
```bash
git log
```
Ye aapko dikhayega ki kab-kab kya save kiya tha.

---
**Tip:** Jab bhi koi bada kaam khatam ho, ye 3 commands chalao:
1. `git status`
2. `git add .`
3. `git commit -m "message"`
