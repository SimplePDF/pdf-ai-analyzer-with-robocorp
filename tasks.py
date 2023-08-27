from robocorp.tasks import task
from robocorp import workitems
from robocorp import http
from pypdf import PdfReader
from robocorp import vault
from robocorp import storage
import requests
import json


@task
def extract_feedback_from_pdf():
    for item in workitems.inputs:
        http.download(
            item.payload.get("data").get("submission").get("url"), "temp_document.pdf")
        reader = PdfReader("temp_document.pdf")

        page = reader.pages[0]
        text = page.extract_text()

        # Tweak the logic below for your document
        lines = text.split('\n')
        feedback = '\n'.join(lines[1:])

        workitems.outputs.create(payload={"feedback": feedback})


@task
def analyze_feedback():
    for item in workitems.inputs:
        feedback = item.payload.get("feedback")
        result = analyze_feedback_with_open_ai(feedback)
        workitems.outputs.create(
            payload={"feedback": feedback, "result": result})


def analyze_feedback_with_open_ai(feedback):
    secrets_container = vault.get_secret('open_ai_api')
    prompt = storage.get_asset("feedback_prompt")
    open_api_key = secrets_container['api_key']

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {open_api_key}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{prompt} {feedback}"}]
    }

    response = requests.post(url, headers=headers, json=data)

    json_response = response.json()

    return json.loads(json_response['choices'][0]['message']['content'])
