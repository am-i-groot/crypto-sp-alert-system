# Crypto-SP-Alert-System
Coded for Buzzer to give alerts whenever selling price crosses a barrier that will allow to have Crypto Compare interface for Bitcoin like Cryptocurrency. Executed python codes in Linux (ubuntu) on VMware Workstation 17 Player using multiple libraries.

*THIS PROJECT DOES NOT REQUIRE YOU TO HAVE A BITCOIN WALLET AND/OR PURCHASE/SELL BITCOINS. ALL THE EXTERNAL APIS USED IN THIS PROJECT ARE PUBLIC AND IT IS A PURELY EDUCATIONAL PROJECT.*

This is an interesting assignment which is based on the popular cryptocurrency called Bitcoin. You have to build a Bitcoin Price Alert System using Bolt IoT . As a part of this you will write a Python program that checks the current price of Bitcoin and alerts you if the price is greater than the selling price that you have set. Before you jump to the tasks, lets learn a bit about Bitcoin.

## What is Bitcoin?
A software developer going by the name of Satoshi Nakamoto proposed bitcoin in 2008, as an electronic payment system based on mathematical proof. The idea was to produce a means of exchange, independent of any central authority, that could be transferred electronically in a secure, verifiable and immutable way.

Since its launch in 2009, Bitcoin has been a controversial concept. Some people accept it as an anonymous currency, which protects their privacy and also provides a unified platform for all kinds of transactions online. Whereas there are others who shun it saying that it 's the currency of the black market.

But, the recent upshoot of the Bitcoin price has made everyone want to invest in it. There are stories about people who paid 25,000 Bitcoins for a pizza back in 2009-10 and are now regretting that decision. Whereas there are others who are running mining rigs and farms and making millions. But, it is not necessary that the Bitcoin price always stays high. Sometimes it rises and sometimes it falls so why not build a system that tells us when it rises and when it falls.

## Task 1: Understand the Price API
To build the Bitcoin Price Alerting system, we will require a method to find the current price of Bitcoin by writing a Python program. We will use the following website https://min-api.cryptocompare.com to get the price of Bitcoin. It is a very popular site that provides APIs using which you can fetch various cryptocurrency related data. You don't need  to create an account on the site for this assignment. On this website all currencies are called as symbols or “sym ”in short. You will use the Single Symbol Price API to get the price of Bitcoin in USD. Here is the documentation of the Single Symbol Price API: https://min-api.cryptocompare.com/documentation?key=Price &cat=SingleSymbolPriceEndpoint .

Read the API documentation to see what is the API URL you should use in your Python program as well as read about the parameters that you can need to pass to this API. You will also find the execute call button which you can click to test and see the result that the API provides. Can you now find out what will be the URL to get the price of Bitcoin in USD and INR?

## Task 2: Setup a Buzzer
Connect the buzzer to your Bolt module. The buzzer will be switched ON when the current price of the Bitcoin is greater than the selling price defined by you.

## Task 3: Bitcoin Price Alerting System
Write a Python program that will do the following

Fetch the current price of Bitcoin every 30 seconds using the Single Symbol Price API in USD.
Check if the current price returned by the API is greater than the selling price defined by you. You can define the selling price as a variable in your program.
If the current price is greater than the selling price, the program should trigger the Bolt Cloud API to switch on the buzzer connected to the Bolt module for 5 seconds and then switches it off after 5 seconds.
Your program should repeat the steps 1,2,3 continuously every 30 seconds.
You will require some additional Python libraries to be installed to run this project. We will also provide you a reference of the Python function to get the current price of Bitcoin. You will need to use these resources listed below to complete this assignment.
NOTE: Make sure that your program checks the value of Bitcoin every 30 seconds or more and not any lesser time than 30 seconds as you can get rate limited on the Bolt Cloud if you make the API calls too fast. Then you will have to wait until your API calls are allowed.

## Resources:
1. Make sure that you have installed the following libraries before your write the Python program.

```
sudo apt-get update
sudo pip3 install boltiot
sudo pip3 install pyOpenSSL ndg-httpsclient pyasn1
sudo pip3 install 'requests[security]'
```
2. Use the following Python function in your program to fetch the current price of Bitcoin. However you will have to replace the `URL` variable in the code with the URL you obtained in task 1 for the getting the price of Bitcoin in USD.

```
def get_bitcoin_price():
  URL = "https://min-api.cryptocompare.com/"# REPLACE WITH CORRECT URL
  response = requests.request("GET ", URL)
  response = json.loads(response.text)
  current_price = response["USD "]
  return current_price
```
## Submitting The Solution:
This assignment is meant to be a self-study exercise, and you do not have to submit this a solution for this assignment.

