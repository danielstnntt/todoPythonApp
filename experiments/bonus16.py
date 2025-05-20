import FreeSimpleGUI as gui


labelFile = gui.Text("Select Files to Compress: ")
fileInputBox = gui.Input()
fileButton = gui.FilesBrowse("Choose Files: ")

labelDestination = gui.Text("Select Destination Folder: ")
folderInputBox = gui.Input()
folderButton = gui.FolderBrowse("Choose Folder: ")


compressButton = gui.Button("Compress")

window = gui.Window('File Compressor',
                    layout=[[labelFile], [fileInputBox, fileButton],
                            [labelDestination], [folderInputBox, folderButton],
                            [compressButton]])
window.read()
window.close()
