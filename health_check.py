#!/usr/bin/env python3
import shutil
import psutil
import socket
import time
import emails

# Report an error if CPU usage is over 80%
def check_cpu():
    usage = psutil.cpu_percent(0.1)
    return usage > 80

# Report an error if available disk space is lower than 20%
def check_disk():
    du = shutil.disk_usage('/')
    pct = du.free / du.total * 100
    return pct < 20

# Report an error if available memory is less than 500MB
def check_memory():
    mem = psutil.virtual_memory()
    mem_available = mem.available / (1024 * 1024)
    return mem_available < 500

# Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
def check_hostname():
    return socket.gethostbyname('localhost') != '127.0.0.1'

def generate_subjectline(case):
    

    print cases[case]

if __name__ == "__main__":
    cases = {
        "cpu" : "Error - CPU usage is over 80%",
        "disk" : "Error - Available disk space is less than 20%",
        "memory" : "Error - Available memory is less than 500MB",
        "hostname" : "Error - localhost cannot be resolved to 127.0.0.1"
    }

    sender = "automation@example.com"
    recipient = "student-03-5a1f1d893fce@example.com"
    body = "Please check your system and resolve the issue as soon as possible."

    while True:
        subjects = []
        if check_cpu():
            subjects.append(cases['cpu'])

        if check_disk():
            subjects.append(cases['disk'])

        if check_memory():
            subjects.append(cases['memory'])

        if check_hostname():
            subjects.append(cases['hostname'])

        for sub in subjects:
            msg = emails.generate(sender, recipient, sub, body)
            emails.send(msg)

        time.sleep(60)