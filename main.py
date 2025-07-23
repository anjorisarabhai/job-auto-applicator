import time
import random
import yaml
import csv
import os
from datetime import datetime

# === Import custom modules ===
from utils.scraper import get_job_links  # Dummy list for now
from utils.cover_letter_generator import generate_cover_letter
from utils.resume_editor import tailor_resume
from utils.linkedin_apply import apply_on_linkedin  # Optional

# === Load config ===
with open("config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# === Application logger ===
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

# === Get job list (dummy for now) ===
jobs = get_job_links(config["keywords"], config["locations"])
jobs_to_apply = jobs[:config["daily_limit"]]

# === Main loop ===
for job in jobs_to_apply:
    title = job["title"]
    company = job["company"]
    desc = job.get("description", "")
    location = job.get("location", "Unknown")

    print(f"\n📌 Applying to: {title} at {company} ({location})")

    # Generate cover letter
    generate_cover_letter(title, company)

    # Tailor LaTeX resume
    tailor_resume(config["resume_path"], title, desc)

    # OPTIONAL: LinkedIn Easy Apply (manually test with real job link)
    job_url = "https://www.linkedin.com/jobs/collections/recommended/?currentJobId=4270732419"  # Replace with real Easy Apply job
    apply_on_linkedin(job_url)

    # Log the application
    log_application(
        job,
        resume_path="resume/tailored_resume.pdf",
        cover_letter_path="logs/generated_cover_letter.txt"
    )

    wait = random.uniform(30, 60)
    print(f"🕒 Waiting {int(wait)} seconds before next...")
    time.sleep(wait)

print("\n🎉 All applications for today are done.")
