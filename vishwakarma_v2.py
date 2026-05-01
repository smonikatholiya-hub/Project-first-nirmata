import os
import time
from google.generativeai import GenerativeModel, configure

class VishwakarmaV3:
    def __init__(self):
        self.master = "Sunil Rinwa"
        self.title = "Samrat"

        configure(api_key="AIzaSyCKHpPo2BclLJ25_P01ry8j3ZbbGrFIx58")

        self.model = GenerativeModel("gemini-1.5-flash")

    def generate_code(self, prompt):
        """🤖 AI Code Generator"""
        try:
            response = self.model.generate_content(
                "Give only real working code. If error then say ERROR.\n" + prompt
            )
            return response.text
        
        except Exception as e:
            print("[ERROR AI]:", e)
            return None

    def build_project(self, category):
        """🚀 App / Website / Survey Generator"""

        desc = input(f"[{self.title}] What to build: ")

        print("⚡ Generating with AI...")

        prompt = f"Create a complete {category}: {desc}. Give full working code."

        code = self.generate_code(prompt)

        if not code or "ERROR" in code:
            print("❌ Failed or Invalid Output")
            return

        filename = f"{category}_{int(time.time())}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)

        print(f"✅ Created: {filename}")

    def run_core(self):
        print(f"🔥 VISHWAKARMA v3 ACTIVE // MASTER: {self.master}")

        while True:
            print("\n1. Build App")
            print("2. Build Website")
            print("3. Build Survey")
            print("4. Exit")

            choice = input(f"[{self.title}] Command: ")

            if choice == "1":
                self.build_project("mobile app")
            elif choice == "2":
                self.build_project("website")
            elif choice == "3":
                self.build_project("survey form")
            elif choice == "4":
                break


if __name__ == "__main__":
    vk = VishwakarmaV3()
    vk.run_core()
