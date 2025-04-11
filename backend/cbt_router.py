from fastapi import APIRouter, Request
from backend.langchain_logic import analyze_thought
import traceback

print("🚀 CBT router loaded.")

router = APIRouter()

@router.post("/analyze")
async def analyze(request: Request):
    print("📩 Endpoint hit")
    try:
        body = await request.json()
        print("📦 Raw body:", body)

        text = body.get("text", "")
        print("🔍 Extracted text:", text)

        result = await analyze_thought(text)
        print("✅ Result returned:", result)

        return result
    except Exception as e:
        print("🔥 ERROR in /analyze route:")
        traceback.print_exc()
        return {"advice": "something broke"}
