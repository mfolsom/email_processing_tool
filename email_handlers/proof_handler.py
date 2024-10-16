import re

class ProofHandler:
    def __init__(self, email):
        self.email = email

    def get_subject(self):
        return self.email.Subject
    
    def get_body(self):
        return self.email.Body
    
    def get_links(self):
        email_body = self.get_body()
        links = re.findall(r'(https?://[^\s]+)', email_body)
        return links
    
    def print_message_info(self):
        """Print the subject and body of the email."""
        print(f"Subject: {self.get_subject()}")
        print(f"Body: {self.get_body()}")

    def process_flagged_emails(self, flagged_emails):
        """Process the flagged emails if any are found."""
        if len(flagged_emails) > 0:
            first_flagged = flagged_emails[0]
            print(f"Number of flagged emails: {len(flagged_emails)}")
            ProofHandler(first_flagged).print_message_info()
        else:
            print("No flagged emails found.")

    def process_first_email(self, email):
        """Process the first email if no flagged emails are found."""
        print("Retrieving the first email.")
        ProofHandler(email).print_message_info()