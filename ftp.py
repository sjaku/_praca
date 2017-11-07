<<<<<<< HEAD
__author__ = 'sjaku'

from ftplib import FTP
import os, sys, ssl

host = "pcredit.ayz.pl"
user = "pcredit"
password = "OE06jiai0"

File2Send = "C:\\Users\\sjaku\\Desktop\\linuxpl\\"
MacOSx2Send = "//Users//szymon//Downloads//[Dla_sklepu]//banery//"
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
=======
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
>>>>>>> 14519f1742b58de18bb17400b51db0a0a96511d8
