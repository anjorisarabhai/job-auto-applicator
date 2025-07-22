from utils.resume_editor import tailor_resume
from utils.cover_letter_generator import generate_cover_letter
from utils.scraper import get_job_links
import time, random, yaml

# Load config
with open("config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

jobs = get_job_links(config["keywords"], config["locations"])
jobs_to_apply = jobs[:config["daily_limit"]]

for job in jobs_to_apply:
    title = job["title"]
    company = job["company"]
    desc = job["description"]

    print(f"\n📌 Applying to: {title} at {company}")

    # Generate tailored cover letter
    generate_cover_letter(title, company)

    # Generate tailored resume (basic copy for now)
    tailor_resume(config["resume_path"], title, desc)

    wait = random.uniform(15, 45)
    print(f"🕒 Waiting {int(wait)} seconds...")
    time.sleep(wait)
