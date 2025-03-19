# BotBattleOfSea

* VS-Code setup: [Link](docs/vscode_setup/README.md)

## Overview

BotBattleOfSea is an advanced AI-driven bot designed for competitive gameplay in the Battle of Sea game. This bot is engineered to demonstrate strategic thinking and adaptability in real-time gaming scenarios. The main purpose is to collect the glitters and, when the bot-question comes up, to identify and answer the questions.

### Data Preparation

The effectiveness of BotBattleOfSea relies on meticulous data preparation. This involves gathering, cleaning, and preprocessing data to ensure the bot can make accurate decisions during gameplay.

![Data Preparation](https://raw.githubusercontent.com/MariosChartsias/BotBattleOfSea/main/img/banner-integrations.png?token=GHSAT0AAAAAACTB7RTGYNKUOGI3BIL5NIRMZS276SQ)

Key steps in data preparation include:

- **Data Collection**: Accumulating gameplay data to train and test the bot.
- **Data Cleaning**: Removing inconsistencies and noise from the data to improve accuracy.
- **Feature Engineering**: Creating meaningful features that enhance the bot's learning process.
- **Data Splitting**: Dividing the data into training, validation, and test sets to evaluate performance.

### OCR Detection
#### screenshot 1 before detection
<img src="https://raw.githubusercontent.com/MariosChartsias/BotBattleOfSea/refs/heads/main/img/ocr%20before%20detection.png" alt="OCR Detection" width="1500"/>

#### screenshot 1 after detection
<img src="https://raw.githubusercontent.com/MariosChartsias/BotBattleOfSea/main/img/ocr%20after%20detection.jpg?token=GHSAT0AAAAAACTB7RTGKXOXCUQBRO7CP2P2ZS3AIVQ" alt="OCR Detection" width="1500"/>

#### screenshot 2 after detection (only)
<img src="https://raw.githubusercontent.com/MariosChartsias/BotBattleOfSea/main/img/01e62519-e5e5-465e-be29-69c2d059b50f.png?token=GHSAT0AAAAAACTB7RTGQWUAWSMH7LU7NURUZS3AVDA" width="1500"/>

## Features

- **Strategic Planning**: Implements complex algorithms to predict and counter opponent moves.
- **Real-Time Decision Making**: Utilizes real-time data to make quick and effective decisions.
- **Adaptability**: Adjusts strategies based on opponent behavior and game progression.

## Installation

Follow the instructions in the [VS-Code setup](docs/vscode_setup/README.md) to set up the development environment.

## Usage

1. Clone the repository.
2. Open the project in VS-Code.
3. Follow the setup instructions provided in the documentation.
4. Run the bot using the provided scripts.

## Development

The bot is developed using a modular approach, allowing for easy updates and enhancements. Key components include:

- **Game Engine Interface**: Facilitates communication with the Battle of Sea game engine.
- **Strategy Module**: Contains the core algorithms for gameplay.
- **Learning Module**: Implements machine learning techniques to improve performance over time.

## Contribution

We welcome contributions from the community. Please read our [contributing guidelines](docs/contributing.md) before submitting pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
