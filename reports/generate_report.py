import pandas as pd

alerts = pd.read_csv("../detection/alerts.csv")

summary = f"""
AI Detection Engineering Lab - Report

Total suspicious activities detected: {len(alerts)}

Suspicious Processes:
{alerts['process'].value_counts()}
"""

with open("report.txt", "w") as f:
    f.write(summary)

print("✅ Report generated as report.txt.")
