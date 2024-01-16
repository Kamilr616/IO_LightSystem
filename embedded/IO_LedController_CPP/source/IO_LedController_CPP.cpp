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


#if defined (__cplusplus)
extern "C" {
#endif

void SysTick_Handler(void)
{
	//neopixels->show();
}

void delay_ms(uint32_t n) {
	for(uint32_t i=0;i<(100*n);i++) // simple delay
	;
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

#endif
	char c;
	char old_c;
	old_c = ' ';

	neopixels = new Neopixels(SPI0_PERIPHERAL);
	neopixels->setAnimColor(0xff0f00);

	neopixels->writeColors(colors);
	neopixels->sendData();
	PRINTF("Start\r\n");
	while(1) {
		c = GETCHAR();
		PRINTF("Znak: %c\r\n", c);

		if (c != old_c) {
		    char validInputs[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};
		    uint32_t isValidInput = 0;

		    for (uint32_t i = 0; i < 7; i++) {
		        if (c == validInputs[i]) {
		            isValidInput = 1;
		            break;
		        }
		    }
		    if (isValidInput) {
		        switch (c) {
					case 'A':
						neopixels->setAnimColor(0xff0000);
						break;
					case 'B':
						neopixels->setAnimColor(0x00ff00);
						break;
					case 'C':
						neopixels->setAnimColor(0x0080ff);
						break;
					case 'D':
						neopixels->setAnimColor(0xff00ff);
						break;
					case 'E':
						neopixels->setAnimColor(0x0000ff);
						break;
					case 'F':
						neopixels->setAnimColor(0x00ffff);
						break;
					case 'G':
						neopixels->setAnimColor(0xff8000);
						break;
					default:
						PRINTF("Error: %c\n", c);
						break;
				}
		old_c = c;
		for(uint32_t j=0; j<(neopixels->getLedsNumber()); j++) {
			neopixels->animate1(neopixels->animColor);
			delay_ms(300);
		}
		}
		}

	}
	delete neopixels;

	return 0 ;
}
