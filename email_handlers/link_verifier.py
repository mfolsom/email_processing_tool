import requests

class LinkVerifier:
    def __init__(self, links):
        self.links = links

    def check_links_present(self, expected_links):
        missing_links = [link for link in expected_links if link not in self.links]
        if missing_links:
            return {"status": "fail", "missing_links": missing_links}
        return {"status": "pass", "missing_links": []}

    def verify_link_targets(self):
        link_status = {}  # Initialize link_status as an empty dictionary
        for link in self.links:
            try:
                response = requests.head(link)
                if response.status_code == 200:
                    link_status[link] = "valid"
                else:
                    link_status[link] = "invalid"
            except requests.RequestException:
                link_status[link] = "unreachable"
        return link_status