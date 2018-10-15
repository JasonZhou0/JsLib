try:
   import Config.BuildConfig.path as Path
except:
   try:
      import path as Path
   except:
      print('Cannot found "path" module, please check it!')
      exit(main())
# lib file paths
Library     = {}
LibraryPath = {}

Library['bootloader'] = [
   ]
LibraryPath['bootloader'] = [
   Path.Path['bootloader']['WorkSpace']+'Tools\\mingw64\\lib\\gcc\\x86_64-w64-mingw32\\lib\\',
   ]

Library['application'] = [
   ]
LibraryPath['application'] = [
   Path.Path['bootloader']['WorkSpace']+'Tools\\mingw64\\lib\\gcc\\x86_64-w64-mingw32\\lib\\',
   ]