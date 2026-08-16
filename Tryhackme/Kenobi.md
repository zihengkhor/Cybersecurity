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

**Answer:** `ANSWER_HERE`

**How I found it:**
```bash
<command>
```

### 1.2 Port Scanning
```bash
# Quick scan — top 1000 ports
sudo nmap -sS <TARGET_IP>

# Full port scan — all 65535 ports
sudo nmap -p- <TARGET_IP> -oN nmap-all-ports.txt

# Detailed service scan on found ports
sudo nmap -sV -sC -O -p <PORT1,PORT2,PORT3> <TARGET_IP> -oN nmap-detailed.txt
```
**Open Ports Found:**

| Port | Service | Version |
|:---:|:---|:---|
| 22 | SSH | OpenSSH X.X |
| 80 | HTTP | Apache X.X |
| 445 | SMB | Samba X.X |

**Screenshot:**
![Nmap Output](screenshots/01-nmap.png)

### 1.3 Web Enumeration (if HTTP/HTTPS found)
```bash
# Directory brute-forcing
gobuster dir -u http://<TARGET_IP> -w /usr/share/wordlists/dirb/common.txt -o gobuster.txt

# Or with ffuff
ffuf -u http://<TARGET_IP>/FUZZ -w /usr/share/wordlists/dirb/common.txt
```
**Interesting Directories Found:**
- `/admin`
- `/login`
- `/backup`

### 1.4 SMB Enumeration (if port 445 found)
```bash
enum4linux -a <TARGET_IP>
smbclient -L //<TARGET_IP>
```

---

## 2. Initial Access / Exploitation

### Vulnerability Identified
**Name:** [e.g., Unauthenticated Remote Code Execution in X]  
**CVE:** [CVE-XXXX-XXXX] (if applicable)  
**Port:** [e.g., 80]  
**Service:** [e.g., Apache / PHP]

### Exploitation Steps
```bash
# Step 1: [What you did]
<command here>

# Step 2: [What you did]
<command here>
```

**Or via Metasploit:**
```bash
msfconsole
msf6 > use exploit/[path/to/exploit]
msf6 exploit(...) > set RHOSTS <TARGET_IP>
msf6 exploit(...) > set LHOST <YOUR_IP>
msf6 exploit(...) > set LPORT 4444
msf6 exploit(...) > exploit
```

**Proof of Access:**
```bash
whoami
# Output: [user / www-data / etc]
```

**Screenshot:**
![Shell Obtained](screenshots/02-shell.png)

---

## 3. Privilege Escalation

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

## 4. Flags

### User Flag
```bash
cat /home/<user>/user.txt
# or
cat /home/<user>/Desktop/user.txt
```
**Flag:** `THM{...}`

### Root Flag
```bash
cat /root/root.txt
# or
cat /root/Desktop/root.txt
# or
cat /root/flag.txt
```
**Flag:** `THM{...}`

---

## 5. Questions & Answers

### Question 1
**Question:** [Paste the exact question from TryHackMe]

**Answer:** `ANSWER_HERE`

**How I found it:**
```bash
# Command used to find the answer
<command>
```
**Output:**
```
<relevant output showing the answer>
```

---

### Question 2
**Question:** [Paste the exact question from TryHackMe]

**Answer:** `ANSWER_HERE`

**How I found it:**
```bash
<command>
```
**Output:**
```
<relevant output>
```

---

### Question 3
**Question:** [Paste the exact question from TryHackMe]

**Answer:** `ANSWER_HERE`

**How I found it:**
```bash
<command>
```
**Output:**
```
<relevant output>
```

---

### Question 4
**Question:** [Paste the exact question from TryHackMe]

**Answer:** `ANSWER_HERE`

**How I found it:**
```bash
<command>
```
**Output:**
```
<relevant output>
```

---

### Question 5
**Question:** [Paste the exact question from TryHackMe]

**Answer:** `ANSWER_HERE`

**How I found it:**
```bash
<command>
```
**Output:**
```
<relevant output>
```

---

## 6. Lessons Learned

| # | Lesson |
|---|--------|
| 1 | [e.g., Always check for anonymous SMB shares first] |
| 2 | [e.g., SUID binaries are a common privesc vector on Linux] |
| 3 | [e.g., Version numbers in banners are gold — always note them] |
| 4 | [e.g., Check `sudo -l` before trying kernel exploits] |

**What I would do differently next time:**
- [e.g., Take screenshots at EVERY step, not just at the end]
- [e.g., Document commands as I run them, not from memory later]

**Tools used:**
- Nmap
- Gobuster / ffuf
- enum4linux
- Metasploit
- [Any other tools]

---

*Writeup by: [Your Name] | GitHub: [github.com/yourname]*
