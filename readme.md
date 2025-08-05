# Project Setup and Execution

This document outlines the steps to set up your environment, configure the API key, and run the Python script.

## 1. Prerequisites

*   **Python 3.6 or higher:** Make sure you have Python installed.  You can check your version with `python --version` or `python3 --version`.
*   **Required Packages:**  The script likely uses the Google Gemini API.  You will need to install the necessary package using pip.  Refer to your `main.py` script for the exact requirements.  A common command would be:

    ```bash
    pip install -r requirements.txt
    ```

    Replace `google-generativeai` and `python-dotenv` with any other necessary packages from your `main.py` file. The `python-dotenv` package is crucial for loading environment variables from the `.env` file.

## 2. Set Up Environment Variable

1.  **Create a `.env` file:** In the root directory of your project (the same directory as `main.py`), create a file named `.env`.

2.  **Add your Google Gemini API key:**  Open the `.env` file with a text editor and add the following line, replacing `your_google_gemini_api_key_here` with your actual API key:

    ```ini
    GOOGLE_API_KEY=your_google_gemini_api_key_here
    ```

## 3. Run the Script

1.  **Navigate to the Project Directory:** Open your terminal or command prompt and navigate to the directory where your `main.py` file and `.env` file are located. You can use the `cd` command (change directory).

2.  **Execute the Script:**  Run the Python script using the following command:

    ```bash
    python main.py
    ```

    If you are using Python 3, you might need to use:

    ```bash
    python3 main.py
    ```

## 4. Enter Your Website Description When Prompted

The script is designed to prompt you for input.

*   **Example Prompt:**  After running the script, you should see a prompt asking for a website description.

*   **Provide the Description:**  Type in a clear and concise description of your website.  For example:

    ```text
    A static landing page for a fictional productivity app called FocusFlow. The website should promote the app and encourage visitors to sign up or download it. It must include a hero section with the app name, a bold headline like “Stay focused. Get more done,” a short subheadline, a call-to-action button, and an appealing background image or gradient. Below that, include a features section highlighting three core features such as “Distraction Blocker,” “Task Timer,” and “Daily Goals,” each with an icon, title, and short description arranged in a responsive grid. Add a “How It Works” section with a 3-step explanation of how the app works—sign up, set goals, and start focusing—along with matching illustrations or icons. Include a testimonials section with 2–3 user quotes, names, and optional profile pictures, styled in cards or sliders with smooth GSAP entrance animations. Optionally, add a pricing section comparing Free and Premium plans in a clean table format. Include a final call-to-action banner to encourage downloads, with a contrasting background and clear CTA button. Finish with a footer containing links to Privacy Policy, Terms of Service, contact info, and social media icons. The design should be clean, modern, and responsive, using semantic HTML5, a minimalist color scheme (e.g., white, soft blues, and grays), a readable sans-serif font like Inter or Roboto, and GSAP animations for scroll effects, fades, and interactive elements.
    ```

*   **Press Enter:**  After typing your description, press the Enter key to submit it to the script.