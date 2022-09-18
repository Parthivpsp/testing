import os

fldrPath = r'C:\Users\parth\OneDrive\Documents\Python\test'


def changeFileNames():
    filenames = []
    for (dirpath, dirnames, filenames) in os.walk(r'C:\Users\parth\OneDrive\Documents\Python\test'):
        break

    for i, f in enumerate(filenames, start=1):
        oldNm = f
        newNm = 'newName_' + str(i)
        # os.rename(fldrPath + r'\\' + oldNm, fldrPath + r'\\' + newNm)
        oldpath = os.path.join(fldrPath, oldNm)
        newpath = os.path.join(fldrPath, newNm)

        os.rename(oldpath, newpath)
        text_file = open(newpath, "w")
        text_file.write("Purchase Amount\n")
        text_file.write("Parthiv")
        text_file.close()


if __name__ == "__main__":
    changeFileNames()

