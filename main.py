from email_handlers.outlook_connector import OutlookConnector
from email_handlers.email_manager import EmailManager
from email_handlers.proof_handler import ProofHandler
import os
from dotenv import load_dotenv

#load environment variables
load_dotenv()

#read environment variables
folder_path_str = os.getenv("FOLDER_PATH")
folder_path = folder_path_str.split(",")

def main():
    # Initialize Outlook connection and folder navigation
    connector = OutlookConnector()

    proofs_folder = connector.get_folder(folder_path)

    # Manage emails in the folder
    email_manager = EmailManager(proofs_folder)

    # Get flagged emails and use ProofHandler to process them
    flagged_emails = email_manager.get_flagged_emails()

    # Process flagged emails if found
    if flagged_emails:
        for email in flagged_emails:
            proof_handler = ProofHandler(email)
            proof_handler.print_message_info_with_links()
    else:
        # If no flagged emails, process the first email
        first_email = email_manager.get_first_email()
        if first_email:
            proof_handler = ProofHandler(first_email)
            proof_handler.print_message_info_with_links()

if __name__ == "__main__":
    main()
