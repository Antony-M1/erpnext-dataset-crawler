# erpnext-dataset-crawler
ERPNext Web Crawler, Scrapy, Web Crawler


# Prerequisites

* Python3.10+


<details>
  <summary><h3>Local Setup</h3></summary>


### Step 1:

clone the Project Using this command
```
git clone https://github.com/Antony-M1/erpnext-dataset-crawler.git
```
### Step 2:
Create a `virtual Environment` using this command
```
python3.10 -m venv .venv
```
Activate For `Windows`
```
source .venv/Scripts/activate
```
Activate For `Linux`
```
source .venv/bin/activate
```

### Step 3.
Install the `requirements.txt` packages
```
pip install -r requirements.txt
```

### Step 4:
Create a `.env` file in the workspace directory. past this code
```
HUGGINGFACEHUB_API_TOKEN=<YOUR_HUGGING_FACE_API_TOKEN_OR_ACCESS_TOKEN>
```

### Step 5.
Download the chrome driver and put in the project root folder

Here the [download link](https://googlechromelabs.github.io/chrome-for-testing/)

### Step 6.
Start the `crawling` process. here the example `cmd`.

For [`FrappeFramework`](https://frappeframework.com/docs/user/en/introduction)
```
scrapy crawl frappeframework -o temp/frappeframework.jsonl
```
For [`EPRNext Doc`](https://docs.erpnext.com/docs/user/manual/en/introduction)
```
scrapy crawl erpnext_doc -o temp/erpnext_doc.jsonl
```

</details>


<details>
  <summary><h3>Debugger</h3></summary>

Create `.vscode/launch.json` file. this debugger for `VSCode`.

Past this code.

```
    {
    "version": "0.2.0",
    "configurations": [
        {
        "name": "Scrapy",
        "type": "python",
        "request": "launch",
        "module": "scrapy",
        "args": ["runspider", "${file}"],
        "console": "integratedTerminal",
        "justMyCode": false
        }
    ]
    }
```
</details>
