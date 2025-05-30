# 🔓 Unlocking Agentic AI: A Developer’s Guide to Tool Calling

Tool calling transforms AI from a passive responder into an active agent capable of executing real-world tasks—such as invoking APIs, querying databases, and running code.

This guide provides a practical walkthrough for developers aiming to integrate tool calling into their AI applications.

---

## 🧠 What Is Tool Calling?

Tool calling (also known as function calling) enables AI models to select and execute external functions based on user intent. These tools can range from fetching weather data to processing payments or managing internal databases.

> Think of it as the AI saying: “I understand what you need—and I know exactly which tool to use to do it.”

---

## ⚙️ How Tool Calling Works

1. **User Query** → AI understands the intent.
2. **Intent Match** → AI selects a matching tool.
3. **Tool Parameters** → AI generates inputs in JSON format.
4. **Tool Execution** → Backend or agent runs the function.
5. **Response Interpretation** → AI interprets and responds to the user.

---

## 💱 Example: Currency Converter Tool

### Step 1: Define the Tool Function (Python)

```python
def convert_currency(from_currency: str, to_currency: str, amount: float) -> dict:
    import requests
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"].get(to_currency)

    if rate:
        converted = round(amount * rate, 2)
        return {"converted_amount": converted, "currency": to_currency}
    else:
        return {"error": "Invalid target currency"}

