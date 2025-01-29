from colorama import Fore, Style
import requests
from security import safe_requests

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
        final_urls = {}  # Initialize final_urls as an empty dictionary
        unreachable_links = {} # Initialize unreachable_links as an emapty dictionary
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        for link in self.links:
            try:
                response = safe_requests.get(link, headers=headers, allow_redirects=True, timeout=10)
                final_url = response.url
                final_urls[link] = final_url
                if response.status_code == 200 or "facebook" in final_url:
                    link_status[link] = "valid"
                else:
                    link_status[link] = "invalid"
            except requests.RequestException as e:
                print(f"Error verifying link {link}: {e}")  # Debugging line to see error details
                link_status[link] = "unreachable"
        return link_status, final_urls, unreachable_links

    def print_link_verification_results(self):
        link_status, final_urls, unreachable_links = self.verify_link_targets()
        invalid_links = []
        unreachable_links = []
        """Print the verification results for all links with colored output."""

        for link, status in link_status.items():
            if status == "valid":
                print(Fore.GREEN + f"Link: {link}, Status: {status}" + Style.RESET_ALL)
            elif status == "invalid":
                print(Fore.RED + f"Link: {link}, Status: {status}" + Style.RESET_ALL)
                invalid_links.append((link, final_urls[link]))
            elif status == "unreachable":
                print(Fore.YELLOW + f"Link: {link}, Status: {status}" + Style.RESET_ALL)
                unreachable_links.append((link, unreachable_links[link]))
            else:
                print(Fore.GREEN + "No links found!" + Style.RESET_ALL)
        print(Fore.LIGHTCYAN_EX + "============ Link Verification Results ============" + Style.RESET_ALL)
        # Print the count of invalid links
        print(Fore.GREEN + f"VALID LINK COUNT: {len(link_status) - len(invalid_links)}" + Style.RESET_ALL)
        print(Fore.YELLOW + f"UNREACHABLE LINK COUNT: {len(unreachable_links)}" + Style.RESET_ALL)
        print(Fore.RED + f"INVALID LINK COUNT: {len(invalid_links)}" + Style.RESET_ALL)

        # Print the final URLs for each invalid link
        print(Fore.LIGHTCYAN_EX + "\n\n============ Invalid Link Details ============" + Style.RESET_ALL)
        for link, final_url in invalid_links:
            print(Fore.RED + f"\nINVALID LINK: {link} \n REDIRECTED TO: {final_url}" + Style.RESET_ALL)

        if not link_status:
            print(Fore.GREEN + "No links found!" + Style.RESET_ALL)
