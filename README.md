# Decision Brief Generator

AI-powered decision brief generator — upload a metrics CSV, get an executive
summary, key findings with cited numbers, prioritized actions, and risks via
the Claude API. Built with Python + Streamlit.

## Run it

````
pip install streamlit pandas anthropic
$env:ANTHROPIC_API_KEY = "your-key"     # PowerShell
python -m streamlit run app.py
````

## How it works

1. Upload any CSV (or use the bundled sample: 12 weeks of Dubai food-delivery metrics)
2. Data is serialized to text (raw CSV + summary statistics)
3. One structured-prompt Claude API call
4. Brief renders in the browser, downloadable as Markdown
````
````

**One thing to watch when pasting:** the block above ends with a stray ``` on the last line before the final fence — delete that trailing line if it comes along (the file should end after "downloadable as Markdown"). The important part is that the three commands sit between a pair of triple-backtick lines, which is what turns them into a proper code block.

Then click **Commit changes**, refresh, and the Run it section should render as a neat grey command box instead of a run-on sentence.

After that, you're genuinely finished: repo link, screenshots, and the 100-word summary — the whole optional challenge, done with a working tool most applicants won't have. Submit it.
