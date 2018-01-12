from ftplib import FTP
import os


host = "pcredit.ayz.pl"
user = "pcredit"
password = "OE06jiai"

File2Send = "C:\\Users\\sjaku\\Desktop\\linuxpl\\"
MacOSx2Send = "//Users//szymon//Downloads//[Dla_sklepu]//banery//slider_baner//"
FTP_Server = "//domains//kreatywneklocki.pl//public_html//img//lego//"


ftp = FTP(host)
ftp.login(user, password)
ftp.cwd(FTP_Server)


dirList = os.listdir(MacOSx2Send)



def deleteFileFromFTP():

    for f in dirList:

        #print FTP_Server + f
        ftp.delete(FTP_Server + f)
        print "FTP file deleted: " + FTP_Server + f
        print "-" * 70

def createDirectory():
    dir = "lego"
    ftp.mkd(dir)
    print "FTP directory created: " + dir

def deleteDirectoryFromFTP():

    ftp.rmd(FTP_Server)
    print "FTP directory deleted: " + FTP_Server
    print "-" * 70


def uploadFile():

    for f in dirList:
        file = open(MacOSx2Send + f, "rb")
        a = "STOR " + f
        ftp.storbinary(a, file)

        file.close()


deleteDirectoryFromFTP()

ftp.quit()
