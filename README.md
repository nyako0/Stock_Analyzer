# Stock_Analyzer
stock_helper

It's a project for Parsing data from stock exchange website, then computer transmit data (coded name of company and P/E coefficient) via UART. After that STM32 recieves data, makes array of strutures for every company, sorts it (P/E coefficient should be small) and transmits data on PC.

STM32 code is in STM32-app/MDK-ARM/StCubeGenerated.uvprojx
