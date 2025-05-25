from openai import OpenAI
import os
import PyPDF2

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_cv_text(pdf_path="data/CV_2025MAR.pdf"):
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

CV_CONTEXT = get_cv_text()

def ask_bot(user_input):
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OpenAI API key is not set.")

    response = client.chat.completions.create(
        model="qwen/qwen3-8b:free",
        messages=[
            {"role": "system", "content": "You are an assistant. Here is the user's CV for context:\n" + CV_CONTEXT},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content