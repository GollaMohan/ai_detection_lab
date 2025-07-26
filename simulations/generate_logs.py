import pandas as pd
import random
import time

processes = ["lsass.exe", "powershell.exe", "notepad.exe", "explorer.exe", "malware_sim.exe"]
logs = []

for i in range(50):
    logs.append({
        "timestamp": time.time(),
        "process": random.choice(processes),
        "action": random.choice(["read", "write", "execute"]),
        "user": random.choice(["Admin", "User1"]),
    })

df = pd.DataFrame(logs)
df.to_csv("logs.csv", index=False)
print("Fake logs generated.")
