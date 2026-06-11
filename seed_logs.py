from logger import write_log

# Simulated attacks
for i in range(6):
    write_log("login_failed", "192.168.1.10", "Invalid login attempt")

for i in range(4):
    write_log("port_scan", "10.0.0.5", "Scanning ports")