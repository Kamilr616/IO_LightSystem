/*
 * Copyright 2016-2023 NXP
 * All rights reserved.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

/**
 * @file    IO_LedController_CPP.cpp
 * @brief   Application entry point.
 */
#include <stdio.h>
#include "board.h"
#include "peripherals.h"
#include "pin_mux.h"
#include "clock_config.h"
#include "LPC804.h"
#include "fsl_debug_console.h"
#include "Neopixels.h"
#include "fsl_usart.h"

Neopixels *neopixels;

uint32_t mode = 0;


std::vector<uint32_t> colors = {
		// GRB
		0x00ff00, //red
		0x80ff00, //orange
		0xffff00, //yellow
		0xff8000, //chartreuse
		0xff0000, //green
		0xff0080, //spring green
		0xff00ff, //cyan
		0x8000ff, //dodger blue
		0x0000ff, //blue
		0x0080ff, //purple
		0x00ffff, //violet
};

std::vector<uint32_t> colorsY = {
		// GRB
		0xffff00, //yellow
		0x000000, //black
		0x000000, //black
		0x000000, //black
		0x000000, //black
		0x000000, //black
		0x000000, //black
		0x000000, //black
		0x000000, //black
		0x000000, //black
};


#if defined (__cplusplus)
extern "C" {
#endif

void SysTick_Handler(void)
{
	neopixels->shiftRight();
}

#if defined (__cplusplus)
} // extern "C"
#endif
/*
 * @brief Application entry point.
 */

int main(void) {
	/* Init board hardware. */
	BOARD_InitBootPins();
	BOARD_InitBootClocks();
	BOARD_InitBootPeripherals();
#ifndef BOARD_INIT_DEBUG_CONSOLE_PERIPHERAL
	/* Init FSL debug console. */
	BOARD_InitDebugConsole();
//	usart_config_t user_config;
//	USART_GetDefaultConfig(&user_config);
//	user_config.baudRate_Bps = 9600U;
//	user_config.enableTx = true;
//	user_config.enableRx = true;
//	USART_Init(USART0,&user_config,120000000U);

#endif
	char c;

	neopixels = new Neopixels(SPI0_PERIPHERAL);
	neopixels->writeColors(colors);
	neopixels->sendData();
	//SysTick_Config(SystemCoreClock / 5);
	PRINTF("Start\r\n");
	while(1) {

		c = GETCHAR();
		PRINTF("Pozycja: %c\r\n", c);
		//USART_ReadBlocking(USART0, input, 5);
		switch (c) {
		        case '0':
		            neopixels->setPosition(0, 0xffff00);
		            break;
		        case '1':
		            neopixels->setPosition(1, 0xffff00);
		            break;
		        case '2':
		            neopixels->setPosition(2, 0xffff00);
		            break;
		        case '3':
		            neopixels->setPosition(3, 0xffff00);
		            break;
		        case '4':
		            neopixels->setPosition(4, 0xffff00);
		            break;
		        case '5':
		            neopixels->setPosition(5, 0xffff00);
		            break;
		        case '6':
		            neopixels->setPosition(6, 0xffff00);
		            break;
		        case '7':
		            neopixels->setPosition(7, 0xffff00);
		            break;
		        case '8':
		            neopixels->setPosition(8, 0xffff00);
		            break;
		        case '9':
		            neopixels->setPosition(9, 0xffff00);
		            break;
		        default:
		            PRINTF("Error: %c\n", c);
		    }

	}
	delete neopixels;

	return 0 ;
}
