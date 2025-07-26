import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

from state import AgentState


load_dotenv()


def email_node(state: AgentState) -> AgentState:
    print("Getting your email ready to send ...")

    results = state.results or []

    if not results:
        raise ValueError("No search results found to send via email.")

    formatted_links = "\n".join(
        f"{i+1}. {item['title']}\n{item['link']}" for i, item in enumerate(results)
    )

    email_body = f"""
    Hi,
    
    Here are the latest results from your search on: "{state.query}"
    
    {formatted_links}
    
    Best regards,
    NewsPilot Bot
    """

    sender_email = os.environ["GMAIL_SENDER_EMAIL"]
    receiver_email = os.environ["GMAIL_RECEIVER_EMAIL"]
    app_password = os.environ["GOOGLE_APP_PASSWORD"]

    msg = MIMEMultipart()

    msg["Subject"] = "NewsPilot Search Results"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    msg.attach(MIMEText(email_body, "plain"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)

            server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as exception:

        raise exception

    print("Email sent successfully!")

    return state
