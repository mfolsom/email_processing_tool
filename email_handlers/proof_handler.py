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