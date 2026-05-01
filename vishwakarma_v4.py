import os
import time
import json
import google.generativeai as genai
from flask import Flask, request, jsonify

class VishwakarmaV4:
    def __init__(self):
        self.master = "Sunil Rinwa"
        self.status = "ACTIVE"

        genai.configure(api_key="AIzaSyCKHpPo2BclLJ25_P01ry8j3ZbbGrFIx58")

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
            res = self.model.generate_content(prompt)
            return res.text
        except:
            return "AI Error"

    def execute_task(self, command):
        if "time" in command:
            return time.ctime()
        elif "status" in command:
            return "System Running"
        else:
            return self.generate(command)

app = Flask(__name__)
vk = VishwakarmaV4()

@app.route('/')
def home():
    return {
        "system": "Vishwakarma V4",
        "status": vk.status,
        "master": vk.master
    }

@app.route('/execute', methods=['POST'])
def execute():
    data = request.json or {}
    command = data.get("command", "")

    result = vk.execute_task(command)

    vk.save_memory({
        "cmd": command,
        "res": result,
        "time": time.time()
    })

    return jsonify({"output": result})

@app.route('/memory')
def memory():
    with open(vk.memory_file) as f:
        return json.load(f)

@app.route('/health')
def health():
    return {"status": "OK"}

if __name__ == "__main__":
    port = 10000
    print("Vishwakarma V4 ACTIVE")
    app.run(host="0.0.0.0", port=port)
