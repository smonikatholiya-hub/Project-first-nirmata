import os
import time
import json
from openai import OpenAI

class VishwakarmaV3:
    def __init__(self):
        self.master = "Sunil Rinwa"
        self.title = "Samrat"

        self.client = OpenAI(api_key="AIzaSyCKHpPo2BclLJ25_P01ry8j3ZbbGrFIx58")

        self.memory_file = "vk_memory.json"

        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                json.dump([], f)

    def save_memory(self, data):
        with open(self.memory_file, "r+") as f:
            mem = json.load(f)
            mem.append(data)
            f.seek(0)
            json.dump(mem, f, indent=2)

    def generate_code(self, prompt):
        try:
            response = self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are a senior developer. Create full multi-file projects with clean code."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            print("AI Error:", e)
            return None

    def auto_debug(self, filename):
        with open(filename, "r") as f:
            code = f.read()

        prompt = f"Fix errors in this code:\n{code}"
        fixed = self.generate_code(prompt)

        if fixed:
            with open(filename, "w") as f:
                f.write(fixed)

    def build_project(self):
        idea = input("What do you want to build: ")

        code = self.generate_code(f"Create full Python project for: {idea}")

        if not code:
            print("Failed")
            return

        filename = f"project_{int(time.time())}.py"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)

        self.save_memory({"project": idea, "file": filename})

        print(f"Created: {filename}")

        run = input("Run now? (y/n): ")
        if run == "y":
            os.system(f"python {filename}")

            fix = input("Auto fix? (y/n): ")
            if fix == "y":
                self.auto_debug(filename)

    def show_memory(self):
        with open(self.memory_file, "r") as f:
            data = json.load(f)
            for d in data:
                print(d)

    def self_evolve(self):
        idea = input("How should I improve: ")
        
        prompt = f"Improve this system based on: {idea}"
        improvement = self.generate_code(prompt)

        with open("evolution.txt", "a") as f:
            f.write(improvement + "\n\n")

    def run(self):
        print("Vishwakarma V3 Active")

        while True:
            print("\n1. Build Project")
            print("2. Show Memory")
            print("3. Self Improve")
            print("4. Exit")

            choice = input("Command: ")

            if choice == "1":
                self.build_project()
            elif choice == "2":
                self.show_memory()
            elif choice == "3":
                self.self_evolve()
            elif choice == "4":
                break


if __name__ == "__main__":
    app = VishwakarmaV3()
    app.run()
