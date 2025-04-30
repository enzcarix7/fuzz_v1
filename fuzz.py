from requests import get, Response
from time import sleep

def fuzz(url: str, wordlist_file: str) -> None:
    counter = 0
    with open(wordlist_file, 'r', errors='ignore') as wordlist:
        for word in wordlist:
            word: str = word.strip()
            if not word:
                continue
            new_url: str = f'{url}/{word}'
            try:
                response: Response = get(new_url)
                if response.status_code == 200:
                    print(f'[+] Fuzzed URL: {new_url} - Status: {response.status_code}')
            except Exception as e:
                print(f'[-] Error fuzzing {new_url}: {str(e)}')
                continue

            counter += 1
            sleep(1)
            if counter % 100 == 0:
                print(f'[!] Fuzzed {counter} URLs - Pausing for 5 seconds...')
                sleep(5)
                print('[*] Resuming fuzzing...')

url: str = 'http://x.x.x.x' # Replace with your target URL (https://example.com or http://example.com)
wordlist_file: str = r'wordlists/path'
fuzz(url, wordlist_file)
