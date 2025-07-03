---
theme: uncover
class: invert
footer: 'Coder Trader | 03/07/25'
style: |
  body {
    background-color: #2E3440; /* Dark pastel background */
    color:rgb(65, 68, 71); /* Light pastel text */
  }
  h1, h2, h3 {
    font-size: 25px; /* Adjust as needed */
    color: #88C0D0; /* Soft pastel cyan for headers */
  }
  p {
    font-size: 15px; /* Adjust as needed */
    color:rgb(205, 209, 218); /* Light pastel text */
  }
  a {
    color: #A3BE8C; /* Pastel green for links */
  }
  code.language-python {
    font-size: 15px; /* Adjust as needed */
    background-color: #3B4252; /* Slightly darker for code blocks */
    color: #D08770; /* Muted pastel orange for code text */
  }
  ul, ol {
    font-size: 15px; /* Adjust as needed */
    color: rgb(205,209,218); /* Light pastel text */
  }
---
# Requests
---
## GET
Making a GET request in Python is straightforward, especially if you're using the `requests` library, which simplifies handling HTTP requests. Here's a basic example of how you can make a GET request:
---
1. **Install Requests Library** (if you haven't already):

   ```bash
   pip install requests
   ```
   ```bash
   uv add requests
   ```

2. **Example Python Code**:

   ```python
   import requests

   url = 'https://api.example.com/data'  # Replace with the URL you want to request

   # url = 'https://api.binance.com//api/v3/depth?symbol=BTCUSDT&limit=5'  # Replace with the URL you want to request
   # Sending GET request
   response = requests.get(url)

   # Checking if the request was successful (status code 200)
   if response.status_code == 200:
       # Printing the response content (usually JSON or HTML)
       print(response.json())  # Use response.text for non-JSON content
   else:
       print(f"Error {response.status_code}: {response.text}")
   ```
---
### Explanation:

* **`import requests`**: Imports the `requests` library.
* **`url`**: Specifies the URL you want to send a GET request to.
* **`requests.get(url)`**: Sends a GET request to the specified URL.
* **`response.status_code`**: Checks the HTTP status code returned by the server.
* **`response.json()` / `response.text`**: Retrieves the response content (JSON or raw text) returned by the server.

### Notes:

* Ensure you handle exceptions (like network errors or invalid responses) using try-except blocks for robustness in real-world applications.
* Modify the URL (`url`) and handling of response data (`response.json()` or `response.text`) based on the API or endpoint you are interacting with.

This example covers a basic scenario. Depending on your specific use case (such as handling headers, authentication, or more complex data), additional configurations may be necessary.
