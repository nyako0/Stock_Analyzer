import stocks_scraper
import uart_driver
import time
import name_company

#COM Port config
com_port = 'COM22'

send_data_state = 0
calculate_state = 0
get_top_10_state = 0
get_bottom_10_state = 0
con = 0

def get_data(info, top_10, bottom_10):
    try:
        top_10.set('No data provided')
        bottom_10.set('No data provided')

        info.set('    Getting data from the web...')

        global stocks
        stocks = stocks_scraper.get_stocks_data()
        info.set('    Data was received from the web')

        global send_data_state
        send_data_state = 1
    except Exception as e:
        print(e)
        info.set(f'    {e}')

def send_data(info):
    try:
        info.set('    Sending data to the external machine...')
        time.sleep(1)

        global con
        if con == 0:
            global external_machine
            external_machine = uart_driver.UARTDriver(com_port, 38400)
            con += 1

        external_machine.com_send([1])
        answer = external_machine.com_read(1)

        if answer == b'\x01':
            names = stocks[0]
            coeficients = stocks[1]
            companies = name_company.number_company(names) 

            for i in range(len(names)):
                coeficient_to_send = int(float(coeficients[i]))
                if coeficient_to_send > 255:
                    coeficient_to_send = 255
                
                external_machine.com_send([companies[i][1], coeficient_to_send])
                external_machine.com_read(2)
                
            info.set('    Data was sent to the external machine')

            global calculate_state
            calculate_state = 1
        else:
            info.set('    Error! Data was not sent to the external machine')
    except Exception as e:
        print(e)
        info.set(f'    {e}')

def calculate(info):
    try:
        info.set('    Calculating the stocks on the external machine...')
        time.sleep(1)

        external_machine.com_send([2])
        answer = external_machine.com_read(1)

        if answer == b'\x02':
            info.set('    Calculation was done on the external machine')
        else:
            info.set('    Error! Calculation was not done on the external machine')

        for i in range(len(stocks[0])):
            external_machine.com_read(2)
        
        global get_top_10_state
        get_top_10_state = 1

    except Exception as e:
        print(e)
        info.set(f'    {e}')

def get_top_10(info, top_10):
    try:
        info.set('    Getting top 10 stocks from the external machine...')
        time.sleep(1)

        text = ''
        external_machine.com_send([3])
        answer = external_machine.com_read(1)

        if answer == b'\x03':
            for i in range(10):
                num = int.from_bytes(external_machine.com_read(1), 'big')
                data = stocks[0][num]
                if i == 0:
                    text = f'{i+1}. {data}'
                else:
                    text += f'\n{i+1}. {data}'
            top_10.set(text)

            info.set('    Top 10 stocks were received from the external machine')

            global get_bottom_10_state
            get_bottom_10_state = 1

        else:
            info.set('    Error! Top 10 stocks were not received from the external machine')
    except Exception as e:
        print(e)
        info.set(f'    {e}')

def get_bottom_10(info, bottom_10):
    try:
        info.set('    Getting worst 10 stocks from the external machine...')
        time.sleep(1)

        text = ''
        external_machine.com_send([4])
        answer = external_machine.com_read(1)

        if answer == b'\x04':
            for i in range(10):
                num = int.from_bytes(external_machine.com_read(1), 'big')
                data = stocks[0][num]
                if i == 0:
                    text = f'{i+1}. {data}'
                else:
                    text += f'\n{i+1}. {data}'
            bottom_10.set(text)

            info.set('    Worst 10 stocks were received from the external machine')

            global send_data_state
            send_data_state = 0
            global calculate_state
            calculate_state = 0
            global get_top_10_state
            get_top_10_state = 0
            global get_bottom_10_state 
            get_bottom_10_state = 0

        else:
            info.set('    Error! Worst 10 stocks were not received from the external machine')
    except Exception as e:
        print(e)
        info.set(f'    {e}')