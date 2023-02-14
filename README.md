# TrabajoFinGrado

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Contributors](#contributors)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project

This project is about a Telegram bot capable of detecting the atmospheric pollution present in a white sheet or cardboard smeared with Vaseline, the user must upload the photo to the bot together with the location, this information is sent to a web built with Django to be able to visualize the information.

### Built With
* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

<!-- CONTRIBUTORS -->
## Contributors
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/aitormorais">
        <img src="https://avatars3.githubusercontent.com/u/43671531?s=400&v=4"
         width="150px;" alt="Aitor Morais"/><br/><sub><b>Aitor Morais</b></sub></a><br/></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps:

### Prerequisites
* python3
* python3-dev
#### Windows
Download and install Python from this [link](https://www.python.org/downloads/windows/)
#### Linux
```sh
sudo apt install python3 python3-dev
```

### Installation

1. Clone the repository
```sh
git clone https://github.com/aitormorais/TrabajoFinGrado
```

2. Install Python packages
#### Windows
```sh
pip install -r requirements.txt
```
#### Linux
```sh
sudo pip3 install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage
### Demo

You can launch the website locally with the following command:
```sh
python manage.py runserver
```


You can activate the Telegram bot by going into the directory called "bot" and entering the following command: 

```sh
python bot.py 
```
once the bot is active, you should search in telegram for the following name : **@TFGImagen_bot**
if the website is active and the bot is active you can start using it.
Note: _For more information, please refer to the [Django documentation](https://www.djangoproject.com/start/),
[Telegram documentation](https://core.telegram.org/bots/api).


<!-- CONTRIBUTING -->
## Contributing

Feel free to open pull requests with new features or bug fixes. Any contributions you make are **greatly appreciated**.

<!-- CONTACT -->
## Contact
Feel free to ask me any information relevant to the project via email: aitormorais@opendeusto.es

