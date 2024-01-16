/*
 * Neopixels.cpp
 *
 *  Created on: 14 lis 2023
 *      Author: kamil
 */

#include <Neopixels.h>
Neopixels::Neopixels(SPI_Type *base) {
	SPI_base = base;
	SPI_WriteConfigFlags(base, kSPI_ReceiveIgnore);
}

Neopixels::~Neopixels() {
	buffer.clear();
}

uint32_t Neopixels::getLedsNumber() {
	return buffer.size();
}

void Neopixels::addColor(uint32_t color) {
	buffer.push_back(color);
}

void Neopixels::writeColors(std::vector<uint32_t> color) {
	buffer.clear();
	buffer = color;
}

void Neopixels::sendData() {
	uint16_t LED_data=0;
	for(uint32_t j=0;j<getLedsNumber();j++) {
		for(int i=23;i>=0;i--) {
			LED_data = GET_BIT(buffer[j], i) ? CODE_1 : CODE_0;
			while(!(SPI_base->STAT & SPI_STAT_TXRDY_MASK));
			SPI_base->TXDAT = LED_data ;
		}
	}
	// Reset >= 50 us
	LED_data=0;
	for(int j=0;j<50;j++) {
		while(!(SPI_base->STAT & SPI_STAT_TXRDY_MASK));
		SPI_base->TXDAT = LED_data ;
	}
}

//Animacje
void Neopixels::setPosition(uint32_t position, uint32_t color) {
	static uint32_t k=0;
	for(uint32_t j=0; j<getLedsNumber(); j++) {
		buffer[j]=0; // leds off
	}
	buffer[position]=color;

	if(k>=getLedsNumber()) {
		k=0;
	}
	sendData();
}

void Neopixels::fillColor(uint32_t color) {
	static uint32_t k=0;
	for(uint32_t j=0; j<getLedsNumber(); j++) {
		buffer[j]=color; // leds off
	}
	if(k>=getLedsNumber()) {
		k=0;
	}
	sendData();
}

void Neopixels::animate1(uint32_t color) {
	static uint32_t k=0;
	if (k <= 0 ){
		for(uint32_t j=0; j<getLedsNumber(); j++) {
		buffer[j]=0; // leds off
		}
	}
	buffer[k++]=color;

	if(k>=getLedsNumber()) {
		k=0;
	}
	sendData();
}
void Neopixels::shiftLeft(uint32_t number) {
	std::rotate(buffer.begin(), buffer.begin() + number, buffer.end());
	sendData();
}

void Neopixels::shiftRight(uint32_t number ) {
	std::rotate(buffer.rbegin(), buffer.rbegin() + number, buffer.rend());
	sendData();
}

void Neopixels::setAnimColor(uint32_t color){
	animColor = color;
}


void Neopixels::show(){
	if(countPendulum == 0U){
		buffer.clear();
	}
	if(countPendulum < getLedsNumber()){
		addColor(animColor);
		sendData();
		countPendulum++;
	}
	else{
		countPendulum = 0U;
	}
}


void Neopixels::pendulum(uint32_t number){
	if(countPendulum < number){
		shiftLeft();
		countPendulum++;
	}
	else if(countPendulum >= number && countPendulum < (2*number)){
		shiftRight();
		countPendulum++;
	}
	else{
		shiftLeft();
		countPendulum = 1U;
	}
}
