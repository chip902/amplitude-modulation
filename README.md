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