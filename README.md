# URL Caller Script

This script is designed to call a list of URLs every 60 minutes to keep them active. The URLs are stored in a JSON file (`urls.json`).

## Features

- Calls each URL every 60 minutes.
- Prints a success message for each URL called.
- Retries on failure.

## Requirements

- Python 3.x
- `requests` library

## Usage

1. Ensure you have Python 3.x installed.
2. Install the required dependencies by running:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the script:
   ```sh
   python script.py
   ```

## Configuration

The URLs to be called are stored in the `urls.json` file. You can add or remove URLs as needed.

Example `urls.json`:
```json
{
    "urls": [
        "https://example.com/api/endpoint1",
        "https://example.com/api/endpoint2",
        "https://example.com/api/endpoint3"
    ]
}
