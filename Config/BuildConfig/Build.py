import os
import sys
import time
import getpass

type = sys.version_info.major

MainMenu = {}
MainMenu[0] = {
   'Build bootloader'   :['call build -Q =boot '],
   'Build application'  :['call build -Q =app '],
   'Rebuild bootloader' :['call build -Q =boot =delete '],
   'Rebuild application':['call build -Q =app =delete '],
   'Rebuild all'        :['call build -Q =boot =delete ', 'call build -Q =app =delete '],
   'Clean bootloader'   :['call build -c -Q =boot =delete '],
   'Clean application'  :['call build -c -Q =app =delete '],
   'Clean all'          :['call build -c -Q =boot =delete ', 'call build -c -Q =app =delete '],
   'ELF->TXT(need tasking licence!)' :['call build -Q =boot =elf ', 'call build -Q =app =elf '],
   'Start automatic code' :['call Tools\\Python\\Python37-32\\python.exe Config\\BuildConfig\\automatic.py'],
   }

def str_len(str): 
   try: 
      row_l=len(str) 
      utf8_l=len(str.encode('utf-8')) 
      return (utf8_l-row_l)/2+row_l
   except:
      return 0

while(1):
   print('')
   print('##########################################################')
   print('##                                                      ##')
   UserName       = 'Hello ['+getpass.getuser()+']'
   LineLen        = str_len('                                                      ')
   UserNameLen    = str_len(UserName)
   SpaceLen       = LineLen-UserNameLen
   LeftSpaceLen   = SpaceLen/2
   RightSpaceLen  = SpaceLen - LeftSpaceLen
   if(LeftSpaceLen < 0 or RightSpaceLen < 0):
      print("##                Your name is too long!                ##")
   else:
      LeftFill       = ''
      RightFill      = ''
      while(LeftSpaceLen):
         LeftFill += ' '
         LeftSpaceLen-=1
      while(RightSpaceLen):
         RightFill += ' '
         RightSpaceLen-=1
      print ('##'+LeftFill+UserName+RightFill+'##')
   print('##',end='',flush=True)
   Data = '>>> Welcome to Easy Construct! <<<'
   Start = 0
   End   = 8
   fill  = ' '
   while(1):
      delay = 0.01
      DataLen = str_len(Data)
      Offset= Start
      print('%s%s'%(fill,Data),end='',flush=True)
      if(End<Start):
         break
      while(DataLen):
         print('\b',end='',flush=True)
         DataLen-=1
      time.sleep(delay)
      Start+=1
   print('          ##')
   print('##                                                      ##')
   print('##',end='',flush=True)
   Data = '--- Jason Zhou '
   Start = 80
   End   = 38
   fill  = ''
   DataLen = str_len(Data)
   while(Start):
      print(' ',end='',flush=True)
      Start-=1
   Start = 80
   while(1):
      delay = 0.01
      DataLen = str_len(Data)
      Offset= Start
      print('%s%s'%(fill,Data),end='',flush=True)
      if(Start<End):
         break
      while(DataLen+1):
         print('\b',end='',flush=True)
         DataLen-=1
      time.sleep(delay)
      Start-=1
   print('  ##')
   print('##########################################################\n')
   MenuDepth  = 0
   MenuNumMax = {
      '0':0,
      '1':0,
      }
   CallMenu = {}
   for menu_user in MainMenu[MenuDepth].keys():
      CallMenu[MenuNumMax['%d'%MenuDepth]] = MainMenu[MenuDepth][menu_user]
      if type == 2:
         print  [MenuNumMax['%d'%MenuDepth]], menu_user
      elif type == 3:
         print(' [%d].'%MenuNumMax['%d'%MenuDepth], '%s'%menu_user)
      MenuNumMax['%d'%MenuDepth] += 1
   InputKey = input('\nPlease enter your option number: ')
   try:
      InputKey = int(InputKey)
   except:
      if (InputKey == 'exit'):
         break
      print('Error: Please enter a pure number or "exit" to close this window!')
      # os.system('pause')
      continue
   else:
      if InputKey < MenuNumMax['%d'%MenuDepth]:
         print('You are really smart! The world is wonderful because of you!')
         for cmd in CallMenu[InputKey]:
            os.system(cmd)
      else:
         print('Error: Your input number put of range!')
      # os.system('pause')