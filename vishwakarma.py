import os
import time
import json
import hashlib
import google.generativeai as genai

class VishwakarmaV4:
    def __init__(self):
        self.master = "Sunil Rinwa"
        self.title = "Samrat"
        self.auth_key = hashlib.sha256("121".encode()).hexdigest()
        
        # 🔑 Your Key Placeholder
        api_key = "AIzaSyCKHpPo2BclLJ25_P01ry8j3ZbbGrFIx58"
        
        if api_key != "YOUR_GEMINI_KEY_HERE":
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel('gemini-1.5-pro')
        
        self.memory_file = "vk_memory.json"
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                json.dump([], f)

    def verify(self):
        key = input("[AUTH]: ")
        return hashlib.sha256(key.encode()).hexdigest() == self.auth_key

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
            print("AI Error:", e)
            return None

    def create_project_structure(self, name):
        os.makedirs(name, exist_ok=True)
        os.makedirs(f"{name}/templates", exist_ok=True)
        os.makedirs(f"{name}/static", exist_ok=True)

    def build_web_app(self):
        if not self.verify():
            print("❌ Unauthorized")
            return
        
        name = input("Project name: ")
        idea = input("What web app: ")
        
        self.create_project_structure(name)
        print("⚡ Building Flask App...")
        
        code = self.generate(f"Create Flask app for: {idea} with routes and HTML templates")
        
        if not code:
            return
        
        with open(f"{name}/app.py", "w", encoding="utf-8") as f:
            f.write(code)
            
        html = f"""
<!DOCTYPE html>
<html>
<head><title>{name}</title></head>
<body>
<h1>{idea}</h1>
<p>Powered by Vishwakarma</p>
</body>
</html>
"""
        with open(f"{name}/templates/index.html", "w", encoding="utf-8") as f:
            f.write(html)
            
        self.save_memory({"project": name, "idea": idea})
        print(f"✅ Web App Ready in folder: {name}")
        print(f"▶ Run: cd {name} && python app.py")

    def auto_debug(self, filepath):
        with open(filepath, "r") as f:
            code = f.read()
        fixed = self.generate(f"Fix this Python Flask code:\n{code}")
        if fixed:
            with open(filepath, "w") as f:
                f.write(fixed)
            print("✅ Fixed")

    def run(self):
        print(f"🔥 VISHWAKARMA v4 ACTIVE // {self.master}")
        while True:
            print("\n1. Build Web App")
            print("2. Memory")
            print("3. Exit")
            
            cmd = input("Command: ")
            if cmd == "1":
                self.build_web_app()
            elif cmd == "2":
                if os.path.exists(self.memory_file):
                    print(open(self.memory_file).read())
            elif cmd == "3":
                break

if __name__ == "__main__":
    app = VishwakarmaV4()
    app.run()
