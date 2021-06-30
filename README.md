# Cli_suite
## _Modular CLI with information at a glance_

Personal command line interface suite for with useful information, modular with different tools.

![alt text](https://raw.githubusercontent.com/LobsterBM/cli_suite/main/screenshot.png?token=AJAGATARRB4XX7QU5YD2CALA4UB3Y)

## Dependencies 
* requests==2.22.0
* terminaltables==3.1.0
* termgraph==0.5.1
* termcolor==1.1.0
* geopy==2.1.0
* psutil==5.8.0

*Note: not yet tested on Mac or Windows



## Features

*** 
### Weather module
Shows current and future weather (temperature , weather , wind)  in a selected location .

Powered by : Openweathermap

### Cryptocurrency ticker
Shows info for various cryptocurrencies. (24 max/min , 24% , price)
* Add or remove different cryptocurrencies 
* Select FIAT currency for price comparison

Powered by : Coingecko

### System monitor
Show graph with RAM and CPU  usage 

## Usage
  
```sh
 -fiat , -f : updates fiat currency for cryptocurrency comparison
```
 ```sh
 -crypto , -c : adds cryptocurrency to the list , you can add multiple coins separated by a space
 ```
 ```sh
 -rcrypto , -rc : removes cryptocurrency from the list, also supports multiple coins
 ```
 
 ```sh
  -timer , -t : time in seconds for interface to update 
  ```
 ```sh
 -location , -l : location for weather info , location in one words , no spaces
 ```
 ```sh
 -modules , -m  : modules to add to the interface , separated by spaces
 ```
 ```sh
 -rmodules , -m : modules to remove from interface
 ```
 ```sh
 -weatherhours -w : number of hours for weather forecasting
```

## Installation

Just pip install all requirements.

## Development

Feel free to add tools, or simply feedback or ideas.

## License

MIT

https://openweathermap.org : Creative Commons Attribution-ShareAlike 4.0 International license (CC BY-SA 4.0)

Coingecko license & ToS : https://www.coingecko.com/en/api_terms


