# ChatGPT Web App

This is a simple web application that allows you to chat with ChatGPT using LangChain and Streamlit.

## Prerequisites

- Python 3.6 or higher
- langchain library
- streamlit library
- python-dotenv library

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. Install the required dependencies:

   ```shell
   pip install langchain streamlit python-dotenv
   ```

## Usage

1. Obtain an API key from OpenAI and set it in the `.env` file:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

2. Run the application:

   ```shell
   streamlit run main.py
   ```

3. Open your web browser and visit `http://localhost:8501` to access the web app.

4. Enter your message in the text input and click the "Send" button to chat with ChatGPT.

## Configuration

- The `OPENAI_API_KEY` environment variable should be set in the `.env` file to authenticate with the OpenAI API. Make sure to replace `your_api_key_here` with your actual API key.

## License

This project is licensed under the [MIT License](LICENSE).
