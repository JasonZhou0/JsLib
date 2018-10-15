import os

Path={}

if __name__ == '__main__':
   WorkSpace = os.path.abspath('..\\..')+'\\'
else:
   WorkSpace = os.getcwd()+'\\'
   
Path['bootloader'] = {
   'WorkSpace'       :WorkSpace,
   'BuildRelativePath':'Build\\bootloader\\',
   'BuildPath'       :WorkSpace+'Build\\bootloader\\',
   'BinPath'         :WorkSpace+'Build\\bootloader\\bin\\',
   'Target'          :WorkSpace+'Build\\bootloader\\bin\\bootloader',
   'TargetName'      :'bootloader',
   'LinkerFile'      :WorkSpace+'Config\\LinkerFile\\STM32F407VETx_FLASH_BOOT.ld',
   'ObjPath'         :WorkSpace+'Build\\bootloader\\obj\\',
   'SourcePath'      :{
      'MCULibraryPath'  :WorkSpace+'Source\\',
      }
   }

Path['application'] = {
   'WorkSpace'       :WorkSpace,
   'BuildRelativePath':'Build\\application\\',
   'BuildPath'       :WorkSpace+'Build\\application\\',
   'BinPath'         :WorkSpace+'Build\\application\\bin\\',
   'Target'          :WorkSpace+'Build\\application\\bin\\application',
   'TargetName'      :'application',
   'LinkerFile'      :WorkSpace+'Config\\LinkerFile\\STM32F407VETx_FLASH_APP.ld',
   'ObjPath'         :WorkSpace+'Build\\application\\obj\\',
   'SourcePath'      :{
      'MCULibraryPath'  :WorkSpace+'Source\\',
      }
   }

if __name__ == '__main__':
   import os
   print(Path)
   os.system('pause')

