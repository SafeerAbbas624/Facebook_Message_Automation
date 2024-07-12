# Facebook Message Automation Script

## Introduction
This script is a Python automation tool that uses Selenium to log in to Facebook and reply to messages using multiple accounts in parallel. It's designed to simplify the process of managing multiple Facebook accounts and responding to messages.

## Features
- Multi-account support: The script can log in to multiple Facebook accounts and reply to messages simultaneously.
- Random user agent: The script uses a random user agent to mimic human behavior and avoid detection by Facebook's anti-bot systems.
- Configurable sleep times: The script includes random sleep times to avoid overwhelming Facebook's servers and to simulate human behavior.
- Error handling: The script includes error handling to handle exceptions and continue running even if an error occurs.

## Installation for All OS

### Windows
1. Install Python from the official website: Python Downloads
2. Install the required libraries by running the following command in your terminal:
    ```sh
    pip install selenium webdriver_manager fake_useragent
    ```
3. Download the ChromeDriver executable from the official website: ChromeDriver Downloads
4. Add the ChromeDriver executable to your system's PATH environment variable.

### macOS (via Homebrew)
1. Install Python using Homebrew:
    ```sh
    brew install python
    ```
2. Install the required libraries by running the following command in your terminal:
    ```sh
    pip install selenium webdriver_manager fake_useragent
    ```
3. Install ChromeDriver using Homebrew:
    ```sh
    brew install chromedriver
    ```
4. Add the ChromeDriver executable to your system's PATH environment variable.

### Linux (Ubuntu-based)
1. Install Python using apt:
    ```sh
    sudo apt-get install python3
    ```
2. Install the required libraries by running the following command in your terminal:
    ```sh
    pip3 install selenium webdriver_manager fake_useragent
    ```
3. Install ChromeDriver using apt:
    ```sh
    sudo apt-get install chromedriver
    ```
4. Add the ChromeDriver executable to your system's PATH environment variable.

## Usage
1. Create a file named `login_data.txt` with the following format:
    ```sh
    email|password|message
    email|password|message
    ...
    ```
    Replace `email`, `password`, and `message` with your actual Facebook login credentials and the message you want to send.
   Put the 'login_data.txt' file in same directory of script.
3. Run the script using Python:
    ```sh
    python script.py
    ```
4. The script will log in to each Facebook account, navigate to the messages page, and reply to any new messages with the specified message.

## Thanks Note
Thank you for using this script! I hope it helps you manage your Facebook accounts more efficiently. If you have any questions or issues, feel free to reach out to me.
