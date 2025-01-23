#proof_handler.py
import re
import requests
from colorama import Fore, Style

from email_handlers.link_verifier import LinkVerifier

class ProofHandler:
    def __init__(self, email):
        self.email = email

    def get_subject(self):
        return self.email.Subject

    def get_body(self):
        return self.email.Body
    
    def get_cleaned_body(self):
        """remove urls from the email body"""
        email_body = self.get_body()
        cleaned_body = re.sub(r'<https?://[^\s\"\'<>]+>', '', email_body)
        # Split lines and remove the first line (preheader)
        body_lines = cleaned_body.splitlines()
        cleaned_body_without_preheader = "\n".join(body_lines[1:]).strip()
        return cleaned_body_without_preheader

    
    def get_preheader(self):
        """Return the first line of the email body as the preheader."""
        email_body = self.get_body()
        preheader = email_body.splitlines()[0] if email_body else ""
        return preheader.strip()

    def get_links(self):
        """Extract all links using a simple regex."""
        email_body = self.get_body()

        # Simplified regex to find all HTTP/HTTPS links
        links = re.findall(r'https?://[^\s\"\'<>]+', email_body)

        # Strip any potential trailing whitespace or special characters
        links = [link.strip() for link in links if link]
        return links

    def process_flagged_emails(self, flagged_emails):
        """Process all flagged emails."""
        for email in flagged_emails:
            proof_handler = ProofHandler(email)
            proof_handler.print_message_info_with_links()
            
    def process_first_email(self, email):
        """Process the first email."""
        proof_handler = ProofHandler(email)
        proof_handler.print_message_info_with_links()

    def print_message_info(self):
        """Print the subject and body of the email."""
        print(f"Subject: {self.get_subject()}")
        print(f"Preheader: {self.get_preheader()}")
        print(f"Body:\n {self.get_cleaned_body()}")

    def print_message_info_with_links(self):
        """Print the email's subject, body, and link verification results."""
        links = self.get_links()
        if links:
            self.print_message_info()
        else:
            print("No links found in the email.")

        link_verifier = LinkVerifier(links)
        link_verifier.print_link_verification_results()
