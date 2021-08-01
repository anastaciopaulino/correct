import os

class Correct:

    def __init__(self):
        self.listFiles = []
    
    def correctFlesh(self):
        for file in self.listFiles:
            openFile = open(str(file), 'r+')
            newFile = open(str(file) + '.srt', 'w')

            for line in openFile.readlines():
                line = line.replace('->', '-->')
                line = line.replace('00: ', '00:')
                newFile.write(line)
        
        print('Foram alterado %d arquivo/s' %(len(self.listFiles)))
    
    def removeFile(self):
        for file in self.listFiles:
            if not('srt' in file):
                os.remove(file)
        
        print('Foram removido %d arquivo/s' %(len(self.listFiles)))
    
    def removeExtesion(self, extesion):
        for file in self.listFiles:
            if(str(extesion) in file):
                os.rename(file, file[:-4])
        
        print('Foram renomeado %d arquivo/s' %(len(self.listFiles)))
            

    def listerFile(self, path):
        files = os.listdir(path)

        if('rename.py' in files):
            files.remove('rename.py')


        for file in files:
            pathDir = os.path.join(path, file)

            if(os.path.isdir(pathDir)):
                self.listerFile(pathDir)
            
            if(os.path.isfile(pathDir)):
                self.listFiles.append(pathDir)
        

test = Correct()
test.listerFile('.')
test.correctFlesh()
test.removeFile()