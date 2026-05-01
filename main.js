const { GoogleGenerativeAI } = require("@google/generative-ai");
const API_KEY = "AIzaSyD2UUV_a7IIp9Wx8VG-cXAj2euTrFhMffA";
const genAI = new GoogleGenerativeAI(API_KEY);
async function run() {
    try {
        const model = genAI.getGenerativeModel({ model: "gemini-pro" });
        const result = await model.generateContent("System check: Is Vishwakarma Project Online?");
        console.log("\n--- SUCCESS ---");
        console.log("AI Response:", result.response.text());
        console.log("---------------\n");
    } catch (e) {
        console.log("\n--- ERROR ---");
        console.log("Detail:", e.message);
        console.log("---------------\n");
    }
}
run();
