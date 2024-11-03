# Flask App for Calling URLs

This Flask application is designed to call URLs from a JSON file and log the results. It also serves a home page and provides an endpoint to retrieve logs.

## Features

- **Logging**: Logs messages to a file with a maximum number of lines.
- **URL Calling**: Calls URLs from a JSON file and logs the results.
- **Background Task**: Runs a background task to periodically call URLs.
- **Home Page**: Serves a home page using a template.
- **Get Logs**: Provides an endpoint to retrieve logs.

## How to Run

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

3. Open your browser and navigate to `http://127.0.0.1:5000/` to see the home page.

4. To retrieve logs, navigate to `http://127.0.0.1:5000/get_logs`.

## Dependencies

- Flask
- requests

## Files

- `app.py`: The main Flask application.
- `templates/index.html`: The HTML template for the home page.
- `urls.json`: The JSON file containing URLs to call.
- `application.log`: The log file.

## License

This project is licensed under the MIT License.
