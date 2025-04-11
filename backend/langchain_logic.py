async def analyze_thought(text: str) -> dict:
    print("📥 Inside analyze_thought with:", text)
    return {"advice": f"You said: {text}"}
