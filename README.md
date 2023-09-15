# edgeAutomation

# Instructions for Using the Program

Follow these steps to use the program effectively:

1. **Retrieve Microsoft Edge Version:**
   - Navigate to your locally installed Microsoft Edge browser.
   - Click on the ellipsis (...) icon in the top-right corner.
   - Select "Settings."
   - Scroll down and click on "About Microsoft Edge."
   - Note the Edge version displayed. You will need this version in the next step.

2. **Download Microsoft Edge WebDriver:**
   - Visit the Microsoft Edge WebDriver download page: [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
   - Download the WebDriver that matches the Edge version obtained in Step 1. Make sure to download the appropriate version for your operating system.

3. **Prepare the Info CSV File:**
   - Create or edit the `info.csv` file to provide the required details for each website you want to automate. The CSV file should have the following columns:
   
     - `link`: The URL of the website to test.
     - `username_id`: The HTML element ID for the username input field.
     - `password_id`: The HTML element ID for the password input field.
     - `login_id`: The HTML element ID for the login/submit button.
     - `username`: The username to use for logging in.
     - `password`: The password to use for logging in.

   Here's an example structure for the `info.csv` file: <br>
   link,username_id,password_id,login_id,username,password
   https://example.com,usernameField,passwordField,loginButton,user123,Password123
   https://another-site.com,usernameInput,passwordInput,loginBtn,admin,SecretPwd

    

# features to implement
crpytography encryption of credentials <br>