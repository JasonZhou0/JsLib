try:
   import Config.BuildConfig.path as Path
except:
   try:
      import path as Path
   except:
      print('Cannot found "path" module, please check it!')
      exit(main())
# gnu arm toolchain must be already in system path

BuildMode      = 'debug'
CompilerTool   = 'gcc'
Compiler       = {}
CompileToolBacePath  = 'Tools\\mingw64\\bin\\'
# bootloader
Compiler['bootloader']={
   'ARCH'      :'x86', ## x86, arm
   # 'CPU'       :'cortex-m4',
   
   'AR'        :CompileToolBacePath+'ar',
   'AS'        :CompileToolBacePath+'as',
   'CC'        :CompileToolBacePath+'gcc',
   'CXX'       :CompileToolBacePath+'g++',
   'LINK'      :CompileToolBacePath+'gcc',
   'SIZE'      :CompileToolBacePath+'size',
   'RANLIB'    :CompileToolBacePath+'ranlib',
   'OBJDUMP'   :CompileToolBacePath+'objdump',
   'OBJCOPY'   :CompileToolBacePath+'objcopy',
   'PROGSUFFIX':'.exe',
   }
DEVICE = ' -fsigned-char -std=gnu11 -fmessage-length=0'
Compiler['bootloader']['CCFLAGS']   = DEVICE + ' -ffunction-sections -fdata-sections -Wfatal-errors -Wall -Wextra'
# Compiler['bootloader']['ASFLAGS'] = ' -c' + BOOT_DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '
Compiler['bootloader']['LINKFLAGS'] = DEVICE + ' -flto -Wl,--gc-sections,-Map=%s.map'%(Path.Path['bootloader']['Target'])
if BuildMode == 'debug':
   Compiler['bootloader']['CCFLAGS'] += ' -g -O0'# -gdwarf-2'
   # Compiler['bootloader']['ASFLAGS'].Append = ' -g -gdwarf-2'
else:
   Compiler['bootloader']['CCFLAGS'] += ' -O2'

# application
Compiler['application']={
   'ARCH'      :'x86',
   # 'CPU'       :'cortex-m4',
   
   'AR'        :CompileToolBacePath+'ar',
   'AS'        :CompileToolBacePath+'as',
   'CC'        :CompileToolBacePath+'gcc',
   'CXX'       :CompileToolBacePath+'g++',
   'LINK'      :CompileToolBacePath+'gcc',
   'SIZE'      :CompileToolBacePath+'size',
   'RANLIB'    :CompileToolBacePath+'ranlib',
   'OBJDUMP'   :CompileToolBacePath+'objdump',
   'OBJCOPY'   :CompileToolBacePath+'objcopy',
   'PROGSUFFIX':'.exe',
   }
DEVICE = ' -fsigned-char -std=gnu11 -fmessage-length=0'
Compiler['application']['CCFLAGS']   = DEVICE + ' -ffunction-sections -fdata-sections -Wfatal-errors -Wall -Wextra'
# Compiler['application']['ASFLAGS'] = ' -c' + BOOT_DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '
Compiler['application']['LINKFLAGS'] = DEVICE + ' -flto -Wl,--gc-sections,-Map=%s.map'%(Path.Path['application']['Target'])
if BuildMode == 'debug':
   Compiler['application']['CCFLAGS'] += ' -g -O0'# -gdwarf-2'
   # Compiler['application']['ASFLAGS'].Append = ' -g -gdwarf-2'
else:
   Compiler['application']['CCFLAGS'] += ' -O2'

if __name__ == '__main__':
   import os
   print(Compiler)
   os.system('pause')

