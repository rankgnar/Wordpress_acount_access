WordPress Access Script

This script allows you to access a WordPress site and save the credentials in CSV and JSON files.

Requirements

- Python installed
- Required libraries (can be installed with pip install requests)

Usage

1. Clone or Download the Repository:
   git clone https://github.com/rankgnar/Wordpress_acount_access.git
   cd Wordpress_acount_access

2. Run the Script from the Command Line:

   - On Windows:
     ```bash
     python main.py
     ```
   - On Mac/Linux:
     ```bash
     python3 main.py
     ```

3. Enter the Required Data:

   - Domain of WordPress site (e.g., https://yourdomain.com)
   - Username
   - Password

4. **Ensure JWT-Auth is Configured on WordPress:**

   - Before using this script, make sure the WordPress site has the JWT-Auth plugin configured. You can find the plugin (https://wordpress.org/plugins/jwt-authentication-for-wp-rest-api/).

5. The script will perform authentication, save information in CSV and JSON files, and display messages in the console.

File Structure

- domains_wordpress.csv: CSV file containing the list of WordPress domains.
- wordpress_json_files/: Folder containing JSON files with access credentials.

Notes

- Ensure you have sufficient permissions to write in the folder where the script is located.
- This script has no graphical interface and works only from the command line.
