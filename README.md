# decision-brief-generator
AI-powered decision brief generator — upload a metrics CSV, get an executive summary, key findings, and prioritized actions via the Claude API. Built with Python + Streamlit.
# Decision Brief Generator

Turns raw business metrics (CSV) into an executive decision brief — summary,
key findings with cited numbers, prioritized actions, and risks — using the Claude API.

## Run it

pip install streamlit pandas anthropic
$env:ANTHROPIC_API_KEY = "your-key"     (PowerShell)
python -m streamlit run app.py

## How it works
1. Upload any CSV (or use the bundled sample: 12 weeks of Dubai food-delivery metrics)
2. Data is serialized to text (raw CSV + summary statistics)
3. One structured-prompt Claude API call
4. Brief renders in the browser, downloadable as Markdown
