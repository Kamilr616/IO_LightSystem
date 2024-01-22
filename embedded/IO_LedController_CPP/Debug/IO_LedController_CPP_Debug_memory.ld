/*
 * GENERATED FILE - DO NOT EDIT
 * Copyright 2008-2013 Code Red Technologies Ltd,
 * Copyright 2013-2024 NXP
 * Generated linker script file for LPC804
 * Created from memory.ldt by FMCreateLinkMemory
 * Using Freemarker v2.3.30
 * MCUXpresso IDE v11.8.1 [Build 1197] [2023-10-27] on 22 sty 2024, 19:54:47
 */

MEMORY
{
  /* Define each memory region */
  PROGRAM_FLASH (rx) : ORIGIN = 0x0, LENGTH = 0x7f80 /* 32640 bytes (alias Flash) */  
  BOOT_FLASH (rx) : ORIGIN = 0x7f80, LENGTH = 0x80 /* 128 bytes (alias Flash2) */  
  SRAM (rwx) : ORIGIN = 0x10000000, LENGTH = 0xfe0 /* 4064 bytes (alias RAM) */  
  IAP_SRAM (rwx) : ORIGIN = 0x10000fe0, LENGTH = 0x20 /* 32 bytes (alias RAM2) */  
}

  /* Define a symbol for the top of each memory region */
  __base_PROGRAM_FLASH = 0x0  ; /* PROGRAM_FLASH */  
  __base_Flash = 0x0 ; /* Flash */  
  __top_PROGRAM_FLASH = 0x0 + 0x7f80 ; /* 32640 bytes */  
  __top_Flash = 0x0 + 0x7f80 ; /* 32640 bytes */  
  __base_BOOT_FLASH = 0x7f80  ; /* BOOT_FLASH */  
  __base_Flash2 = 0x7f80 ; /* Flash2 */  
  __top_BOOT_FLASH = 0x7f80 + 0x80 ; /* 128 bytes */  
  __top_Flash2 = 0x7f80 + 0x80 ; /* 128 bytes */  
  __base_SRAM = 0x10000000  ; /* SRAM */  
  __base_RAM = 0x10000000 ; /* RAM */  
  __top_SRAM = 0x10000000 + 0xfe0 ; /* 4064 bytes */  
  __top_RAM = 0x10000000 + 0xfe0 ; /* 4064 bytes */  
  __base_IAP_SRAM = 0x10000fe0  ; /* IAP_SRAM */  
  __base_RAM2 = 0x10000fe0 ; /* RAM2 */  
  __top_IAP_SRAM = 0x10000fe0 + 0x20 ; /* 32 bytes */  
  __top_RAM2 = 0x10000fe0 + 0x20 ; /* 32 bytes */  
