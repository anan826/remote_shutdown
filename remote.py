# 開機通知
import smtplib
import email.message
from datetime import datetime
import socket
# 中途等待
import time as tm
# 遙控關機
import imaplib
import email
import subprocess


# 讀取檔案
with open(r"此處替換成該讀取檔案的絕對路徑")as file:
    account = file.readlines()[0]
with open(r"此處替換成該讀取檔案的絕對路徑")as file:
    password = file.readlines()[1]
    file.close()
# 現在時間
time = datetime.now()
currentTime = time.strftime("%H:%M:%S")
# 取得IP位址
IPAdress = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
IPAdress.connect(("8.8.8.8", 80))
ip = IPAdress.getsockname()[0]
# 信件內容
content = email.message.EmailMessage()
content["From"] = "此處替換成電子信箱"
content["To"] = "此處替換成電子信箱"
content["Subject"] = "Personal Computer Boot Record Report - 開機紀錄"
content.set_content(
    "開機通知:此郵件從該IP:{0}位址發送，你的電腦已在 {1} 開機。".format(ip, currentTime))
# 連線Gmail
mail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
mail.login(account, password)
mail.send_message(content)
mail.close()


# time sleep

tm.sleep(60)  # 可以替換成想要的等待時間

# Gmail 登入資訊

# 搜尋條件
searchSubject = 'shutdown'

# 關機命令
shutDownCommand = 'shutdown /s /t 1'

# 連線到 Gmail 伺服器
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(account, password)
mail.select('inbox')
mail.literal = searchSubject.encode('utf-8')
typ, data = mail.search(None, 'SUBJECT')

# 搜尋郵件
typ, data = mail.search(None, f'SUBJECT "{searchSubject}"')

# 取得郵件 ID
mail_ids = data[0]
id_list = mail_ids.split()

# 讀取郵件內容
for i in id_list:
    typ, data = mail.fetch(i, '(RFC822)')
    for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject = msg['subject']
            print('Subject:', subject)
            if subject == searchSubject:
                subprocess.call(shutDownCommand.split())
                print("   OFF   ON  ")
                print("         __")
                print("       / ^ /")
                print("      /   /")
                print("     /   /")
                print("    /   /")
                print("   /   /")
                print("  /__ /  ")
                print("             ")
                print("Shutting down computer...")
                print(".             ")
                print(".             ")
                print(".             ")
                print(".             ")
                print(".             ")
                print(".             ")
                print(".             ")
                print("   OFF   ON  ")
                print("      __      ")
                print("     \\^ \\")
                print("      \\  \\")
                print("       \\  \\")
                print("        \\  \\")
                print("         \\  \\")
                print("          \\__\\")
                mail.store(i, '+FLAGS', '\\Deleted')
                mail.expunge()

# 登出 Gmail
mail.close()
mail.logout()
