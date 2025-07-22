import csv
from datetime import datetime
import os
from utils.resume_editor import tailor_resume
from utils.cover_letter_generator import generate_cover_letter
from utils.scraper import get_job_links
import time, random, yaml

def log_application(job, resume_path, cover_letter_path, status="Applied"):
    log_path = "logs/applied_jobs.csv"
    file_exists = os.path.isfile(log_path)

    with open(log_path, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Job Title", "Company", "Location", "Resume File", "Cover Letter File", "Status"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            job["title"],
            job["company"],
            job.get("location", "Unknown"),
            resume_path,
            cover_letter_path,
            status
        ])

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

    log_application(
    job,
    resume_path="resume/tailored_resume.pdf",
    cover_letter_path="logs/generated_cover_letter.txt"
    )

    wait = random.uniform(15, 45)
    print(f"🕒 Waiting {int(wait)} seconds...")
    time.sleep(wait)
