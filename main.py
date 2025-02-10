import requests
import json
import markdown
import pdfkit

def generate_cheat_sheet(model,subject):
    url = "http://localhost:11434/api/generate"
    model = model

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "model": model,
        "prompt": subject,
        "stream": False
    }

    try:
        response = requests.post(url, headers=headers, json=data)  
        response.raise_for_status()  # Raise an error for bad responses 4xx, 5xx

        response_data = response.json()  
        actual_response = response_data.get("response", "No response found")  

        print(actual_response)

        with open(subject+".md", "w", encoding="utf-8") as text_file:
            text_file.write(actual_response)
        
        html_content = markdown.markdown(actual_response)
        pdfkit.from_string(html_content, subject+".pdf")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    model = input("Model : ")
    subject = input("Enter the subject : ")
    generate_cheat_sheet(model,subject)
