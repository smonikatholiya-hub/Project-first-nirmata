impo

rt os
import time
import json
import hashlib
import google.generativeai as genai
from flask import Flask, request, jsonify

class VishwakarmaV4:
    def __init__(self):
        self.master = "Sunil Rinwa"
        self.title = "Samrat"
        self.status = "OPERATIONAL"
        
        # ✅ Secure API Key
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("AIzaSyCKHpPo2BclLJ25_P01ry8j3ZbbGrFIx58")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-1.5-pro')

        self.memory_file = "vk_memory.json"
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                json.dump([], f)

    def save_memory(self, data):
        with open(self.memory_file, "r+") as f:
            try:
                mem = json.load(f)
            except:
                mem = []
            mem.append(data)
            f.seek(0)
            json.dump(mem, f, indent=2)

    def generate(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"System_Error: {str(e)}"

webapp = Flask(__name__)
vishwakarma = VishwakarmaV4()

@webapp.route('/')
def home():
    return {
        "status": "Vishwakarma V4 Running",
        "master": vishwakarma.master
    }

@webapp.route('/execute', methods=['POST'])
def execute():
    data = request.json
    
    command = data.get("command", "Hello")
    result = vishwakarma.generate(command)

    vishwakarma.save_memory({
        "command": command,
        "time": time.time()
    })

    return jsonify({"result": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    webapp.run(host="0.0.0.0", port=port)
