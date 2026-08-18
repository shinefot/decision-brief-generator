import os

import anthropic
import pandas as pd
import streamlit as st

st.title("📊 Decision Brief Generator")
st.caption("Upload raw metrics → get an executive brief with recommended actions.")

# --- Load data: user's upload, or fall back to the bundled sample ---
uploaded = st.file_uploader("Upload a CSV", type="csv")

if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.success(f"Loaded {len(df)} rows from your file.")
else:
    df = pd.read_csv("sample_data.csv")
    st.info("No file uploaded — using bundled sample data.")

st.dataframe(df, use_container_width=True)

# --- Convert the dataframe to text Claude can read ---
def data_as_text(df):
    return (
        "RAW DATA (CSV):\n"
        + df.to_csv(index=False)
        + "\nSUMMARY STATISTICS:\n"
        + df.describe(include="all").to_csv()
    )

# --- The prompt: this is where the product thinking lives ---
PROMPT_TEMPLATE = """You are a senior business analyst preparing a decision brief \
for a growth leadership team.

Analyze the dataset below and write a decision brief with exactly these sections:

## Executive Summary
2-3 sentences on the overall state of the business.

## Key Findings
3-5 bullet points. Each must cite specific numbers from the data \
(trends, inflection points, correlations). Call out anything concerning.

## Recommended Actions
3 concrete, prioritized actions. For each: what to do, why the data supports it, \
and what metric would prove it worked.

## Risks & Caveats
1-2 bullets on data limitations or alternative explanations.

Be direct and specific. No filler.

{data}
"""

# --- Generate the brief on button click ---
if st.button("Generate Decision Brief", type="primary"):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        st.error("Set the ANTHROPIC_API_KEY environment variable first.")
        st.stop()

    client = anthropic.Anthropic(api_key=api_key)

    with st.spinner("Analyzing data..."):
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1500,
            messages=[
                {"role": "user", "content": PROMPT_TEMPLATE.format(data=data_as_text(df))}
            ],
        )

    brief = response.content[0].text
    st.markdown("---")
    st.markdown(brief)
    st.download_button("Download brief (.md)", brief, file_name="decision_brief.md")
    