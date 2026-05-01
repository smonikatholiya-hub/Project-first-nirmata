import google.generativeai as genai
import os

# Configuration
API_KEY = "AIzaSyCKHpPo2BclLJ25_P01ry8j3ZbbGrFIx58"
TARGET_URL = "curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: AIzaSyCKHpPo2BclLJ25_P01ry8j3ZbbGrFIx58' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
"

genai.configure(api_key=AIzaSyCKHpPo2BclLJ25_P01ry8j3ZbbGrFIx58)

def execute_vishwakarma():
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # System Initialization
        auth_check = model.generate_content("SYSTEM_CHECK_V1")
        
        if auth_check:
            print(f"STATUS: ONLINE")
            print(f"GATEWAY: {TARGET_curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent" \
  -H 'Content-Type: application/json' \
  -H 'X-goog-api-key: AIzaSyCKHpPo2BclLJ25_P01ry8j3ZbbGrFIx58' \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "Explain how AI works in a few words"
          }
        ]
      }
    ]
  }'
}")
            print(f"RESPONSE: {auth_check.text}")
            
    except Exception as error:
        print(f"STATUS: OFFLINE")
        print(f"ERROR_LOG: {error}")

if __name__ == "__main__":
    execute_vishwakarma()
