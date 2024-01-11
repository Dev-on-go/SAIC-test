import docker
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body):

    sender_email = "speeserpant@outlook.com"
    receiver_email = "crackitnotes@gmail.com"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.office365.com", 587)
    status_code, response = server.ehlo()  
    #print(f"echo:{status_code},{response}")
    status_code, response = server.starttls() 
    #print(f"start:{status_code},{response}")
    status_code, response = server.login(sender_email, "Birthd@y03")
    #print(f"login:{status_code},{response}")


    # Send email
    server.send_message(message)
    server.quit()

def monitor_containers():
    client = docker.from_env()
    container_states = {}

    def handle_event(event):
        container_id = event["Actor"]["ID"]
        container_state = event["status"]

        if container_state == "start":
            container_states[container_id] = "running"
        elif container_state == "die":
            container_states[container_id] = "exited"

        container_info = client.containers.get(container_id).name
        subject = "Container Alert - State Change"
        body = f"Container: {container_info}\nCurrent State: {container_state}"
        send_email(subject, body)

    for event in client.events(decode=True):
        handle_event(event)
# Run the monitoring function
monitor_containers()