import os
import sys

# sys.path.append(r'%s\\Config\\BuildConfig\\'%os.getcwd()) # add config file path to system path

base_env  = Environment(ENV = os.environ)
   
class ConstructTarget(object):
   def __init__(self,name,env,arg):
      self.name = name
      self.env  = env
      self.arg  = arg
   def GetConfig(self):
      import Config.BuildConfig.compiler  as Compiler
      import Config.BuildConfig.include   as Include
      import Config.BuildConfig.define    as Define
      import Config.BuildConfig.library   as Lib
      import Config.BuildConfig.path   	as Path
      env = self.env
      env['CCCOMSTR']   = "Compiling $TARGET"
      env['LINKCOMSTR'] = "Linking $TARGET"
      # tool chain
      for name in Compiler.Compiler[self.name].keys():
         env[name] = Compiler.Compiler[self.name][name]
      # files path
      for name in Path.Path[self.name].keys():
         env[name] = Path.Path[self.name][name]
      # define
      env['CPPDEFINES'] = Define.Define[self.name]
      # include
      env['CPPPATH']    = Include.Include[self.name]
      # lib files
      env['LIB']         = Lib.Library[self.name]
      # lib file paths
      env['LIBPATH']     = Lib.LibraryPath[self.name]

      if '=delete' in self.arg or '=Delete' in self.arg:
         print('Start delete %s floder...'%env['BuildRelativePath'])
         import shutil
         # delete folder "Build\\%s"%self.name and all files
         if os.path.exists('%s'%env['BuildRelativePath']):
            shutil.rmtree('%s'%env['BuildRelativePath'])
         print('Complete delete %s floder.'%env['BuildRelativePath'])
      print('Start build %s...'%env['TargetName'])

      Export('env')
   def CallAutomaticScript(self):
      import Config.BuildConfig.automatic as Automatic
      Automatic.AutomaticCode()
   def PrintAll(self):
      for item in self.env.Dictionary().items():
         print(item)
      print('Construct target name  : %s'%self.name)
      print('Construct target arg   : %s'%self.arg)
      for object in self.object:
         print('Construct target object: %s'%object)
   def GetObject(self):
      self.object    = []
      AllSConscript  = []
      for source_path in self.env['SourcePath'].values():
         for dirpath, dirnames, filenames in os.walk(source_path):
            if ("SConscript" in filenames):
               SConscript_path_file = os.path.join(dirpath,"SConscript")
               if SConscript_path_file not in AllSConscript:
                  AllSConscript.append(SConscript_path_file)
                  object = SConscript([SConscript_path_file])
                  if object not in self.object:
                     self.object += object
   def Program(self):
      self.prg = self.env.Program( target = self.env['Target'], source = self.object, )
   def OutPut(self):
      if '=ELF' in self.arg or '=Elf' in self.arg or '=elf' in self.arg:
         POST_ACTION = ' Tools\\ELF\\elfdump.exe %s > %s.txt'%(self.prg[0], self.prg[0])
         self.env.AddPostAction(self.prg, POST_ACTION)
      
      if '=size' in self.arg or '=Size' in self.arg or '=SIZE' in self.arg:
         POST_ACTION = self.env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(self.prg[0], self.env['Target']) + self.env['SIZE'] + ' %s \n'%self.prg[0]\
                     + self.env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(self.prg[0], self.env['Target'])   + self.env['SIZE'] + ' %s \n'%self.prg[0]\
                     + self.env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(self.prg[0], self.env['Target'])  + self.env['SIZE'] + ' %s \n'%self.prg[0]
      else:
         POST_ACTION = self.env['OBJCOPY'] + ' -g -O binary %s %s.bin\n'%(self.prg[0], self.env['Target']) \
                     + self.env['OBJCOPY'] + ' -g -O ihex %s %s.hex\n'%(self.prg[0], self.env['Target'])   \
                     + self.env['OBJCOPY'] + ' -g -O srec %s %s.srec\n'%(self.prg[0], self.env['Target'])
      
      self.env.AddPostAction(self.prg, POST_ACTION)



if ('=bootloader' in sys.argv or '=Bootloader' in sys.argv or '=Boot' in sys.argv or '=BOOT' in sys.argv or '=boot' in sys.argv):
   Project = ConstructTarget('bootloader', base_env, sys.argv)
elif ('=application' in sys.argv or '=Application' in sys.argv or '=App' in sys.argv or '=APP' in sys.argv or '=app' in sys.argv):
   Project = ConstructTarget('application', base_env, sys.argv)
Project.GetConfig()
# Project.CallAutomaticScript()
Project.GetObject()
Project.Program()
Project.OutPut()
# Project.PrintAll()
