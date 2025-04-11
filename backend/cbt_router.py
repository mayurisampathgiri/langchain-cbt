from fastapi import APIRouter
from backend.langchain_logic import analyze_thought
from backend.models import ThoughtInput, CBTResponse
import traceback

router = APIRouter()
print("🚀 CBT router loaded.")

@router.post("/cbt/analyze", response_model=CBTResponse)
async def analyze(input: ThoughtInput):
    print("📥 Incoming text:", input.text)
    try:
        result = await analyze_thought(input.text)
        return CBTResponse(advice=result)
    except Exception as e:
        print("🔥 Error analyzing:", e)
        traceback.print_exc()
        return CBTResponse(advice="Oops, something went wrong.")
