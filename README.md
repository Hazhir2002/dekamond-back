# 🧠 Business Metrics AI Agent

An intelligent backend agent built using **LangGraph** and **FastAPI** to analyze daily business performance data (sales, costs, customers), calculate key metrics (like profit and CAC), and generate actionable recommendations.

---

## 🚀 Features

- 📊 Calculates key metrics: **Profit**, **Revenue Change**, **Cost Change**, **Customer Acquisition Cost (CAC)**
- ⚠️ Generates alerts for negative profit or abnormal CAC changes
- 🧠 Provides strategic **recommendations** (e.g., reduce costs, increase ad budget)
- 🔗 API-ready with **FastAPI**
- 🌐 Optional frontend integration with **Dekamond Frontend**
- 🧪 Includes unit tests for validating business logic

---

## 📁 Project Structure

```
.
├── app.py                   # FastAPI app
├── main.py                  # LangGraph agent setup
├── requirements.txt         # Dependencies
├── test_agent.py            # Unit tests
├── nodes/
│   ├── input_node.py
│   ├── processing_node.py
│   └── recommendation_node.py
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Create and Activate a Virtual Environment

```bash
python -m venv .env

# Activate (Windows)
.env\Scripts\activate

# Activate (Mac/Linux)
source .env/bin/activate
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧪 Running the App

### ✅ Run Backend (CLI Only)

To run the agent and view output in the terminal:

```bash
python main.py
```

---

### 🌐 Run Backend API (With Frontend Support)

To run the backend server using FastAPI:

```bash
uvicorn app:app --reload
```

- Access API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- Endpoint to call: `POST /analyze`

You can now integrate it with your frontend (e.g., Dekamond React app running at `http://localhost:3000`).

---

## 🔬 Running Tests

Use `pytest` to validate the agent’s output and logic:

```bash
pytest -v
```

---

## 🧠 API Usage

### 🔗 POST `/analyze`

Send daily business data for analysis.

#### ✅ Example Request:

```json
{
  "today": {
    "revenue": 1200,
    "cost": 800,
    "customers": 40
  },
  "yesterday": {
    "revenue": 1000,
    "cost": 600,
    "customers": 50
  }
}
```

#### 📤 Example Response:

```json
{
  "profit": 400,
  "alerts": ["Alert: CAC increased by more than 20%"],
  "recommendations": [
    "Review marketing campaigns to reduce CAC.",
    "Consider increasing advertising budget to boost growth."
  ]
}
```

---

## 🛠 Technologies Used

- [LangGraph](https://github.com/langchain-ai/langgraph)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pytest](https://docs.pytest.org/)

---

## 📌 Notes

- Ensure CORS is enabled in `app.py` if you're connecting to a frontend on a different port (e.g., React on `localhost:3000`).
- Data must include both `today` and `yesterday` fields with valid `revenue`, `cost`, and `customers` values.


