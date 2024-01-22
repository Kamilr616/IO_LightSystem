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

Neopixels *neopixels;


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


void delay_(uint32_t delay_count) {
    for (uint32_t i = 0; i < (delay_count * 100); i++) {
        __asm volatile("nop");
    }
}

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
	char c, old_c;
	old_c = ' ';

	neopixels = new Neopixels(SPI0_PERIPHERAL);
	neopixels->writeColors(colors);
	neopixels->sendData();
	PRINTF("Start\r\n");
	while(1) {
		c = GETCHAR();
		PRINTF("Incoming: %c\r\n", c);

		if (c != old_c) {
		    char validInputs[7] = {'A', 'B', 'C', 'D', 'E', 'F', 'G'};
		    bool isValidInput = false;

		    for (uint32_t i = 0; i < 7; i++) {
		        if (c == validInputs[i]) {
		            isValidInput = true;
		            break;
		        }
		    }
		    if (isValidInput) {
		    	switch (c) {
		    	    case 'A':
		    	        neopixels->setAnimColor(0xff0000);  // Thumb_Up: Zielony
		    	        break;
		    	    case 'B':
		    	        neopixels->setAnimColor(0x0080ff);  // Thumb_Down: Purpurowy
		    	        break;
		    	    case 'C':
		    	        neopixels->setAnimColor(0x0000ff);  // Open_Palm: Niebieski
		    	        break;
		    	    case 'D':
		    	        neopixels->setAnimColor(0xffff00);  // Closed_Fist: Żółty
		    	        break;
		    	    case 'E':
		    	        neopixels->setAnimColor(0xff0080);  // Victory: Spring green
		    	        break;
		    	    case 'F':
		    	        neopixels->setAnimColor(0xff00ff);  // Pointing_Up: Cyjanowy
		    	        break;
		    	    case 'G':
		    	        neopixels->setAnimColor(0x00ff00);  // ILoveYou: Czerwony
		    	        break;
		    	    default:
		    	        PRINTF("Value error: %c\n", c);
		    	        neopixels->setAnimColor(0xffffff);
		    	        break;
		    	}
		old_c = c;
		for(uint32_t j=0; j<(neopixels->getLedsNumber()); j++) {
			neopixels->animate_flow();
			neopixels->sendData();
			delay_(300);
		}
		}
		}
	}
	delete neopixels;

	return 0 ;
}
