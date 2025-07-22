import os
import subprocess

def tailor_resume(tex_path, job_title, job_desc, output_pdf_path="resume/tailored_resume.pdf"):
    if not os.path.exists(tex_path):
        print("❌ LaTeX source file not found!")
        return

    with open(tex_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace placeholder with the actual job title
    content = content.replace("%%JOB_TITLE%%", job_title)

    # Save the modified tex file
    tailored_tex_path = "resume/tailored_resume.tex"
    with open(tailored_tex_path, "w", encoding="utf-8") as file:
        file.write(content)

    # Compile to PDF using pdflatex
    try:
        subprocess.run([
    r"C:\Users\Dell\AppData\Local\Programs\MiKTeX\miktex\bin\x64\pdflatex.exe",
    "-output-directory=resume",
    tailored_tex_path
], check=True)

        os.rename("resume/tailored_resume.pdf", output_pdf_path)
        print(f"✅ Tailored LaTeX resume compiled: {output_pdf_path}")
    except subprocess.CalledProcessError:
        print("❌ LaTeX compilation failed.")
