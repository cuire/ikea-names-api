# ikea-names-api
Small API using RNN model to generate names for Ikea products.

To make that API, I used pytorch and flask. Original dataset with existing Ikea products was taken from kaggle.
Then data was normalized and used to train RNN model.
Model was saved and then used in flask app to generate names.

## Installation

Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

```bash
pip install -r requirements.txt
```

```bash
python run.py
```

## Usage

<!--  write paragraph about ?q= -->

To get a name for a product, send a GET request to the server with the query parameter `q` set to first letter/lettres of the product.

If `q` is not set, a random name will be generated.


```bash
curl http://localhost:5000/?q=tr
```

```bash
StatusCode        : 200
StatusDescription : OK
Content           : {"name":"trollsta"}

RawContent        : HTTP/1.1 200 OK
                    Connection: close
                    Content-Length: 20
                    Content-Type: application/json
                    Date: Thu, 19 Oct 2023 14:17:00 GMT
                    Server: Werkzeug/3.0.0 Python/3.11.0

                    {"name":"trollsta"}

Forms             : {}
Headers           : {[Connection, close], [Content-Length, 20], [Content-Type, application/json], [Date, Thu, 19 Oct 20
                    23 14:17:00 GMT]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 20
```

