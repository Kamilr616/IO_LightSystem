/*
 * Neopixels.h
 *
 *  Created on: 14 lis 2023
 *      Author: kamil
 */

#ifndef NEOPIXELS_H_
#define NEOPIXELS_H_
#include <vector>
#include <algorithm>
#include "fsl_spi.h"
#define GET_BIT(k, n) (k & (1 << (n)))
#define SET_BIT(k, n) (k |= (1 << (n)))
#define CLR_BIT(k, n) (k &= ~(1 << (n)))
#define CODE_0 0b10000
#define CODE_1 0b11100

class Neopixels {

public:
	Neopixels(SPI_Type *base);
	virtual ~Neopixels();
	uint32_t getLedsNumber();
	void addColor(uint32_t color);
	void writeColors(std::vector<uint32_t> color);
	void sendData();

	void shiftLeft(uint32_t number = 1U);
	void shiftRight(uint32_t number = 1U);
	void animate_flow();
	void setPosition(uint32_t position=0U, uint32_t color=0x00ff00);
	void pendulum(uint32_t number);
	void fillColor(uint32_t color);
	void setAnimColor(uint32_t color = 0x00ff00);


private:
	SPI_Type *SPI_base=NULL;
	std::vector<uint32_t> buffer;
	uint32_t countPendulum = 0U;
	uint32_t animColor = 0x00ff00;


};

#endif /* NEOPIXELS_H_ */
