from fastapi import FastAPI
from app.models import CodeInput, SuggestionsOutput
from app.analyzer import analyze_code
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.post("/analyze", response_model=SuggestionsOutput)
async def analyze(input: CodeInput):
    suggestions = analyze_code(input.code)
    return SuggestionsOutput(suggestions=suggestions)
