# Email Processing Project

## Overview
This project is designed to process emails from an Outlook inbox. It connects to your Outlook account, retrieves flagged emails, and processes them to extract and verify links. The project uses environment variables to configure the folder paths and other settings.

## Setup

### 1. Activate the Python Environment
First, create and activate a virtual environment. You can use `venv` to create a virtual environment.

#### On Windows:
```sh
python -m venv myenv
.\myenv\Scripts\activate
```

#### On macOS/Linux:
```sh
python3 -m venv myenv
source myenv/bin/activate
```
### 2. Install Requirements
Install the required packages using pip and the 'reqirements.txt' file.
```sh
pip install -r requirements.txt
```
### 3. Set Up Environment Variables
Create a '.env' file in the root directory of your project and set the FOLDER_PATH variable to specify the folder path in your Outlook account.
```sh
# .env
FOLDER_PATH=Directory,Subdirectory 
```
(e.g. Starbucks, Proofs)

### 4. Run the Unit Tests
To run the tests, use pytest. Ensure you are in the virtual environment before running the tests.
```sh
pytest
```
### 5. Set an Email to be Tested
To verify an email, outlook must be open on your os.  Mark the target email as flagged in your Outlook inbox. The script will process the most recent flagged email.

### 6. Run the Script
To run the script and process the emails, execute the main.py file.
```sh 
python main.py
```
After the script completes you will see the following output: 
Email Subject, Preheader and Body
Link Verification Results Counts and Detailed summary of invalid links and their corresponding redirects. 

### Known Limitations
The script will only process the latest flagged email in your inbox. If you have multiple flagged emails, the one with the most recent date will be processed. 

The script may occasionally flag links as invalid that are valid especially if there are complex redirects or authentication layers. Always double check the output by visiting the invalid links. 

### Project Structure

email_processing/
├── email_handlers/
│   ├── __init__.py
│   ├── email_manager.py
│   ├── outlook_connector.py
│   ├── proof_handler.py
│   └── link_verifier.py
├── tests/
│   ├── test_email_manager.py
│   ├── test_outlook_connector.py
│   ├── test_proof_handler.py
│   └── test_link_verifier.py
├── .env
├── .gitignore
├── main.py
├── pytest.ini
├── README.md
└── requirements.txt

### Detailed Explanation of Files

- **main.py**: The main script that initializes the Outlook connection, retrieves flagged emails, and processes them.
- **email_handlers/**: Contains the modules for handling emails, connecting to Outlook, and verifying links.
- **tests/**: Contains the test files for the project.
- **.env**: Environment variables file.
- **requirements.txt**: Lists the dependencies required for the project.
- **pytest.ini**: Configuration file for pytest.
- **README.md**: This file, providing an overview and setup instructions for the project.

### Contact
For any questions or issues, please open an issue on the GitHub repository.


