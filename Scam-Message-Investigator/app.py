
import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="Scam Message Investigator",
    page_icon="🔍",
    layout="centered"
)

# Application title
st.title("🔍 Scam Message Investigator")

st.write(
    "Analyze suspicious messages using AI "
    "and identify possible scam indicators."
)

st.divider()

# Message input
st.subheader("📩 Enter Your Message")

message = st.text_area(
    "Paste the suspicious SMS, email, or WhatsApp message below:",
    height=200,
    placeholder="Example: Congratulations! You have won a free prize. Click this link to claim..."
)

# Function to analyze the message
def investigate_message(text):

    url = "http://localhost:11434/api/chat"

    prompt = f"""
    You are a Scam Message Investigator.

    Analyze the following message carefully.

    Message:
    {text}

    Provide an investigation report with these sections:

    1. Risk Level: Low, Medium, or High.
    2. Message Type: Identify the possible type of message.
    3. Warning Signs: List suspicious words, links,
       requests, or other warning signs.
    4. Explanation: Explain why the message may be
       suspicious or legitimate.
    5. Recommended Actions: Explain what the receiver
       should do to stay safe.

    Important:
    - Do not assume every message is a scam.
    - Do not claim a link is malicious without verification.
    - If information is insufficient, mention that.
    - Give a clear and simple report.
    """

    payload = {
        "model": "gemma3:1b",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    response = requests.post(
        url,
        json=payload,
        timeout=180
    )

    response.raise_for_status()

    result = response.json()

    return result["message"]["content"]


# Analyze button
if st.button("🔎 Investigate Message", use_container_width=True):

    if not message.strip():

        st.warning("Please enter a message first.")

    else:

        with st.spinner("AI is investigating your message..."):

            try:

                report = investigate_message(message)

                st.success("Investigation completed!")

                st.subheader("📊 Investigation Report")

                st.markdown(report)

                st.download_button(
                    label="⬇️ Download Investigation Report",
                    data=report,
                    file_name="scam_investigation_report.txt",
                    mime="text/plain"
                )

            except requests.exceptions.ConnectionError:

                st.error(
                    "Cannot connect to Ollama. "
                    "Please make sure Ollama is running."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "The AI model took too long to respond. "
                    "Please try again."
                )

            except Exception as e:

                st.error(f"An error occurred: {e}")

st.divider()

st.caption(
    "AI-generated results are preliminary assessments, "
    "not proof that a message is safe or fraudulent."
)
