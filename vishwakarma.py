import os
import time

from openai import OpenAI

class VishwakarmaV2:
    def __init__(self):
        self.master = "Sunil Rinwa"
        self.title = "Samrat"
        
        self.client = OpenAI(api_key="AIzaSyCKHpPo2BclLJ25_P01ry8j3ZbbGrFIx58")

    def generate_code(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are an expert developer. Generate clean working code."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        
        except Exception as e:
            print("[ERROR AI]:", e)
            return None

    def build_entity(self, category):
        desc = input(f"[{self.title}] What to build: ")
        
        print("Generating with AI...")
        
        prompt = f"Create a complete {category} project: {desc}. Give full working code."
        code = self.generate_code(prompt)
        
        if not code:
            print("Failed")
            return
        
        filename = f"{category}_{int(time.time())}.py"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
        
        print(f"Created: {filename}")
        
        run = input("Run now? (y/n): ")
        if run.lower() == "y":
            os.system(f"python {filename}")

    def website_builder(self):
        name = input("Website name: ")
        
        html = f"""
<!DOCTYPE html>
<html>
<head>
<title>{name}</title>
<style>
body {{ font-family: Arial; text-align:center; }}
</style>
</head>
<body>
<h1>Welcome to {name}</h1>
<p>Powered by Vishwakarma</p>
</body>
</html>
"""
        with open("index.html", "w") as f:
            f.write(html)
        
        print("Website Ready: index.html")

    def run_core(self):
        print(f"VISHWAKARMA v2 ACTIVE // MASTER: {self.master}")
        
        while True:
            print("\n1. Build App")
            print("2. Build Website")
            print("3. Exit")
            
            choice = input(f"[{self.title}] Command: ")
            
            if choice == "1":
                self.build_entity("app")
            elif choice == "2":
                self.website_builder()
            elif choice == "3":
                break


if __name__ == "__main__":
    vk = VishwakarmaV2()
    vk.run_core()
