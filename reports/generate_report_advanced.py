import openai
import pandas as pd

openai.api_key = "YOUR_API_KEY"

alerts = pd.read_csv("alerts.csv")

prompt = f"""
You are a cybersecurity analyst. Given these suspicious alerts, generate a detailed detection report:

{alerts.to_dict(orient='records')}
"""

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=500,
    temperature=0.5,
)

report_text = response['choices'][0]['message']['content']

with open("report_advanced.md", "w") as f:
    f.write(report_text)

print("✅ Advanced report generated as report_advanced.md")
