try:
   import Config.BuildConfig.path as Path
except:
   try:
      import path as Path
   except:
      print('Cannot found "path" module, please check it!')
      exit()
Include  = {}
# Include path
Include['bootloader'] = [
   Path.Path['bootloader']['WorkSpace']+'Source\\types\\',
   Path.Path['bootloader']['WorkSpace']+'Source\\math\\sort\\',
   
   ]
Include['application'] = [
   Path.Path['bootloader']['WorkSpace']+'Source\\types\\',
   Path.Path['bootloader']['WorkSpace']+'Source\\math\\sort\\',
   
   ]
# End of Include path
