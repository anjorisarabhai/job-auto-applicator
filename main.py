import time, random, yaml
from utils.scraper import get_job_links
from utils.cover_letter_generator import generate_cover_letter

# Load config
with open("config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# Get dummy job links (real scraping will come later)
jobs = get_job_links(config["keywords"], config["locations"])

# Limit to daily limit
jobs_to_apply = jobs[:config["daily_limit"]]

# Loop and generate cover letters
for job in jobs_to_apply:
    title = job["title"]
    company = job["company"]
    print(f"\nApplying to: {title} at {company}")

    generate_cover_letter(title, company)

    # Simulate time delay between applications
    wait = random.uniform(15, 45)
    print(f"🕒 Waiting for {int(wait)} seconds before next...")
    time.sleep(wait)
