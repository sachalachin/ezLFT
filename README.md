# ezLFT

![](https://img.shields.io/github/license/sachalachin/ezLFT)

ezLFT is a Python program to speed up the process of ordering NHS COVID-19 lateral flow tests.


## Before you begin

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements listed in the *requirements.txt* file:

	```bash
pip install -r requirements.txt
```		

- The Google Chrome driver executable should be in the same directory as *main.py*. You can use the *chromedriver.exe* included in this repo, or download your own on the [ChromeDriver website](https://chromedriver.chromium.org/downloads).

- Enter your NHS login details into the *.env* file in the following format:
```
EMAIL = "youremail@here.com"
PASSWORD = "yourpassword"
```

- You will need to have used the lateral flow ordering service at least once manually before running ezLFT. This is so the service is able to save your address.


## Usage

You can run the program with the following terminal command:
```python
python main.py
```
ezLFT is headless unless specifically modified to show the GUI. Progress will be shown in the terminal, in addition to the order confirmation prompt at the end.

## Disclaimer
Please use this tool responsibly and in line with the terms and conditions of the NHS services. You can only order one box of tests per day, this program is designed to help automate that process.


## License
[Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)
