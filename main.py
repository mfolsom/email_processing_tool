from email_handlers.outlook_connector import OutlookConnector
from email_handlers.email_manager import EmailManager
from email_handlers.proof_handler import ProofHandler

def main():
    # Initialize Outlook connection and folder navigation
    connector = OutlookConnector()
    folder_path = ["Starbucks", "Proofs"]  # Path to the specific folder
    proofs_folder = connector.get_folder(folder_path)

    # Manage emails in the folder
    email_manager = EmailManager(proofs_folder)

    # Get flagged emails and use ProofHandler to process them
    flagged_emails = email_manager.get_flagged_emails()
    proof_handler = ProofHandler(None)  # Create an instance to use static methods

    # Process flagged emails if found
    proof_handler.process_flagged_emails(flagged_emails)

    # If no flagged emails, process the first email
    if not flagged_emails:
        first_email = email_manager.get_first_email()
        proof_handler.process_first_email(first_email)

if __name__ == "__main__":
    main()
