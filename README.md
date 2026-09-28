# Tavily search practice

A small Python script that searches the web and prints five results with their titles, links, and snippets. It starts with an EEG research query, but you can supply any query.

## Set up on Windows PowerShell

```powershell
git clone https://github.com/nickmendoza224/tavily-search-practice.git
cd tavily-search-practice
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

Get an API key from the [Tavily dashboard](https://app.tavily.com/). Set it in the current PowerShell window (replace the example value):

```powershell
$env:TAVILY_API_KEY = "your-key-here"
.venv\Scripts\python search.py
```

To try your own question:

```powershell
.venv\Scripts\python search.py "What is an EEG window in seizure detection?"
```

The key is read from the `TAVILY_API_KEY` environment variable. Never commit your real key to GitHub. The temporary value above disappears when you close that PowerShell window.
