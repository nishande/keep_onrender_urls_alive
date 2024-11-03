from flask import Flask, render_template
import threading
import time
import requests
import json
from datetime import datetime
from queue import Queue
import logging
from collections import deque
import os

app = Flask(__name__)

# Constants
LOG_FILE = 'application.log'
MAX_LOG_LINES = 500

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class LogHandler:
    def __init__(self, filename, max_lines):
        self.filename = filename
        self.max_lines = max_lines
        
    def write_log(self, message):
        # Read existing logs
        logs = self.read_logs()
        logs.append(message)
        
        # Keep only the last max_lines
        if len(logs) > self.max_lines:
            logs = logs[-self.max_lines:]
            
        # Write back to file
        with open(self.filename, 'w') as file:
            for log in logs:
                file.write(log + '\n')

    def read_logs(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r') as file:
            return [line.strip() for line in file.readlines()]

# Initialize log handler
log_handler = LogHandler(LOG_FILE, MAX_LOG_LINES)

def call_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        log_message = f"[{get_timestamp()}] Successfully called the URL: {url}"
        log_handler.write_log(log_message)
    except requests.RequestException as e:
        log_message = f"[{get_timestamp()}] Error occurred: {e}"
        log_handler.write_log(log_message)

def background_task():
    while True:
        try:
            with open('urls.json', 'r') as file:
                data = json.load(file)
                urls = data['urls']

            for url in urls:
                call_url(url)
            time.sleep(90)  # Wait for 90 seconds
        except Exception as e:
            log_message = f"[{get_timestamp()}] Error in background task: {e}"
            log_handler.write_log(log_message)

# Start the background thread
background_thread = threading.Thread(target=background_task, daemon=True)
background_thread.start()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_logs')
def get_logs():
    logs = log_handler.read_logs()
    return {'logs': logs[::-1]}  # Reverse the logs to show newest first

if __name__ == '__main__':
    app.run(debug=True)