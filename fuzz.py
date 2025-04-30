from requests import get, Response


def fuzz(url: str):

    interesting_word: list[str]=[
        'admin',
        'user',
        'password',
        'root',
        'api',
        'db',
        'ftp',
        'login',
        'account',
        'logout',
        'reset',
        'change',
        'delete',
        'edit',
        'view',
        'upload',
        'download',
        'backup',
        'restore',
        'update',
        'upgrade',
        'install',
        'uninstall',
        'remove',
        'enable',
        'disable',
        'start',
        'stop',
        'restart',
        'backup',
        'restore',
        'monitor',
        'report',
        'logs',
        'debug',
        'error',
        'warning',
        'critical',
        'notice',
        'info',
        'success',
        'fail',
    ]
    for word in interesting_word:
        fuzzed_url: str = f"http://{url}/{word}"
        try:
            res: Response = get(fuzzed_url)
            if res.status_code != 404:
                print(f'Word found: {word} - URL: {fuzzed_url} - Status Code: {res.status_code} - Content Length: {len(res.text)}')
        except Exception as e:
            print(f'Error fuzzing {fuzzed_url}: {str(e)}')

target: str = 'example.com'
fuzz(target)
