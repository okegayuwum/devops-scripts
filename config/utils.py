import os
import json
import logging
import subprocess

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_all_files(directory):
    """Return a list of all files in the given directory."""
    return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def get_all_directories(directory):
    """Return a list of all directories in the given directory."""
    return [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

def read_json_file(file_path):
    """Read the contents of a JSON file."""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise

def execute_shell_command(command):
    """Execute a shell command and return the output."""
    try:
        output = subprocess.check_output(command, shell=True)
        return output.decode('utf-8')
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {command}\nError: {e}")
        raise