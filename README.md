# What if I had invested in Vanguards??


**Disclaimer: I'm not a financial expert so all this information could very well be wrong!**


Lets say you have some money, how much could you benefit if you put that into a Vanguards account instead of your bank's standard savings account?

This is just a site inspired by my own personal experience of learning about investing




# Demo
Note some text in the demo is a bit outdated but haven't had the time to update the gif

![Demo](img/demo.gif)




# How does it work?

Actual information based on WealthSimple [here](https://help.wealthsimple.com/hc/en-ca/articles/214187018-How-has-the-Growth-portfolio-performed-) so credits to them. This website takes in what free cash you have and
then computes the potential value of the stock portfolio if you invested in WealthSimple based on the average rate of return stated by them. I used their Growth Portfolio's percentages.

# Technology stack

Frontend
* [Bootstrap 4.0](https://getbootstrap.com/)
* [mdBootstrap](https://mdbootstrap.com/) for some animations
* Vanilla JavaScript for some basic DOM manipulation
* CSS
* HTML

Backend
* Django
* Python

# TODO

* The html code was hastily put together so there are some parts of it that could be cleaned

* Implement django forms for user input, right now it it is just sending a post request without input validation

* Make the user input fields's width growth as the input gets bigger

* dockerize the application for quick deployment
