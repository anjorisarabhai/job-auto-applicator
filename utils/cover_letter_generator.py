import os

def generate_cover_letter(role, company, output_path="logs/generated_cover_letter.txt"):
    # Read the cover letter template
    with open("cover_letter_template.txt", "r", encoding="utf-8") as template_file:
        template = template_file.read()

    # Replace placeholders
    customized_letter = (
        template.replace("{{ROLE}}", role)
                .replace("{{COMPANY}}", company)
    )

    # Save the customized letter
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as out_file:
        out_file.write(customized_letter)

    print(f"✅ Cover letter generated for {role} at {company}")
