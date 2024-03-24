import streamlit as st
import uuid

def generate_webhook_url():
    # Generate a unique identifier using UUID
    webhook_id = str(uuid.uuid4())
    # Construct the webhook URL
    webhook_url = f"https://your-domain.com/webhook/{webhook_id}"
    return webhook_url

def main():
    st.title("Webhook Receiver App")

    # Generate a unique webhook URL
    webhook_url = generate_webhook_url()

    # Display the webhook URL
    st.write("Use the following URL as your webhook endpoint:")
    st.write(webhook_url)

    # Display a message indicating that the app is ready to receive data
    st.write("This app is ready to receive data from the webhook.")

    # Define a placeholder to display incoming data
    incoming_data = st.empty()

    # Listen for incoming webhook data
    if "webhook_data" not in st.session_state:
        st.session_state.webhook_data = []

    if st.session_state.webhook_data:
        incoming_data.write("Incoming Data:")
        incoming_data.write(st.session_state.webhook_data)

if __name__ == "__main__":
    main()
