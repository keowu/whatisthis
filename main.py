import easygui

# LICENSE MIT
# BASE BY @KEOWU
# Be more than free to modify whatever you want, but I left your like in the original repository and if possible leave the credits,
# and of course if it is a very significant change, leave a pull request with it, so that you can be part of the project.

class WhatIsThis(object):

    @staticmethod
    def getBinaryFileSignature(bytes_array):
        TGA_SIGN = ['0X54', '0X52', '0X55', '0X45', '0X56', '0X49', '0X53', '0X49',
                    '0X4F', '0X4E', '0X2D', '0X58', '0X46', '0X49', '0X4C', '0X45',
                    '0X2E', '0X00']
        EXCUTABLE_SIGN = ['0X4D', '0X5A']
        WALLET_SIGN = ['0X0A', '0X16', '0X6F', '0X72', '0X67', '0X2E', '0X62', '0X69', '0X74',
                       '0X63', '0X6F', '0X69', '0X6E', '0X2E', '0X70', '0X72']
        ADSFORMAT = ['0X30', '0X26', '0XB2', '0X75', '0X8E', '0X66', '0XCF', '0X11',
                     '0XA6', '0XD9', '0X00', '0XAA', '0X00', '0X62', '0XCE', '0X6C']
        MP3FORMAT_SIGN = ['0X49', '0X44', '0X33']
        GIF1_SIGN = ['0X47', '0X49', '0X46', '0X38', '0X37', '0X61']
        GIF2_SIGN = ['0X47', '0X49', '0X46', '0X38', '0X39', '0X61']
        JAR_SIGN = ['0X50', '0X4B', '0X3', '0X4']
        MPGE4_SIGN = ['0X66', '0X74', '0X79', '0X70', '0X4D', '0X53', '0X4E', '0X56']
        MPEGISO_SIGN = ['0X66', '0X74', '0X79', '0X70', '0X69', '0X73', '0X6F', '0X6D']
        PDF_SIGN = ['0X25', '0X50', '0X44', '0X46', '0X2D']
        ELF_SIGN = ['0X7F', '0X45', '0X4C', '0X46']
        TELEGRAMDESKTOPFILE_SIGN = ['0X54', '0X44', '0X46', '0X24']
        TELEGRAMDESKTOPFILEENCRYPTED_SIGN = ['0X54', '0X44', '0X45', '0X46']
        SQLITEDB_SIGN = ['0X53', '0X51', '0X4C', '0X69', '0X74', '0X65', '0X20', '0X66',
                         '0X6F', '0X72', '0X6D', '0X61', '0X74', '0X20', '0X33', '0X00']

        # 2 Byte signature Windows Executable
        if (hex(ord(bytes_array[0])).upper()) in EXCUTABLE_SIGN:
            if (hex(ord(bytes_array[1])).upper()) in EXCUTABLE_SIGN:
                return "MZ - Windows Executable"

        # 17 Bytes signature Truevision Targa Graphic file
        if (hex(ord(bytes_array[0])).upper()) in TGA_SIGN:
            if (hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() and
                hex(ord(bytes_array[3])).upper() and
                hex(ord(bytes_array[4])).upper() and hex(ord(bytes_array[5])).upper() and
                hex(ord(bytes_array[6])).upper() and
                hex(ord(bytes_array[7])).upper() and hex(ord(bytes_array[8])).upper() and
                hex(ord(bytes_array[9])).upper() and
                hex(ord(bytes_array[10])).upper() and hex(ord(bytes_array[11])).upper() and
                hex(ord(bytes_array[12])).upper() and
                hex(ord(bytes_array[13])).upper() and hex(ord(bytes_array[14])).upper() and
                hex(ord(bytes_array[15])).upper() and
                hex(ord(bytes_array[16])).upper()) in TGA_SIGN:
                return "TGA - Truevision Targa Graphic file"

        # 16 Bytes signature MultiBit Bitcoin wallet file
        if hex(ord(bytes_array[0])).upper() in WALLET_SIGN:
            if (hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() and hex(
                    ord(bytes_array[3])).upper()
                and hex(ord(bytes_array[4])).upper() and hex(ord(bytes_array[5])).upper() and hex(
                        ord(bytes_array[6])).upper()
                and hex(ord(bytes_array[7])).upper() and hex(ord(bytes_array[8])).upper() and hex(
                        ord(bytes_array[9])).upper()
                and hex(ord(bytes_array[10])).upper() and hex(ord(bytes_array[11])).upper() and hex(
                        ord(bytes_array[12])).upper()
                and hex(ord(bytes_array[13])).upper() and hex(ord(bytes_array[14])).upper() and hex(
                        ord(bytes_array[15])).upper()) in WALLET_SIGN:
                return "MultiBit Bitcoin wallet file"

        # 16 Bytes signature ASF, WMA, WMV - Microsoft Windows Media Audio/Video File (Advanced Systems Format)
        if hex(ord(bytes_array[0])).upper() in ADSFORMAT:
            if (hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() and hex(
                    ord(bytes_array[3])).upper()
                and hex(ord(bytes_array[4])).upper() and hex(ord(bytes_array[5])).upper() and hex(
                        ord(bytes_array[6])).upper()
                and hex(ord(bytes_array[7])).upper() and hex(ord(bytes_array[8])).upper() and hex(
                        ord(bytes_array[9])).upper()
                and hex(ord(bytes_array[10])).upper() and hex(ord(bytes_array[11])).upper() and hex(
                        ord(bytes_array[12])).upper()
                and hex(ord(bytes_array[13])).upper() and hex(ord(bytes_array[14])).upper() and hex(
                        ord(bytes_array[15])).upper()
                and hex(ord(bytes_array[16])).upper()) in WALLET_SIGN:
                return "ASF, WMA, WMV - Microsoft Windows Media Audio/Video File (Advanced Systems Format)"

        # 3 Bytes signature  MP3	MPEG-1 Audio Layer 3 (MP3) audio file
        if (hex(ord(bytes_array[0])).upper()) in MP3FORMAT_SIGN:
            if hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() in MP3FORMAT_SIGN:
                return "MP3	MPEG-1 Audio Layer 3 (MP3) audio file"

        # 6 Bytes GIF Graphics interchange format file - GENETIC SEQUENCE 1
        if (hex(ord(bytes_array[5])).upper()) in GIF1_SIGN:
            if (hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() and hex(
                    ord(bytes_array[3])).upper()
                    and hex(ord(bytes_array[4])).upper() and hex(ord(bytes_array[5])).upper()):
                return "GIF Graphics interchange format file - GENETIC SEQUENCE 1"

        # 6 Bytes GIF Graphics interchange format file - GENETIC SEQUENCE 2
        if (hex(ord(bytes_array[5])).upper()) in GIF2_SIGN:
            if (hex(ord(bytes_array[1])).upper() in GIF2_SIGN and hex(ord(bytes_array[2])).upper() in GIF2_SIGN and hex(
                    ord(bytes_array[3])).upper() in GIF2_SIGN
                    and hex(ord(bytes_array[4])).upper() in GIF2_SIGN and hex(
                        ord(bytes_array[5])).upper() in GIF2_SIGN):
                return "GIF Graphics interchange format file - GENETIC SEQUENCE 2"

        # 4 Bytes ZI PKZIP archive file, APK	ANDROID, JAR - Java archive; compressed file package for classes and data
        # KMZ	 	Google Earth saved working session file
        # KWD	 	KWord document
        # ODT, ODP, OTT, OXPS, SXC, SXD, SXI, SXW, SXC, WMZ, XPI, XPS, XPT
        if (hex(ord(bytes_array[0])).upper()) in JAR_SIGN:
            if (hex(ord(bytes_array[1])).upper() in JAR_SIGN and hex(ord(bytes_array[2])).upper() in JAR_SIGN and
                    hex(ord(bytes_array[3])).upper() in JAR_SIGN):
                concept = """
                    ZIP	 	PKZIP archive file (Ref. 1 | Ref. 2)
                    ZIP	 	Apple Mac OS X Dashboard Widget, Aston Shell theme, Oolite eXpansion Pack,
                    APK	 	Android package
                    JAR	 	Java archive; compressed file package for classes and data
                    KMZ	 	Google Earth saved working session file
                    KWD	 	KWord document
                    ODT, ODP, OTT	 	OpenDocument text document, presentation, and text document template, respectively.
                    OXPS	 	Microsoft Open XML paper specification file
                    SXC, SXD, SXI, SXW	 	OpenOffice spreadsheet (Calc), drawing (Draw), presentation (Impress),
                    and word processing (Writer) files, respectively.
                    SXC	 	StarOffice spreadsheet
                    WMZ	 	Windows Media compressed skin file
                    XPI	 	Mozilla Browser Archive
                    XPS	 	XML paper specification file
                    XPT	 	eXact Packager Models
                    ! These files are usually very easy to unzip and access or reverse engineer, be aware that some may have obfuscation mechanisms.
                    """
                return concept

        # 8 Bytes MPEG-4 video file
        if (hex(ord(bytes_array[0])).upper()) in MPGE4_SIGN:
            if (hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() and
                    hex(ord(bytes_array[3])).upper() and hex(ord(bytes_array[4])).upper() and
                    hex(ord(bytes_array[5])).upper() and hex(ord(bytes_array[6])).upper() and
                    hex(ord(bytes_array[7])).upper() in MPGE4_SIGN):
                return "MPEG-4 video file"

        # 8 Bytes MP4 ISO Base Media file (MPEG-4) v1
        if (hex(ord(bytes_array[0])).upper()) in MPEGISO_SIGN:
            if (hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() and
                    hex(ord(bytes_array[3])).upper() and hex(ord(bytes_array[4])).upper() and
                    hex(ord(bytes_array[5])).upper() and hex(ord(bytes_array[6])).upper() and
                    hex(ord(bytes_array[7])).upper() in MPEGISO_SIGN):
                return "MP4 ISO Base Media file (MPEG-4) v1"

        # 5 Bytes PDF document
        if (hex(ord(bytes_array[0])).upper()) in PDF_SIGN:
            if (hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() and
                    hex(ord(bytes_array[3])).upper() and hex(ord(bytes_array[4])).upper() in PDF_SIGN):
                return "PDF document"

        # 4 Bytes Executable and Linkable Format
        if (hex(ord(bytes_array[0])).upper()) in ELF_SIGN:
            if (hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() and
                    hex(ord(bytes_array[3])).upper() in ELF_SIGN):
                return "Executable and Linkable Format"

        # 4 Bytes Telegram Desktop File
        if (hex(ord(bytes_array[0])).upper()) in TELEGRAMDESKTOPFILE_SIGN:
            if (hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() and
                    hex(ord(bytes_array[3])).upper() in TELEGRAMDESKTOPFILE_SIGN):
                return "Telegram Desktop File"

        # 4 Bytes Telegram Desktop Encrypted File
        if (hex(ord(bytes_array[0])).upper()) in TELEGRAMDESKTOPFILEENCRYPTED_SIGN:
            if (hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() and
                    hex(ord(bytes_array[3])).upper() in TELEGRAMDESKTOPFILEENCRYPTED_SIGN):
                return "Telegram Desktop Encrypted File"

        # 16 Bytes SQLite Database
        if (hex(ord(bytes_array[0])).upper()) in SQLITEDB_SIGN:
            if (hex(ord(bytes_array[1])).upper() and hex(ord(bytes_array[2])).upper() and
                    hex(ord(bytes_array[3])).upper() and hex(ord(bytes_array[4])).upper() and hex(
                        ord(bytes_array[5])).upper()
                    and hex(ord(bytes_array[6])).upper() and hex(ord(bytes_array[7])).upper() and hex(
                        ord(bytes_array[8])).upper()
                    and hex(ord(bytes_array[9])).upper() and hex(ord(bytes_array[10])).upper() and hex(
                        ord(bytes_array[11])).upper()
                    and hex(ord(bytes_array[12])).upper() and hex(ord(bytes_array[13])).upper() and hex(
                        ord(bytes_array[14])).upper() and
                    hex(ord(bytes_array[15])).upper() in SQLITEDB_SIGN):
                return "SQLite Database"

    @staticmethod
    def binaryload(filepath):
        global file, filelines
        try:
            with open(filepath, "rb") as file:
                file.readlines()
                filelines = file.tell()
                file.close()

            with open(filepath, "rb") as file:
                bytes = file.read(1)
                bytes = bytes.decode(errors='ignore')
                i = 0
                bytes_array = []
                print("Reading the binary, Please Wait a little bit....")
                print(
                    "This takes a while and depends on your computer, more will happen sooner or later, wait.")
                while i <= int(filelines):
                    bytes_array.append(bytes)
                    bytes = file.read(1)
                    bytes = bytes.decode(errors='ignore')
                    i += 1
        finally:
            file.close()

        try:
            filepath = easygui.filesavebox(default='WHATISANALISE.wtf')
            with open(filepath, "w") as write:
                write.write(
                    "______________________________________BINARY HEADER______________________________________ \n")
                write.write("Este arquivo tem a assinatura para: %s \n " % WhatIsThis().getBinaryFileSignature(bytes_array))
                write.write(
                    "_________________________________________________________________________________________ \n")
                write.write(
                    "______________________________________BINARY STRINGS_____________________________________ \n")
                for byte in bytes_array:
                    write.write("%s \n" % byte)
                write.write(
                    "_________________________________________________________________________________________ \n")
        finally:
            write.close()

        print(WhatIsThis().getBinaryFileSignature(bytes_array))

    @staticmethod
    def loadfile():
        filepath = easygui.fileopenbox(msg="Join any file")
        WhatIsThis().binaryload(filepath)


# main :D
if __name__ == "__main__":
    WhatIsThis().loadfile()
