# Python Automation & SRE Labs 🚀

This repository contains **15 Python automation exercises** that progress from basic scripting to DevOps/SRE-related tasks.  
They are organized into three levels:

---

## 🟢 Level 1: Fundamentals & Basic Automation
1. Welcome script (input & output)
2. Basic calculator (functions & conditionals)
3. Bulk file renaming
4. Detect duplicate files
5. Local backup with logs

---

## 🟡 Level 2: System Monitoring & APIs
6. Ping multiple servers
7. Simple disk space monitor
8. Consume a public REST API (JSONPlaceholder / OpenWeather)
9. Scheduled task with cron
10. Log file analyzer (regex, statistics)

---

## 🔴 Level 3: DevOps / SRE Focus
11. Service status checker (nginx, mysql, ssh)
12. Git repositories bulk cloning
13. Config file comparator
14. Secure password generator
15. Microservices connectivity checker (port 80/443)

---

## ⚙️ Tech & Tools
- **Python 3**
- `os`, `subprocess`, `shutil`, `logging`, `re`, `requests`, `json`, `psutil`
- Linux environment (Ubuntu 22.04)
- Cron for scheduling
- Git & GitHub for version control

---

## 📂 Example Outputs
Log analyzer:

Log stats:
  ERROR: 44
  INFO: 99
  WARNING: 42
  DEBUG: 15

ERROR lines:
  2025-09-20 13:00:00 ERROR OverflowError en cálculo de cuotas (request_id=9845)
  2025-09-20 13:01:09 ERROR Timeout en servicio externo
  2025-09-20 13:01:32 ERROR OverflowError en cálculo de cuotas
  2025-09-20 13:05:22 ERROR No se pudo conectar a la base de datos (request_id=8977)
  2025-09-20 13:12:16 ERROR Excepción en módulo auth: IndexError


Sertive test (microservices, simulated):

OK: nginx se encuentra activo
FAIL: mysql se encuentra inactivo. Intentando reiniciar... # No tengo instalado mysql en mi maquina virtual jaja 
Failed to restart mysql.service: Unit mysql.service not found.
 No se pudo reiniciar mysql (revisa permisos o logs)
FAIL: ssh se encuentra inactivo. Intentando reiniciar...  
Failed to restart ssh.service: Unit ssh.service not found. # tampoco lo tengo instalado
 No se pudo reiniciar ssh (revisa permisos o logs)


## About
This repository was created as part of my personal learning roadmap to DevOps/SRE.
It demonstrates progression from Python fundamentals to system monitoring, service reliability, and automation tasks.
The goal is to showcase practical exercises that build the foundation for a career in DevOps/Site Reliability Engineering (SRE).

Author: Marco Antonio Morales Suárez


