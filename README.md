# ⚽ Yallacora Scraper

Python web scraping project that collects football matches data from Yallakora using Selenium.

## 🚀 Features

- Scrape football matches data from Yallakora
- Collect:
  - League name
  - Team names
  - Match time
  - Match status
  - Match date
- Export data to CSV file
- Supports scraping a custom date range

---

## 🛠 Technologies Used

- Python
- Selenium
- Pandas
- WebDriver Manager

---

## 📂 Project Structure

```bash
yallacora-scraper/
│
├── scrapping_yallacora.py
├── matches_full_data.csv
└── README.md
```

---

## ▶️ How to Run

### 1️⃣ Install requirements

```bash
pip install selenium pandas webdriver-manager
```

### 2️⃣ Run the script

```bash
python scrapping_yallacora.py
```

---

## 📊 Output Example

| date | league | teamA | teamB | time | status |
|------|---------|--------|--------|------|---------|
| 2026-05-01 | Premier League | Arsenal | Chelsea | 21:00 | Finished |

---

## 🔥 How It Works

The script:

1. Opens Yallakora matches page
2. Extracts leagues and matches
3. Collects teams, time, and match status
4. Saves all collected data into a CSV file

---

## 👨‍💻 Author

Developed by Tharwat Farag

#Digilians