import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('sum.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('files/sum/', zipf)
    zipf.close()

    zipf = zipfile.ZipFile('alice.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('files/alice/', zipf)
    zipf.close()

""" import os
import zipfile

def zipdir(path, outputfile):
    # ziph is zipfile handle
    zipf = zipfile.ZipFile(outputfile, 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(path):
        for file in files:
            zipf.write(os.path.join(root, file))
    zipf.close()


zipdir('file/sum', 'sum.zip')
zipdir('files/sum/sum', 'alice.zip') """