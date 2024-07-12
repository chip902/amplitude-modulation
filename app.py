import requests
import pandas as pd
import json
import base64
import zipfile
import gzip
from io import BytesIO


def export_amplitude_events(api_key, secret_key, project_index, project_name):
    base_url = 'https://amplitude.com/api/2/export'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + base64.b64encode(f"{api_key}:{secret_key}".encode()).decode()
    }
    params = {
        'start': '20240709T00',
        'end': '20240710T00'
    }
    print('Fetching data...')
    response = requests.get(base_url, params=params,
                            headers=headers, timeout=60)

    if response.status_code == 200:
        # Handle zip file response
        zip_file = BytesIO(response.content)
        with zipfile.ZipFile(zip_file, 'r') as z:
            for file_name in z.namelist():
                print(f"Extracting {file_name}...")
                with z.open(file_name) as f:
                    # Check if the file is gzip compressed
                    if file_name.endswith('.gz'):
                        with gzip.GzipFile(fileobj=f) as gz:
                            events_data = gz.read().decode('utf-8')
                            return events_data
                    else:
                        events_data = f.read().decode('utf-8')
                        return events_data
    else:
        print(f"Failed to fetch events. Status Code: {response.status_code}")
        return None


def get_amplitude_events(api_key, secret_key, project_index, project_name):
    base_url = 'https://amplitude.com/api/2/events/list'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + base64.b64encode(f"{api_key}:{secret_key}".encode()).decode()
    }
    params = {
        'non_active': 'false'
    }
    print(headers)
    response = requests.get(base_url, headers=headers,
                            params=params, timeout=60)

    # Write response to a file
    with open(f'response_{project_name}_{project_index}.json', 'w', encoding='utf-8') as file:
        file.write(response.text)

    if response.status_code == 200:
        events = response.json().get('data', [])
        return events
    else:
        print(f"Failed to fetch events. Status Code: {response.status_code}")
        return []


def main():
    with open('project_credentials.json', 'r') as file:
        project_credentials = json.load(file)

    for index, credentials in enumerate(project_credentials):
        api_key = credentials['api_key']
        secret_key = credentials['secret_key']
        project_name = credentials['project_name']

        events = export_amplitude_events(
            api_key, secret_key, index, project_name)
        if events:
            events_list = [json.loads(line)
                           for line in events.strip().split('\n')]
            df = pd.DataFrame(events_list)
            df.to_excel(f'events_project_{index + 1}.xlsx', index=False)
            print(f"Exported events for project {
                  index + 1} to events_project_{index + 1}.xlsx")
        else:
            print(f"No active events found for project {index + 1}")


if __name__ == '__main__':
    main()
