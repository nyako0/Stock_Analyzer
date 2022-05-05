/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
  ******************************************************************************
  * @attention
  *
  * <h2><center>&copy; Copyright (c) 2022 STMicroelectronics.
  * All rights reserved.</center></h2>
  *
  * This software component is licensed by ST under BSD 3-Clause license,
  * the "License"; You may not use this file except in compliance with the
  * License. You may obtain a copy of the License at:
  *                        opensource.org/licenses/BSD-3-Clause
  *
  ******************************************************************************
  */
/* USER CODE END Header */
/* Includes ------------------------------------------------------------------*/
#include "main.h"
#include <stdio.h>
#include <string.h>
#include "stm32f0xx_hal_def.h"
#include "stm32f0xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */

/* USER CODE END Includes */

/* Private typedef -----------------------------------------------------------*/
/* USER CODE BEGIN PTD */

/* USER CODE END PTD */

/* Private define ------------------------------------------------------------*/
/* USER CODE BEGIN PD */
/* USER CODE END PD */

/* Private macro -------------------------------------------------------------*/
/* USER CODE BEGIN PM */

/* USER CODE END PM */

/* Private variables ---------------------------------------------------------*/
UART_HandleTypeDef huart1;

/* USER CODE BEGIN PV */

enum responses {
    RESP_OK = 1,
  RESP_CALC,
  RESP_TOP,
  RESP_BOT,
  RESP_ERR
  
};

struct company
{
  uint8_t company;
  uint8_t PE;
};
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART1_UART_Init(void);
/* USER CODE BEGIN PFP */
void get_worst (struct company *data)
{
  int i=0;
  for (i=0;i<10;i++)
  {
    HAL_UART_Transmit(&huart1, (uint8_t *) &data[i].company, 1, 200);
  }
}

void get_top (struct company *data)
{
  int i=0;
  for (i=99;i>89;i--)
  {
    HAL_UART_Transmit(&huart1, (uint8_t *) &data[i].company, 1, 200);
  }
}


void get_three(struct company *data)
{
  uint8_t resp;
  
  if (HAL_UART_Receive(&huart1, &resp, sizeof(resp), 200000) == HAL_OK && resp == 0x03)
  {
    resp = RESP_TOP;
    
  }
  else
  {
    resp = RESP_ERR;
    
  }

    HAL_UART_Transmit(&huart1,&resp, 1, 200);
  
   if (resp == RESP_TOP)
  {

     get_top(data);

  }
}
void get_four(struct company *data)
{
  uint8_t resp;
  
  while (HAL_UART_Receive(&huart1, &resp, sizeof(resp), 1000) != HAL_OK)
  {
    if (resp != 0x04)
			resp = RESP_ERR;
			continue;
  }
		resp = RESP_BOT;
  

    HAL_UART_Transmit(&huart1,&resp, 1, 200);
  
   if (resp == RESP_BOT)
  {

     get_worst(data);

  }
}
void bsortDesc(struct company *data ,int s)
{
    uint8_t i, j;
    struct company temp;
    
    for (i = 0; i < s - 1; i++)
    {
        for (j = 0; j < (s - 1-i); j++)
        {
            if (data[j].PE < data[j + 1].PE)
            {
                temp = data[j];
                data[j] = data[j + 1];
                data[j + 1] = temp;
            } 
        }
    }
    for (int k=0; k < s; ++k)
    {
      HAL_UART_Transmit(&huart1, (uint8_t *) &data[k], 2, 200);
    }
    

}


void get_second (struct company *data)
{
  uint8_t resp; 
  while  (HAL_UART_Receive(&huart1, &resp, sizeof(resp), 1000) != HAL_OK)
  {
    if(resp != 0x02)
			resp = RESP_ERR;
			continue;
	}
	resp = RESP_CALC;


  HAL_UART_Transmit(&huart1,&resp, 1, 200);
  
   if (resp == RESP_CALC)
  {
     bsortDesc(data, 100);
  }
}


/* USER CODE END PFP */
uint16_t receive_data(struct company *data)
{
  uint8_t i;
  for (i=0;i<100;++i)
  {
     if (HAL_UART_Receive(&huart1, (uint8_t*)(data+i),sizeof(struct company) , 1000) != HAL_OK)
    {
      --i;
			continue;
    }
    else 
    {
      HAL_UART_Transmit(&huart1,(uint8_t *) &data[i] , sizeof(struct company), 200);
    }
  }
    return i;
}

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  * @retval int
  */
