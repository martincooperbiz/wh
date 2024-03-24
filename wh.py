import streamlit as st
import pandas as pd

# Define a placeholder to store incoming webhook data
if "webhook_data" not in st.session_state:
    st.session_state.webhook_data = []

# Use a fixed webhook ID
WEBHOOK_ID = "422654c5-34ea-4790-9d72-d36fcb665d0f"

def generate_webhook_url():
    # Construct the webhook URL
    webhook_url = f"https://49win8x85gkbzcpq5ze9dr.streamlit.app/webhook/{WEBHOOK_ID}"

    return webhook_url

def main():
    st.title("Webhook Receiver App")

    # Generate the webhook URL
    webhook_url = generate_webhook_url()

    # Display the webhook URL
    st.write("Use the following URL as your webhook endpoint:")
    st.write(webhook_url)

    # Display a message indicating that the app is ready to receive data
    st.write("This app is ready to receive data from the webhook.")

    # Listen for incoming webhook data
    if st.session_state.webhook_data:
        # Display incoming data as a table
        st.write("Incoming Data:")
        df = pd.DataFrame(st.session_state.webhook_data)
        st.write(df)

if __name__ == "__main__":
    main()
