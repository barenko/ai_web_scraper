## Link to get chromewebdriver:

    https://googlechromelabs.github.io/chrome-for-testing/#stable

## To run

    py -m poetry shell
    py -m streamlit run .\src\ai_web_scraper\main.py

## How to install Ollama3

- Install ollama from https://ollama.com/download
- You can get the ollama LLM options from their github project: https://github.com/ollama/ollama. Just download one that runs ok with your machine

  ollama run llama3.1


## Usage example

- Start the server
- Start ollama
- Open the browser http://localhost:8501
- Insert the URL https://www.fundamentus.com.br/detalhes.php?papel=ITUB4
- Insert the description: Generate a table with all table data found. Name the  first column as "Item" and the second as "Value". Translate the first column  investment terms to english and use the translated term instead of the original. Do not translate the second column.
