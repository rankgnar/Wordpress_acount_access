import json
import os
import requests
import csv

DOMAIN_WORDPRESS = "domains_wordpress.csv"
WPS_JSON_FILE = "wordpress_json_files"

def update_json_list_wp(json_folder_path):
    updated_json_files = [file for file in os.listdir(json_folder_path) if file.endswith('.json')]
    return updated_json_files

def write_to_csv(domain, file_path):
    file_exists = os.path.isfile(file_path)
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Domains_wordpress'])
        writer.writerow([domain])

def access_wordpress_account(domain, username, password):
    write_to_csv(domain, DOMAIN_WORDPRESS)
    authentication_url = f'{domain}/wp-json/jwt-auth/v1/token'

    credentials = {'username': username, 'password': password}

    try:
        response = requests.post(authentication_url, json=credentials)

        if response.status_code == 200:
            data = response.json()
            token = data.get('token')
            if token:
                cleaned_domain = domain.replace("//", "__").replace(".", "_").replace(":", "_")
                json_folder_path = WPS_JSON_FILE
                with open(f'{json_folder_path}/{cleaned_domain}_credential.json', 'w') as file:
                    json.dump({'token': token, 'exp': None}, file)  
            else:
                print('Unable to retrieve JWT token from the response.')
        else:
            print(f'Request error: {response.status_code}')

    except Exception as e:
        print(f'Error: {str(e)}')


wordpress_domain = input("Enter the domain of WordPress site (example: https://yourdomain.com): ")
wordpress_username = input("Enter the username: ")
wordpress_password = input("Enter the password: ")


access_wordpress_account(wordpress_domain, wordpress_username, wordpress_password)
