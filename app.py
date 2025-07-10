from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from main import build_agent
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Business Metrics AI Agent",
    description="LangGraph-powered agent that analyzes business data and provides recommendations.",
    version="1.0",
)

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

agent = build_agent()


class DayData(BaseModel):
    revenue: float
    cost: float
    customers: int


class BusinessData(BaseModel):
    today: DayData
    yesterday: DayData


@app.post("/analyze")
def analyze_business(data: BusinessData):
    try:
        result = agent.invoke({"input_data": data.model_dump()})
        return result["summary"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
