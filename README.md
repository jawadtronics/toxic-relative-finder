# ☠️ Toxic Relative Finder @ Jawadtronics

A fun and dramatic Python app that uses humor and randomness to identify the "most toxic" relative from a list you provide. Built for laughs, personal amusement, and a bit of emotional venting. 😉

---

## 💡 Features

- 🎛️ Interactive command-line interface
- 🎲 Random selection of a "toxic" relative
- 📤 Sends user input to a webhook (e.g., Make.com)
- 📨 Stylish HTML email report with dark theme
- 💼 Includes a LinkedIn contact button instead of traditional CTA
- 🖤 Fully themed: Black background + Red highlights

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Libraries:** `requests`, `random`, `json`, `time`, `os`
- **Output Format:** JSON payload → Webhook + HTML Email
- **UI:** Terminal-based with Unicode & emoji formatting
- **Email:** Dark-themed responsive HTML with inline styles (for Gmail, Outlook, etc.)

---

## 📦 JSON Payload Sent to Webhook

```json
{
  "name": "Jawad",
  "email": "jawad@example.com",
  "toxic_relative": "Uncle Bob",
  "relatives": ["Uncle Bob", "Aunt Zara", "Cousin Ali"]
}
