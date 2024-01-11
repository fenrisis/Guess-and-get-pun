import requests


def get_external_ip():
    try:
        response = requests.get('https://api.ipify.org')
        if response.status_code == 200:
            return response.text
        else:
            return "Failed to obtain an IP address."
    except Exception as e:
        return f"An error has occurred: {e}."


if __name__ == "__main__":
    print(f"Your external IP address: {get_external_ip()}")
    