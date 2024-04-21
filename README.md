# KRA PIN Verification System

This project is a Python-based system for automating the verification of Kenya Revenue Authority (KRA) Personal Identification Numbers (PINs). It uses Selenium to interact with the KRA website, solve CAPTCHAs, and retrieve information related to a given KRA PIN. The system is designed to streamline the process of validating KRA numbers and obtaining owner information.

## Project Structure

- `captcha_solver.py`: Contains the logic to solve CAPTCHAs by capturing CAPTCHA images from the KRA website and using Optical Character Recognition (OCR) to determine the correct answer.
- `main.py`: The entry point of the system. It initializes a `PinChecker` instance and processes a given KRA PIN.
- `pin_checker.py`: Defines the `PinChecker` class, which automates the interaction with the KRA website. It handles PIN input, CAPTCHA solving, and data retrieval.
- `web_driver.py`: Contains the `create_web_driver` function to initialize a Selenium WebDriver for Chrome. This is used to automate web interactions.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver
- Google Chrome
- PIL (Python Imaging Library)
- Tesseract-OCR

Ensure that you have Chrome installed and that the ChromeDriver version matches your Chrome version. Additionally, Tesseract-OCR must be installed, and its path should be correctly configured in `captcha_solver.py`.

## How to Use

1. Clone the repository to your local machine.
2. Configure the path to ChromeDriver and Tesseract-OCR in `pin_checker.py` and `captcha_solver.py`, respectively.
3. Open `main.py` and replace `'Your_PIN_Here'` with the actual KRA PIN you want to validate.
4. Run `main.py` to initiate the KRA PIN verification process.
5. The system will interact with the KRA website, solve CAPTCHAs, and retrieve information associated with the given KRA PIN.

## Notes

- This system is intended for educational purposes. Ensure you comply with all applicable laws and the KRA website's terms of service when using it.
- Automated CAPTCHA solving may be against certain website policies. Use with caution and responsibility.
- For the system to work properly, all required dependencies must be installed and correctly configured.

## License

Use it however you wannna :)
