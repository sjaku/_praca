__author__ = 'sjaku'

from ftplib import FTP
import os, sys, ssl

host = "pcredit.ayz.pl"
user = "pcredit"
password = "OE06jiai0"

File2Send = "C:\\Users\\sjaku\\Desktop\\linuxpl\\"
FTP_Server = "//domains//kreatywneklocki.pl//public_html//img//lego2"


ftp = FTP(host)
ftp.login(user, password)
ftp.cwd(FTP_Server)




def placeFile():

    filename = File2Send + "stare_konto.PNG"
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

placeFile()
#https://stackoverflow.com/questions/17438096/ftp-upload-files-python
