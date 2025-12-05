from pydantic import BaseModel
from typing import Dict, Any

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    raw_llm: str
    parsed: Dict[str, Any] = {}

class ExtractRequest(BaseModel):
    analyze_json: Dict[str, Any]

class ExtractResponse(BaseModel):
    raw_llm: str
    features: Dict[str, Any] = {}

class BlueprintRequest(BaseModel):
    feature_json: Dict[str, Any]

class BlueprintResponse(BaseModel):
    raw_llm: str
    blueprint: Dict[str, Any] = {}

class ScoreRequest(BaseModel):
    feature_json: Dict[str, Any]

class ScoreResponse(BaseModel):
    raw_llm: str
    score_json: Dict[str, Any] = {}
