import json
import random
import requests
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("╔══════════════════════════════════════════════════╗")
print("║         🔍 Toxic Relative Finder @ Jawadtronics         ║")
print("╚══════════════════════════════════════════════════╝\n")

name = input("🧑 Enter your name: ")
email = input("📧 Enter your email: ")
rishtadar = []

print("\n👨‍👩‍👧‍👦 Let's list your relatives")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
number = input("🔢 How many relatives do you have? ")

for i in range(int(number)):
    relative = input(f"➡️  Enter name of relative #{i+1}: ")
    rishtadar.append(relative)

print("\n🎲 Picking the most toxic relative...\n")
time.sleep(2)

toxic_relative = random.choice(rishtadar)

data = {
    "name": name,
    "email": email,
    "toxic_relative": toxic_relative,
    "relatives": rishtadar
}

print("📡 Sending data to your email...")
response = requests.post("https://hook.eu2.make.com/k1plj8ysxp6sndddxlgfceeg4hupo50s", json=data)

if response.status_code == 200:
    print("✅ Data sent successfully!")
else:
    print(f"⚠️  Failed to send data. Status Code: {response.status_code}")

print("\n📬 Check your email for the results!\n")
print("╔══════════════════════════════════════════════════╗")
print("║        ✅ Toxic Relative Report Sent!             ║")
print("╚══════════════════════════════════════════════════╝")
