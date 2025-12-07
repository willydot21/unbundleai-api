
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from app.prompts import p_analyze as p_analyze, p_blueprint as p_blueprint, p_extract as p_extract, p_score as p_score
from app.schemas import *
from app.llm_client import call_llm
from app.utils import try_parse_json

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest):
  p = p_analyze(req.text)
  try:
    raw = call_llm(p)
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
  parsed = try_parse_json(raw) or {}    
  return AnalyzeResponse(raw_llm=raw, parsed=parsed)

@app.post("/extract", response_model=ExtractResponse)
def extract(req: ExtractRequest):
    import json
    p = p_extract(json.dumps(req.analyze_json))
    try:
        raw = call_llm(p, max_tokens=800)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    parsed = try_parse_json(raw) or {}
    return ExtractResponse(raw_llm=raw, features=parsed)

@app.post("/blueprint", response_model=BlueprintResponse)
def blueprint(req: BlueprintRequest):
    import json
    p = p_blueprint(json.dumps(req.feature_json))
    try:
        raw = call_llm(p, max_tokens=800)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    parsed = try_parse_json(raw) or {}
    return BlueprintResponse(raw_llm=raw, blueprint=parsed)

@app.post("/score", response_model=ScoreResponse)
def score(req: ScoreRequest):
    import json
    p = p_score(json.dumps(req.feature_json))
    try:
        raw = call_llm(p, max_tokens=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    parsed = try_parse_json(raw) or {}
    return ScoreResponse(raw_llm=raw, score_json=parsed)
