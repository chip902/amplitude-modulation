import requests
import pandas as pd
import json
import base64


def get_amplitude_events(api_key, secret_key, project_index):
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
    with open(f'response_{project_index}.json', 'w', encoding='utf-8') as file:
        file.write(response.text)

    if response.status_code == 200:
        events = response.json().get('data', [])
        return events
    else:
        print(f"Failed to fetch events. Status Code: {response.status_code}")
        return []


def main():
    with open('project_credentials.json', 'r', encoding='utf-8') as file:
        project_credentials = json.load(file)

    for index, credentials in enumerate(project_credentials):
        api_key = credentials['api_key']
        secret_key = credentials['secret_key']

        events = get_amplitude_events(api_key, secret_key, index)
        if events:
            df = pd.DataFrame(events)
            df.to_excel(f'events_project_{index + 1}.xlsx', index=False)
            print(f"Exported events for project {
                  index + 1} to events_project_{index + 1}.xlsx")
        else:
            print(f"No active events found for project {index + 1}")


if __name__ == '__main__':
    main()
