
import webview


import google.generativeai as genai



genai.configure(api_key="AIzaSyDSKIDuDcWISdQ446J8vO-IVUI5XAES2Q0")

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello, i am a student from B. S. Abdur Rahman Crescent Institute Of Science And Technology. i have few questions"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)


class Api:
    
    
    def prompt_response(self,query):
        
        response = chat.send_message(query+" (from B. S. Abdur Rahman Crescent Institute Of Science And Technology)")
        return response.text

api=Api()
html = open("index.html","r").read()
webview.create_window(title='Chatbot', html=html,js_api=api)
webview.start()