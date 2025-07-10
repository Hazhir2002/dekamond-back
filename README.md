## How to run the app:
first create a virtual environment (python -m venv .env)
then activate your venv (.env/Scripts/activate)
then install the packages in requirements.txt (pip install -r requirements.txt)
to run the tests you can do (pytest -v)
if you want to see the result of only the backend you can run (python main.py)
but if you want to see the result and use the agent with dekamond-fron run (uvicorn app:app --reload)