int main(void){
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration--------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_USART1_UART_Init();
  /* USER CODE BEGIN 2 */

  /* USER CODE END 2 */
	/*strcpy((char *)TxData, "Got it\r\n");*/
  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
 // __HAL_UART_ENABLE_IT(&huart1, UART_IT_RXNE);
	// __HAL_UART_ENABLE_IT(&huart1, UART_IT_TC);
	//HAL_UART_Receive_IT(&huart1, (uint8_t *)RxData, 5);
	//HAL_UART_Receive_IT(&huart1, RxData, 1);
	
  while (1)
  {
	int N=100;
  struct company data[N];
  uint8_t resp;
	HAL_Delay(1000);
  if (HAL_UART_Receive(&huart1, &resp, sizeof(resp), 1000) == HAL_OK && resp == 0x01)
  {
    resp = RESP_OK;
  }
  else
  {
    resp = RESP_ERR;
  }
	

  HAL_UART_Transmit(&huart1,&resp, 1, 200);
  
   if (resp == RESP_OK)
  {
    receive_data(data);
  }
       //print_data(data, sizeof(data)/sizeof(data[0]));
  get_second(data);
    
 
  get_three(data);
  get_four(data);	
	}
    /* USER CODE END WHILE */
	/*HAL_UART_Transmit(&huart1, TxData, 15, 200);*/
	
	
/*	int i = sizeof(RxData) / sizeof(RxData[0]);
	if (RxData[i]==0x20)
		HAL_UART_Transmit(&huart1, TxData, 15, 200);
*/		
	
		
    /* USER CODE BEGIN 3 */
  
  /* USER CODE END 3 */

/**
  * @brief System Clock Configuration
  * @retval None
  */
}
void SystemClock_Config(void)
{
  RCC_OscInitTypeDef RCC_OscInitStruct = {0};
  RCC_ClkInitTypeDef RCC_ClkInitStruct = {0};
  RCC_PeriphCLKInitTypeDef PeriphClkInit = {0};

  /** Initializes the RCC Oscillators according to the specified parameters
  * in the RCC_OscInitTypeDef structure.
  */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL6;
  RCC_OscInitStruct.PLL.PREDIV = RCC_PREDIV_DIV1;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    Error_Handler();
  }
  /** Initializes the CPU, AHB and APB buses clocks
  */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_1) != HAL_OK)
  {
    Error_Handler();
  }
  PeriphClkInit.PeriphClockSelection = RCC_PERIPHCLK_USART1;
  PeriphClkInit.Usart1ClockSelection = RCC_USART1CLKSOURCE_PCLK1;
  if (HAL_RCCEx_PeriphCLKConfig(&PeriphClkInit) != HAL_OK)
  {
    Error_Handler();
  }
}

/**
  * @brief USART1 Initialization Function
  * @param None
  * @retval None
  */
static void MX_USART1_UART_Init(void)
{

  /* USER CODE BEGIN USART1_Init 0 */

  /* USER CODE END USART1_Init 0 */

  /* USER CODE BEGIN USART1_Init 1 */

  /* USER CODE END USART1_Init 1 */
  huart1.Instance = USART1;
  huart1.Init.BaudRate = 38400;
  huart1.Init.WordLength = UART_WORDLENGTH_8B;
  huart1.Init.StopBits = UART_STOPBITS_1;
  huart1.Init.Parity = UART_PARITY_NONE;
  huart1.Init.Mode = UART_MODE_TX_RX;
  huart1.Init.HwFlowCtl = UART_HWCONTROL_NONE;
  huart1.Init.OverSampling = UART_OVERSAMPLING_16;
  huart1.Init.OneBitSampling = UART_ONE_BIT_SAMPLE_DISABLE;
  huart1.AdvancedInit.AdvFeatureInit = UART_ADVFEATURE_NO_INIT;
  if (HAL_UART_Init(&huart1) != HAL_OK)
  {
    Error_Handler();
  }
  /* USER CODE BEGIN USART1_Init 2 */

  /* USER CODE END USART1_Init 2 */

}

/**
  * @brief GPIO Initialization Function
  * @param None
  * @retval None
  */
static void MX_GPIO_Init(void)
{

  /* GPIO Ports Clock Enable */
  __HAL_RCC_GPIOF_CLK_ENABLE();
  __HAL_RCC_GPIOA_CLK_ENABLE();

}

/* USER CODE BEGIN 4 */

/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @retval None
  */
void Error_Handler(void)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  __disable_irq();
  while (1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t *file, uint32_t line)
{
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
