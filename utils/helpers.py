import requests

class Helpers:
    @staticmethod
    def check_status_code(url: str, expected_status_code: int) -> bool:
        response = requests.get(url)
        actual_status_code = response.status_code
        print(f"Actual status code: {actual_status_code}")
        return actual_status_code == expected_status_code