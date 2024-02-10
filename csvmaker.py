import csv
import random

def generate_phishing_emails(num_emails, file_path):
    email_texts = [
        "Your account has been compromised. Click here to secure it: https://example.com/secure-account",
        "URGENT: Verify your account now to avoid account suspension. Click here: https://example.com/verify",
        "Action required: Your account has been flagged for suspicious activity. Verify now: https://example.com/verify-account",
        "Your account password has been reset. Click here to confirm: https://example.com/reset-password",
        "Important: Your account access has been restricted. Confirm your identity: https://example.com/confirm-identity",
        "Alert: Unauthorized login detected on your account. Secure it now: https://example.com/secure-account",
        "URGENT: Your account has been hacked. Take action now: https://example.com/secure-account",
        "Security Notice: Your account has been locked due to suspicious activity. Unlock now: https://example.com/unlock-account",
        "Attention: Your account security has been compromised. Verify your details: https://example.com/verify",
        "Critical Alert: Your account is at risk. Verify your identity now: https://example.com/verify-account",
        "Greetings! We have noticed unusual activity on your account. To ensure the security of your account, please verify your information by clicking the link below: https://example.com/verify-account",
        "Important Message: Your account has been accessed from a new location. Verify your identity now: https://example.com/verify-account",
        "URGENT: Immediate action required! Your account has been breached. Verify your details to secure it: https://example.com/verify",
        "Security Alert: Suspicious activity detected on your account. Verify your identity now: https://example.com/verify-account",
        "Account Security Notice: Your account has been compromised. Take action now to prevent further unauthorized access: https://example.com/secure-account",
        "WARNING: Your account is at risk of being suspended. Verify your identity to avoid suspension: https://example.com/verify",
        "Unauthorized Access: Your account has been accessed without authorization. Verify your account now: https://example.com/verify-account",
        "URGENT: Immediate action required! Verify your account to avoid suspension: https://example.com/verify",
        "Security Alert: Unusual activity detected on your account. Verify now: https://example.com/verify",
        "Your account has been suspended. Verify your identity to restore access: https://example.com/verify",
        "IMPORTANT: Your account has been compromised. Verify now to secure it: https://example.com/verify",
        "Suspicious activity detected on your account. Click here to verify: https://example.com/verify",
        "Account verification required: Your account has been flagged. Verify now: https://example.com/verify",
        "Your account security has been compromised. Verify your details: https://example.com/verify",
        "URGENT: Unauthorized access detected on your account. Verify now: https://example.com/verify",
        "Action required: Your account has been hacked. Verify your identity: https://example.com/verify",
        "Security Notice: Your account is at risk. Verify your account now: https://example.com/verify",
        "IMPORTANT: Your account is locked. Verify your identity to unlock: https://example.com/verify",
        "Your account has been suspended due to suspicious activity. Verify now: https://example.com/verify",
        "URGENT: Immediate action required! Your account is compromised. Verify now: https://example.com/verify",
        "Attention: Your account has been breached. Verify your details now: https://example.com/verify",
        "Security Alert: Your account has been accessed from a new device. Verify now: https://example.com/verify",
        "Your account has been restricted due to security concerns. Verify now: https://example.com/verify",
        "URGENT: Your account has been compromised. Verify your identity now: https://example.com/verify",
        "IMPORTANT: Unauthorized login detected on your account. Verify now: https://example.com/verify",
        "Suspicious login attempt detected on your account. Verify now: https://example.com/verify",
        "Account Security Notice: Your account has been hacked. Verify your details now: https://example.com/verify",
        "Your account security is at risk. Verify your identity to secure it: https://example.com/verify",
        "URGENT: Immediate action required! Your account is compromised. Verify your identity: https://example.com/verify",
        "Attention: Your account has been compromised. Verify your account now: https://example.com/verify",
        "Security Alert: Your account has been flagged. Verify your identity now: https://example.com/verify",
        "Your account has been breached. Click here to verify your identity: https://example.com/verify",
        "IMPORTANT: Your account security has been compromised. Verify now: https://example.com/verify",
        "Suspicious activity detected on your account. Verify your identity now: https://example.com/verify",
        "URGENT: Unauthorized access detected on your account. Take action now: https://example.com/verify",
        "Action required: Your account is at risk. Verify your identity now: https://example.com/verify",
        "Your account has been compromised. Verify your details now: https://example.com/verify",
        "Account Security Notice: Unauthorized login detected on your account. Verify now: https://example.com/verify",
        "Your account has been hacked. Click here to verify your identity: https://example.com/verify",
        "URGENT: Immediate action required! Your account is compromised. Verify now to secure it: https://example.com/verify",
        "Attention: Your account has been flagged for suspicious activity. Take action now: https://example.com/verify",
        "Security Alert: Your account has been breached. Verify your identity now: https://example.com/verify",
        "IMPORTANT: Your account is compromised. Verify your details to secure it: https://example.com/verify",
        "Suspicious login attempt detected on your account. Click here to verify: https://example.com/verify",
        "URGENT: Unauthorized access detected on your account. Verify your identity: https://example.com/verify",
        "Action required: Your account has been compromised. Take immediate action: https://example.com/verify",
        "Your account security is at risk. Take action now to secure it: https://example.com/verify",
        "Account Security Notice: Your account has been compromised. Verify your identity: https://example.com/verify",
        "Your account has been breached. Verify your details to secure it: https://example.com/verify",
        "URGENT: Immediate action required! Unauthorized access detected on your account. Click here to verify: https://example.com/verify",
        "Attention: Your account is compromised. Verify your identity now: https://example.com/verify",
        "Security Alert: Your account has been accessed without authorization. Verify now: https://example.com/verify",
        "IMPORTANT: Your account security has been breached. Click here to verify: https://example.com/verify",
        "Suspicious activity detected on your account. Take action now to secure it: https://example.com/verify",
        "URGENT: Unauthorized access detected on your account. Take action now: https://example.com/verify",
        "Action required: Your account security has been compromised. Click here to verify: https://example.com/verify",
        "Your account is at risk. Verify your identity now to secure it: https://example.com/verify",
        "Account Security Notice: Your account has been compromised. Take action now: https://example.com/verify"
    ]

    # Remove duplicates from email_texts
    email_texts = list(set(email_texts))
    
    non_phishing_email_texts = [
        "Thank you for your recent purchase!",
        "Your order has been confirmed.",
        "Reminder: Appointment tomorrow at 10 AM.",
        "Updates on your subscription.",
        "Invoice for your recent transaction.",
        "Confirmation of your registration.",
        "Your flight details for the upcoming trip.",
        "Weekly newsletter.",
        # Add more non-phishing email texts for variation
    ]
    
    #Code Author Bhanu Guragain

    # Generate phishing emails with label 1
    phishing_emails = [{'text': email_text, 'label': 1} for email_text in email_texts]

    # Generate non-phishing emails with label 0
    non_phishing_emails = [{'text': email_text, 'label': 0} for email_text in non_phishing_email_texts]

    # Generate additional non-phishing emails to balance the dataset
    additional_non_phishing_emails = [{'text': f"Normal email content {i}", 'label': 0} for i in range(num_emails - len(email_texts))]

    # Combine all emails
    all_emails = phishing_emails + non_phishing_emails + additional_non_phishing_emails

    # Shuffle the emails
    random.shuffle(all_emails)

    # Write the emails to the CSV file
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['text', 'label']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_emails)

# Example usage:
num_emails = 100000  # Generate millions of emails
file_path = '/home/bhanu/Desktop/email_data.csv'  # Specify the file path where the CSV file will be created
generate_phishing_emails(num_emails, file_path)
print(f"{num_emails} emails generated and saved to '{file_path}'.")
