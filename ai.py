import openai

openai.api_key = "YOUR_OPENAI_KEY"

def extract_topics(text):
    prompt = f"Extract 3-5 topics as a list: {text}"
    resp = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=50)
    return resp.choices[0].text.strip()

def summarize(text):
    prompt = f"Summarize in 5 bullet points: {text}"
    resp = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=150)
    return resp.choices[0].text.strip()

def generate_insights(summary, topics):
    prompt = f"Based on topics {topics} and summary {summary}, give 3 actionable insights."
    resp = openai.Completion.create(model="text-davinci-003", prompt=prompt, max_tokens=150)
    return resp.choices[0].text.strip()
