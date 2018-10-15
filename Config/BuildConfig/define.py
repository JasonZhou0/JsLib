Define = {}
Define['bootloader']=[
   # 'STM32F407xx',
   # '__GNUC__',
   'STM32F407VE',
   'STM32F4XX',
   'USE_STDPERIPH_DRIVER',
   '__ASSEMBLY__',
   # 'ARM_MATH_CM4',
   # '__CC_ARM',
   '__FPU_USED=1',
   '__FPU_PRESENT=1',
   'BOOTLOADER_ADDRESS=0x08000000',
   'APPLICATION_ADDRESS=0x08002000',
   'CODE_ENTRY_ADDRESS=BOOTLOADER_ADDRESS',
   ]

Define['application']=[
   # 'STM32F407xx',
   # '__GNUC__',
   'STM32F407VE',
   'STM32F4XX',
   'USE_STDPERIPH_DRIVER',
   '__ASSEMBLY__',
   # 'ARM_MATH_CM4',
   # '__CC_ARM',
   '__FPU_USED=1',
   '__FPU_PRESENT=1',
   'BOOTLOADER_ADDRESS=0x08000000',
   'APPLICATION_ADDRESS=0x08002000',
   'CODE_ENTRY_ADDRESS=APPLICATION_ADDRESS',
   ]
   
if __name__ == '__main__':
   import os
   print(Define)
   os.system('pause')