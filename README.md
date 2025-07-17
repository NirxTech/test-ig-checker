# IG Follower Checker

This project is a web application that allows users to check their Instagram followers and identify users who do not follow back. It is built using Flask and provides a simple interface for users to input their Instagram data.

## Project Structure

```
ig-follower-checker
├── app.py                # Main entry point of the web application
├── requirements.txt      # Lists dependencies required for the project
├── templates             # Contains HTML templates for the web application
│   ├── index.html       # Main page for user input
│   └── result.html      # Page to display results of the follower check
├── static               # Contains static files such as CSS
│   └── style.css        # CSS styles for the web application
└── utils                # Contains utility functions
    └── ig_checker.py    # Functions for loading JSON data and checking followers
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd ig-follower-checker
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   Start the Flask application by running:
   ```
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Usage

- Navigate to the main page where you can input your Instagram data.
- After submitting your data, the application will process the information and display the results, showing users who do not follow you back.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.