import pandas as pd

df = pd.read_csv('../simulations/logs.csv')

# Flag processes containing 'malware' or 'powershell' as suspicious
df["detection"] = df["process"].apply(lambda x: "Suspicious" if "malware" in x or "powershell" in x else "Clean")

alerts = df[df["detection"] == "Suspicious"]
alerts.to_csv("alerts.csv", index=False)

print(f"✅ Detection complete. {len(alerts)} suspicious activities saved to alerts.csv.")
