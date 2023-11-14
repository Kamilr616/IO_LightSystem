################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
CPP_SRCS += \
../source/IO_LedController_CPP.cpp \
../source/Neopixels.cpp \
../source/cpp_config.cpp 

C_SRCS += \
../source/semihost_hardfault.c 

CPP_DEPS += \
./source/IO_LedController_CPP.d \
./source/Neopixels.d \
./source/cpp_config.d 

C_DEPS += \
./source/semihost_hardfault.d 

OBJS += \
./source/IO_LedController_CPP.o \
./source/Neopixels.o \
./source/cpp_config.o \
./source/semihost_hardfault.o 


# Each subdirectory must supply rules for building sources it contributes
source/%.o: ../source/%.cpp source/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C++ Compiler'
	arm-none-eabi-c++ -DCPU_LPC804M101JDH24 -DCPU_LPC804M101JDH24_cm0plus -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -D__NEWLIB__ -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/board" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/source" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/drivers" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/CMSIS" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/device" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/component/uart" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/utilities" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fno-rtti -fno-exceptions -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m0plus -mthumb -D__NEWLIB__ -fstack-usage -specs=nano.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

source/%.o: ../source/%.c source/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__NEWLIB__ -DCPU_LPC804M101JDH24 -DCPU_LPC804M101JDH24_cm0plus -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/board" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/source" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/drivers" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/CMSIS" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/device" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/component/uart" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/utilities" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m0plus -mthumb -D__NEWLIB__ -fstack-usage -specs=nano.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-source

clean-source:
	-$(RM) ./source/IO_LedController_CPP.d ./source/IO_LedController_CPP.o ./source/Neopixels.d ./source/Neopixels.o ./source/cpp_config.d ./source/cpp_config.o ./source/semihost_hardfault.d ./source/semihost_hardfault.o

.PHONY: clean-source

