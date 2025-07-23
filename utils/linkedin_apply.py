from selenium import webdriver
from selenium.webdriver.common.by import By
import time, random

def apply_on_linkedin(job_url):
    # Set Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")

    # Launch browser
    driver = webdriver.Chrome(options=options)
    driver.get(job_url)

    # Let you log in manually
    input("🔐 Log in to LinkedIn, then press Enter here to continue...")

    try:
        # Click the "Easy Apply" button
        apply_btn = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        apply_btn.click()
        time.sleep(random.uniform(2, 4))

        # Try to find and click the "Submit application" button
        submit_btn = driver.find_element(By.XPATH, "//button[@aria-label='Submit application']")
        submit_btn.click()
        print("✅ Application submitted successfully!")

    except Exception as e:
        print("⚠️ Could not complete application:", e)

    finally:
        time.sleep(5)
        driver.quit()
