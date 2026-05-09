from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime, timedelta
import pandas as pd
import os


def get_matches_for_date(driver, date):
    url = f"https://www.yallakora.com/matches?date={date.strftime('%m/%d/%Y')}#days"
    driver.get(url)

    wait = WebDriverWait(driver, 10)
    all_data = []

    try:
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "matchesList")))
    except:
        return []

    leagues = driver.find_elements(By.CLASS_NAME, "matchesList")

    for league in leagues:
        try:
            league_name = league.find_element(By.TAG_NAME, "h2").text
        except:
            league_name = ""

        matches = league.find_elements(By.CLASS_NAME, "item")

        for match in matches:
            # 🔥 الفرق (الحل الحقيقي)
            try:
                teamA = match.find_element(By.CLASS_NAME, "teamA").text.strip()
                teamB = match.find_element(By.CLASS_NAME, "teamB").text.strip()
            except:
                # fallback لو structure مختلف
                try:
                    teams = match.find_elements(By.CSS_SELECTOR, ".teams")
                    teamA = teams[0].text
                    teamB = teams[1].text
                except:
                    teamA, teamB = "", ""

            # ⏰ الوقت
            try:
                time_match = match.find_element(By.CLASS_NAME, "time").text
            except:
                time_match = ""

            # 📌 الحالة
            try:
                status = match.find_element(By.CLASS_NAME, "matchStatus").text
            except:
                status = ""

            all_data.append({
                "date": date.strftime("%Y-%m-%d"),
                "league": league_name,
                "teamA": teamA,
                "teamB": teamB,
                "time": time_match,
                "status": status
            })

    return all_data


def scrape_range(start_date, end_date):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    current = start_date
    all_matches = []

    while current <= end_date:
        print(f"Scraping {current.strftime('%Y-%m-%d')}...")
        daily = get_matches_for_date(driver, current)

        print(f"Found {len(daily)} matches")

        all_matches.extend(daily)
        current += timedelta(days=1)

    driver.quit()
    return all_matches


# 🔥 الفترة
start = datetime(2026, 4, 21)
end = datetime(2026, 5, 21)

data = scrape_range(start, end)

print(f"\nTotal matches collected: {len(data)}")

# 🔥 حفظ
file_name = "matches_full_data.csv"

if os.path.exists(file_name):
    try:
        os.remove(file_name)
    except:
        file_name = "matches_new.csv"

df = pd.DataFrame(data)
df.to_csv(file_name, index=False, encoding="utf-8-sig")

print(f"Saved to {file_name} ✅")