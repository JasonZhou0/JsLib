# -*- coding: utf-8 -*-
# str = '{0:*>9}'
# str = str.format('ADWA')
# print(str)
import os
import sys
import re
import xlrd
import string

NowSheetName = ''
NowSubscript = 0

def SetNowSubscript(Subscript):
   global NowSubscript
   NowSubscript = Subscript
def GetNowSubscript():
   return NowSubscript
   
def SetNowSheetName(name):
   global NowSheetName
   NowSheetName = name
def GetNowSheetName():
   return NowSheetName

def read_excel():

   #文件位置

   ExcelFile=xlrd.open_workbook(r'D:\MyProject\MyProject\CM01\Source\Extend\Driver\gpio\Template\gpio_config.xlsx')

   #获取目标EXCEL文件sheet名

   print(ExcelFile.sheet_names())

   #------------------------------------

   #若有多个sheet，则需要指定读取目标sheet例如读取sheet2

   # sheet2_name=ExcelFile.sheet_names()[1]

   #------------------------------------

   #获取sheet内容【1.根据sheet索引2.根据sheet名称】

   #sheet=ExcelFile.sheet_by_index(1)

   sheet=ExcelFile.sheet_by_name('function')

   #打印sheet的名称，行数，列数

   print(sheet.name,sheet.nrows,sheet.ncols)

   #获取整行或者整列的值

   rows1=sheet.row_values(0)#第一行内容
   rows2=sheet.row_values(1)#第二行内容
   cols=sheet.col_values(1)#第二列内容

   print(rows1,rows2,cols)

   #获取单元格内容
   # sheet.cell(1,0) = "DWA"
   print(sheet.cell(1,0).value.encode('utf-8'))

   print(sheet.cell_value(1,0).encode('utf-8'))

   print(sheet.row(1)[0].value.encode('utf-8'))

   #打印单元格内容格式

   print(sheet.cell(1,0).ctype)

# records is a list
def LoadTemplate(path,records,encoding):
   try:
     file = open(path, "r", encoding=encoding)  # open file in read mode
   except IOError as message:                   # file open failed
     print("read file error({0}:{1})".format(message, path))
     exit()
   lines = file.readlines()
   for line in lines:
     records.append(line)
   file.close()

class GetExcelConfig(object):
   def __init__(self,path):
      ExcelFile = xlrd.open_workbook(path)
      self.SheetNames= ExcelFile.sheet_names()
      self.ExcelDict = {}
      for sheet_name in self.SheetNames:
         self.ExcelDict[sheet_name] = {}
         sheet = ExcelFile.sheet_by_name(sheet_name)
         if(sheet.ncols > 0):
            parameter_list = sheet.row_values(0)
            for i, parameter in enumerate(parameter_list):
               self.ExcelDict[sheet_name][parameter] = sheet.col_values(i)[1:]
      ExcelFile.release_resources()
      del ExcelFile
   def PrintAll(self):
      print('self.ExcelDict = ',self.ExcelDict)


def GreatSourceFile(path,records,excel,encoding):
   try:
      file = open(path, "w", encoding=encoding)  # open file in read mode
   except IOError as message:                   # file open failed
      print("read file error({0}:{1})".format(message, path))
      exit()

   process     = 'normal' # normal/script
   dict        = {}
   dict_count  = 0
   CodeBlock   = ''
   
   def GetFill(count):
      fill = ''
      stair = count
      if stair > 0:
         stair = stair*3
         while(stair > 0):
            fill = '%s '%fill
            stair-=1
      return fill
   def HandleLineTemplate(line, excel):
      writeLine    = line
      replaceLists = re.findall(r"\$\{(.+?)\}",writeLine)
      if(len(replaceLists) > 0):
         for parameterList in replaceLists:
            temp = string.Template(writeLine)
            run  = "temp.safe_substitute(%s='%s')"%(parameterList, excel.ExcelDict[GetNowSheetName()][parameterList][GetNowSubscript()])
            writeLine = eval(run)
      return writeLine
   for line in records:
      writeLine = HandleLineTemplate(line, excel)
      if process == 'normal':
         #writeLine = HandleLineTemplate(line, excel)
         if '% ' == writeLine[:2]:# when writeLine start is '% ', it is mean: this is a script.
            if ' if ' in writeLine[:5]:
               dict[dict_count]  = 'if'
               dict_count+=1
               CodeBlock         = writeLine[2:]
               process           = 'script'
            elif ' for ' in writeLine[:6]:
               dict[dict_count]  = 'for'
               dict_count+=1
               CodeBlock         = writeLine[2:]
               process           = 'script'
            elif ' while ' in writeLine[:8]:
               dict[dict_count]  = 'while'
               dict_count+=1
               CodeBlock         = writeLine[2:]
               process           = 'script'
            else:
               exec(writeLine[2:])
         else:
            file.writelines(writeLine)
      elif process == 'script':
         if '% ' == writeLine[:2]:# when writeLine start is '% ', it is mean: this is a script.
            if ' if ' in writeLine[:5]:
               dict[dict_count]  = 'if'
               dict_count+=1
               CodeBlock         = '%s%s'%(CodeBlock, writeLine[2:])
            elif ' for ' in writeLine[:6]:
               dict[dict_count]  = 'for'
               dict_count+=1
               CodeBlock         = '%s%s'%(CodeBlock, writeLine[2:])
            elif ' while ' in writeLine[:8]:
               dict[dict_count]  = 'while'
               dict_count+=1
               CodeBlock         = '%s%s'%(CodeBlock, writeLine[2:])
            else:
               CodeBlock         = '%s%s'%(CodeBlock, writeLine[2:])
         elif '%end of ' in writeLine:
            str = '%%end of %s'%dict[dict_count-1]
            if str == writeLine[:-1]:
               dict_count-=1
               if dict_count == 0:
                  exec(CodeBlock)
                  process = 'normal'
            else:
               CodeBlock   = '%s%sfile.writelines(HandleLineTemplate(\'%s\', excel)+\'\\n\')\n'%(CodeBlock, GetFill(dict_count), line[:-1])
         else:
            CodeBlock   = '%s%sfile.writelines(HandleLineTemplate(\'%s\', excel)+\'\\n\')\n'%(CodeBlock, GetFill(dict_count), line[:-1])
         pass
      else:
         print('process\'s value is fault')
   if dict_count != 0:
      file.close()
      print('Error: Template syntax error')
      exit(1)
   file.close()

def AutomaticCode(pyconfig, moduleName):
   print('Start: Automatic programming code for [%s]'%moduleName)
   exec('import %s'%pyconfig)
   TemplateFile = []
   Project_gpio_config = GetExcelConfig(eval("%s.Config['config']"%pyconfig))
   LoadTemplate(eval("%s.Config['template']"%pyconfig), TemplateFile,'utf-8')
   GreatSourceFile(eval("%s.Config['target']"%pyconfig), TemplateFile,Project_gpio_config,'utf-8')
   print('Completed: Automatic programming code for [%s]'%moduleName)

if __name__ == '__main__':
   # gpio
   sys.path.append(r'%s\\Source\\Extend\\Driver\\gpio\\Template\\'%os.getcwd()) # add config file path to system path
   AutomaticCode('gpio_config', 'gpio')
   # end of gpio