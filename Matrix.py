#!/usr/bin/python
import wx
import re
import numpy as np


def Quit(evt):
    dialog = wx.MessageDialog(Dialog1, 'Are you sure you want to exit?', 'End of work', style=wx.OK | wx.CANCEL)
    x = dialog.ShowModal()
    dialog.Destroy()
    if x == wx.ID_OK:
        Dialog1.Close()

def ReadMatrix(evt):
    dialog = wx.FileDialog(Dialog1, message='Select Substitution Matrix', defaultFile='', style=wx.FD_OPEN,pos=(10, 10))
    picked_file=''
    if dialog.ShowModal() == wx.ID_OK:
        file_name = dialog.GetPaths()
        picked_file = open(file_name[0], "r+")
        lines = picked_file.readlines()
        picked_file.close()
        b = ';'
        i = 0
        k = len(lines)
        for x in range(len(lines)):
            if lines[x][0] == '#':
                lines[x] = ''
        while i <= k - 1:
            if lines[i] == '':
                del lines[i]
            else:
                break
        if lines[0][0] != ';':
            b = lines[0][0]
        temp = []
        matrix = []
        digits = list(range(-99, 100))
        for i in range(0, len(digits)):
            digits[i] = str(digits[i])
        for i in range(0, len(lines)):
            for a in range(0, len(lines[i])):
                if ((lines[i][a] in digits) and (lines[i][a + 1] in digits)):
                    temp.append(lines[i][a] + lines[i][a + 1])
                if lines[i][a] != b:
                    if not ((lines[i][a] in digits) and (lines[i][a + 1] in digits)):
                        if not ((lines[i][a] in digits) and (lines[i][a - 1] in digits)):
                            temp.append(lines[i][a])
            matrix.append(temp)
            temp = []
        for i in matrix:
            for a in range(0, len(i) - 1):
                if i[a] == '-':
                        i[a + 1] = '-' + i[a + 1]
        n = 0
        for i in matrix:
            for a in i:
                if a == '-':
                    matrix[n].remove('-')
                if a == '\n':
                    matrix[n].remove('\n')
            n += 1
        if len(matrix[0]) > 5:
              a = 1
              while (a >= 1 and a <= 20):
                    for i in matrix[a]:
                        dl = len(matrix[a])
                        ile = 22 - dl
                        if ile > 0:
                            for t in range(1, ile):
                                 matrix[a].insert(t, ' ')
                    a += 1
        matrix[0].insert(0, ' ')
        n= 0
        m = 0
        for i in matrix:
            for a in i:
                if a == ' ' and n > 0:
                     matrix[n][m] = matrix[m][n]
                m += 1
            m = 0
            n += 1
        for i in range(0, len(matrix[0])):
            for a in range(0, len(matrix[0])):
                if matrix[i][a] in digits:
                    matrix[i][a] = int(matrix[i][a])
        tbl=matrix[0]
        tbl.remove(' ')
        del matrix[0]
        for i in range(0, len(matrix[0]) - 1):
            del matrix[i][0]
        matrixnumpy = np.array(matrix)
        if 'E' or 'F' or 'G' in tbl:
            print('Aminoacids in order:',tbl)
        else:
            print('Nucleotides in order:',tbl)
        print(matrixnumpy)
        loop = False
        while loop == False:
            x = input("Matrix: ")
            if len(x) == 2 and (x[0] and x[1] in tbl):
                a = x[0]
                b = x[1]
                number_1 = tbl.index(a)
                number_2 = tbl.index(b)
                matrix_to_print = matrixnumpy[number_1][number_2]
                print(matrix_to_print)
            elif x == 'q' or x=='quit' or x=='exit' or x=='Quit' or x=='Quit':
                loop=True
            else:
                print("Error, please write two nucleotides or two amino acids, example: AA")
        return matrixnumpy,tbl
    dialog.destroy()
prog = wx.App()
Dialog1 = wx.Frame(None, title='Menu', size=(875, 500))
Menu_Bar = wx.MenuBar()
prog_Menu = wx.Menu()
prog_MenuItemA3 = prog_Menu.Append(wx.ID_ANY, 'Read Matrix', 'Read Data')
Dialog1.Bind(wx.EVT_MENU,ReadMatrix,prog_MenuItemA3)
Menu_Bar.Append(prog_Menu, 'Data')
prog_Menu = wx.Menu()
prog_MenuItemC1 = prog_Menu.Append(wx.ID_EXIT, 'Exit', 'Exit')
Menu_Bar.Append(prog_Menu, 'Exit')
Dialog1.Bind(wx.EVT_MENU, Quit, prog_MenuItemC1)
Dialog1.SetMenuBar(Menu_Bar)
prog_panel = wx.Panel(parent=Dialog1, size=(875, 500))
Dialog1.Center()
Dialog1.Show()
prog.MainLoop()
