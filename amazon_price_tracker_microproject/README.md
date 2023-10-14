# MicroProject - Amazon Price Tracker

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

This documentation provides an explanation of the Python script that monitors the price of an Amazon product and sends an email alert if the price drops below a predefined goal price.

## Purpose
The purpose of this script is to track the price of a specific Amazon product and send an email notification when the price falls below a specified threshold. This can be useful for users who want to be alerted when a product becomes more affordable.

## Dependencies
To run this script, you'll need the following dependencies:
- `confidential` module: This module contains confidential information like email and password, which are imported into the script.
- `smtplib`: This is a Python library used for sending email messages.
- `BeautifulSoup`: A Python library for web scraping and parsing HTML.
- `requests`: A library for making HTTP requests.

## Configuration
Before running the script, make sure to configure the following variables in the script:

- `GOAL_PRICE`: Set the target price you want to monitor for.
- `my_email`: Your Gmail email address.
- `password`: Your Gmail password (Note: Storing your email password in the script may not be secure).
- `url`: The URL of the Amazon product you want to monitor.
- `conf.TO_MAIL`: The email address where you want to receive price alerts.

## Workflow
1. Import necessary modules: The script starts by importing the required modules - `confidential`, `smtplib`, `BeautifulSoup`, and `requests`.

2. Fetch Amazon product details: The script uses the `requests` library to send an HTTP GET request to the Amazon product URL. It then uses BeautifulSoup to parse the HTML content of the product page to extract relevant information.

3. Extract product information: The script extracts the product's name and price from the Amazon page. It calculates the total price by combining the whole and fractional parts of the price.

4. Compare prices: The script compares the extracted price with the `GOAL_PRICE` to determine if the product is now affordable.

5. Send an email alert: If the price is lower than the target price, the script uses `smtplib` to connect to the Gmail SMTP server, logs in with your email and password, and sends an email alert with the product name, price, and a link to the Amazon page.

## Security Considerations
Storing your Gmail password in a script is not recommended from a security perspective. Instead, you should use secure methods for storing sensitive information, such as environment variables or configuration files.

## Usage
To use this script, follow these steps:
1. Configure the script by setting the `GOAL_PRICE`, `my_email`, `password`, `url`, and `conf.TO_MAIL` variables.
2. Run the script, and it will periodically check the price of the specified Amazon product.
3. If the price falls below the specified `GOAL_PRICE`, you will receive an email alert.

## Disclaimer
This script is provided for educational purposes and should be used responsibly. Amazon's terms of service may prohibit automated scraping of their website, so be sure to review and comply with their policies.
