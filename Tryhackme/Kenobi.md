# [Room Name] — TryHackMe Writeup
**Difficulty:** Easy  
**Platform:** TryHackMe  
**Room URL:** https://tryhackme.com/room/[room-name]  
**Date Completed:** 16/08/2026  
**Time Taken:** 1.5 hours  
**OS:** Linux

---

## Table of Contents
1. [Task 1](#1-Task-1)
2. [Task 2](#2-Task-2)
3. [Task 3](#3-Task-3)
4. [Task 4](#4-Task-4)


---

## 1. Task 1

### Question 1.1
**Question:** Scan the machine with nmap, how many ports are open?

**Answer:** `7`

**How I found it:**
```bash
nmap -sV -SS -T5 10.48.176.164
```

**Open Ports Found:**

| Port | Service | Version |
|:---:|:---|:---|
| 21 | FTP | ProFTPD 1.3.5 |
| 22 | SSH | OpenSSH 8.2 |
| 80 | HTTP | Apache 2.4.41 |
| 111 | rpcbind | rpc #100000 |
| 139 | SMB | Samba 4 |
| 445 | SMB | Samba 4 |
| 2049 | nfs | rpc #100003 |

**Screenshot:**  

<img width="767" height="289" alt="image" src="https://github.com/user-attachments/assets/ba5a1632-d36e-45df-9657-dbb69f79bd28" />

---

## 2. Task 2

### Question 2.1
**Question:** Using the nmap command above, how many shares have been found?

**Answer:** `3`

**How I found it:**
```bash
nmap -sV -SS -T5 10.48.176.164
```

---

## 3. Task 3

### Enumeration
```bash
# Check current user
whoami
id

# Check sudo permissions
sudo -l

# Check SUID binaries
find / -perm -4000 2>/dev/null

# Check cron jobs
cat /etc/crontab
ls -la /etc/cron.d/

# Check kernel version
uname -a
```

### Privilege Escalation Vector
**Method:** [e.g., SUID binary exploitation / Kernel exploit / Sudo misconfiguration / PATH hijacking]

**Steps:**
```bash
# Step 1
<command>

# Step 2
<command>
```

**Proof of Root / Admin:**
```bash
whoami
# Output: root
```

**Screenshot:**
![Root Shell](screenshots/03-root.png)

---

## 4. Task 4
