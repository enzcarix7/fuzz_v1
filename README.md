# 🕵️‍♂️ Simple Web Fuzzer

This script performs a basic directory and endpoint fuzzing on a target web server using a custom wordlist.

## 🚀 What It Does

- Appends each word from `wordlist.txt` to the target URL.
- Sends an HTTP GET request.
- Logs the URL if the status code is **200 OK**.
- Adds delays to avoid flooding or rate-limiting.

## 🧠 How to Use

1. **Edit the script**:
   Replace the `url` and `wordlist_file` values:

```python
url: str = 'http://your-target.com'
wordlist_file: str = 'wordlist.txt'
```

2.	Run the script:
```
python3 fuzz.py
```

3.	Check the output:
Found endpoints will be printed to the terminal.


### ⚠️ Legal Notice

This tool is for authorized testing only. Do not use it on targets you don’t have permission to test.
Pentest responsibly.
