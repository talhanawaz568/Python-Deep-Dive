import smtplib
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
smtp_port = 587
email_user = 'your_email'
email_password = 'your_passwd' 

try:
    # Set up the server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Fixed typo here
    server.login(email_user, email_password)

    # Create the email
    subject = 'Test Email Subject'
    body = 'This is a mail sent from a python script'
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email_user
    
    # Update this to a real email address you want to send to
    recipient_email = 'recipient@gmail.com' 
    msg['To'] = recipient_email

    # Send the email
    server.sendmail(email_user, recipient_email, msg.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the connection
    server.quit()
