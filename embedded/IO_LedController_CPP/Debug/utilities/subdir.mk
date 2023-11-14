################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../utilities/fsl_assert.c \
../utilities/fsl_debug_console.c \
../utilities/fsl_str.c 

C_DEPS += \
./utilities/fsl_assert.d \
./utilities/fsl_debug_console.d \
./utilities/fsl_str.d 

OBJS += \
./utilities/fsl_assert.o \
./utilities/fsl_debug_console.o \
./utilities/fsl_str.o 


# Each subdirectory must supply rules for building sources it contributes
utilities/%.o: ../utilities/%.c utilities/subdir.mk
	@echo 'Building file: $<'
	@echo 'Invoking: MCU C Compiler'
	arm-none-eabi-gcc -D__NEWLIB__ -DCPU_LPC804M101JDH24 -DCPU_LPC804M101JDH24_cm0plus -DSDK_OS_BAREMETAL -DSDK_DEBUGCONSOLE=1 -D__MCUXPRESSO -D__USE_CMSIS -DDEBUG -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/board" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/source" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/drivers" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/CMSIS" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/device" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/component/uart" -I"/home/kamil/PycharmProjects/IO_LightSystem/embedded/IO_LedController_CPP/utilities" -O0 -fno-common -g3 -Wall -c -ffunction-sections -fdata-sections -ffreestanding -fno-builtin -fmerge-constants -fmacro-prefix-map="$(<D)/"= -mcpu=cortex-m0plus -mthumb -D__NEWLIB__ -fstack-usage -specs=nano.specs -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.o)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


clean: clean-utilities

clean-utilities:
	-$(RM) ./utilities/fsl_assert.d ./utilities/fsl_assert.o ./utilities/fsl_debug_console.d ./utilities/fsl_debug_console.o ./utilities/fsl_str.d ./utilities/fsl_str.o

.PHONY: clean-utilities

