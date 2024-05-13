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
