# erpnext-dataset-crawler
ERPNext Web Crawler, Scrapy, Web Crawler


# Prerequisites

* Python3.10+

# Debugger

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