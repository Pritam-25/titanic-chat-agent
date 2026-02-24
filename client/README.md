(Optional) Streamlit client for the Titanic Chat Agent

Requirements

- Python 3.10+ (or as configured in your environment)
- Install dependencies from `pyproject.toml` or manually:

```bash
python -m pip install -r requirements.txt
# or with pip
pip install streamlit requests pillow
```

Run

```bash
streamlit run app.py
```

By default the client posts to `http://localhost:8000/api/v1/chat/`. Change the URL in the sidebar if your backend is hosted elsewhere.

Enter a question, click "Ask", and the answer (and any generated image) will display.
