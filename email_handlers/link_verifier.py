from colorama import Fore, Style
import requests

class LinkVerifier:
    def __init__(self, links):
        # Process links to remove trailing '>'
        self.links = [link.rstrip('>') for link in links]

    def check_links_present(self, expected_links):
        missing_links = [link for link in expected_links if link not in self.links]
        if missing_links:
            return {"status": "fail", "missing_links": missing_links}
        return {"status": "pass", "missing_links": []}

    def verify_link_targets(self):
        link_status = {}  # Initialize link_status as an empty dictionary
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        for link in self.links:
            try:
                response = requests.get(link, headers=headers, allow_redirects=True, timeout=10)
                if response.status_code == 200:
                    link_status[link] = "valid"
                else:
                    link_status[link] = "invalid"
            except requests.RequestException as e:
                print(f"Error verifying link {link}: {e}")  # Debugging line to see error details
                link_status[link] = "unreachable"
        return link_status

    def print_link_verification_results(self):
        """Print the verification results for all links with colored output."""
        link_status = self.verify_link_targets()
        for link, status in link_status.items():
            if status == "valid":
                print(Fore.GREEN + f"Link: {link}, Status: {status}" + Style.RESET_ALL)
            elif status == "invalid":
                print(Fore.RED + f"Link: {link}, Status: {status}" + Style.RESET_ALL)
            elif status == "unreachable":
                print(Fore.YELLOW + f"Link: {link}, Status: {status}" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + "No links found!" + Style.RESET_ALL)