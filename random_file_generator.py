import os
import random
import string
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Generates a random string
def random_string(length=200):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# Adds random spaces to simulate words
def wordify(input_text):
    output = input_text
    iter_factor = int(len(input_text) / 10)

    for _ in range(iter_factor):
        rand_index = random.randint(0, len(output) - 1)
        output = output[:rand_index] + ' ' + output[rand_index:]

    return output

# Create a single PDF file with random content
def create_pdf(file_length):
    output_dir = os.path.join(os.getcwd(), "generated")
    os.makedirs(output_dir, exist_ok=True)
    file_name = random_string(12) + ".pdf"
    file_path = os.path.join(output_dir, file_name)

    styles = getSampleStyleSheet()
    story = []

    for _ in range(file_length):
        text = wordify(random_string())
        story.append(Paragraph(text, styles["Normal"]))
        story.append(Spacer(1, 12))

    pdf = SimpleDocTemplate(file_path)
    pdf.build(story)

# Generate exactly 5 random PDF files
def generate_files():
    for _ in range(5):
        file_length = random.randint(10, 200)
        create_pdf(file_length)

if __name__ == "__main__":
    generate_files()
