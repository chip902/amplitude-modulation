# Amplitude Modulation
# Get all your events from Amplitude!!!

This script fetches events from Amplitude for multiple projects and exports them to separate Excel files.

## Prerequisites

- Python 3.x
- Virtual Environment (venv)
- Dependencies: `requests`, `pandas`, `openpyxl`

## Setup

### 1. Create and Activate Virtual Environment

#### On macOS and Linux:
```sh
python -m venv venv
source venv/bin/activate
```

#### On Windows:
```sh
python -m venv venv
venv\Scripts\activate
```

### 2. Install Deps
```sh
pip install requests pandas openpyxl
```

### 3. Create your credential file
Copy the .example file to `project_credentials.json` or create it from scratch

```sh
[
    {
        "api_key": "API_KEY_1",
        "secret_key": "SECRET_KEY_1"
    },
    {
        "api_key": "API_KEY_2",
        "secret_key": "SECRET_KEY_2"
    }
]
```
Replace API_KEY_1, SECRET_KEY_1, etc., with your actual Amplitude API keys and secret keys.

## License

This project is licensed under the MIT License.

## Troubleshooting

### Self-Signed Certificates

If you encounter issues connecting using a self-signed certificate on a protected network, you can either bypass SSL verification (not recommended for production) or provide the path to your self-signed certificate.

#### Bypassing SSL Verification

**Note:** This method is not recommended for production environments due to security risks.

Update the `requests.get` call in the `get_amplitude_events` function to disable SSL verification:

```python
response = requests.get(base_url, headers=headers, params=params, verify=False)
```

#### Using a Self-Signed Certificate

1.	Ensure the self-signed certificate is saved on your file system, e.g., path/to/self-signed-cert.pem.
2.	Update the requests.get call in the get_amplitude_events function to provide the path to the certificate:

```python
cert_path = 'path/to/self-signed-cert.pem'
response = requests.get(base_url, headers=headers, params=params, verify=cert_path)
```

This will allow the script to connect using the self-signed certificate.

