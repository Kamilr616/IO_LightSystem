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
	neopixels->pendulum(9);
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

	neopixels = new Neopixels(SPI0_PERIPHERAL);
	neopixels->writeColors(colorsY);

	SysTick_Config(SystemCoreClock / 5);

	while(1) {
	}
	delete neopixels;

	return 0 ;
}
