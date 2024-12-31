# Text Encryption and Decryption

This project is a Python-based application for encrypting and decrypting text using the Caesar Cipher technique. The application is available in two versions:
1. A command-line interface (CLI) version.
2. A graphical user interface (GUI) version built using Tkinter.

## Features

- **Encryption**: Converts plain text into encrypted text using a shift key.
- **Decryption**: Converts encrypted text back to the original plain text using the same shift key.
- **User-Friendly GUI**: The GUI version offers an intuitive interface for users to interact with the application.

## Prerequisites

- Python 3.x

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/anugrahromadhon/text-encryption-decryption
   ```
2. Navigate to the project directory:
   ```bash
   cd text-encryption-decryption
   ```

*Note: The GUI version requires Tkinter, which is pre-installed with most Python distributions.*

## Usage

### CLI Version
1. Open a terminal.
2. Run the script:
   ```bash
   python main.py
   ```
3. Follow the on-screen prompts to enter the text, shift key, and choose between encryption or decryption.

### GUI Version
1. Open a terminal.
2. Run the script:
   ```bash
   python main_2.py
   ```
3. Interact with the GUI:
   - Enter the text and shift value (key).
   - Click "Encrypt" or "Decrypt" to process the text.
   - View the results in the "Result" section.

## How It Works

The Caesar Cipher technique shifts each letter in the plaintext by a certain number of positions (defined by the shift key) in the alphabet. For decryption, the text is shifted back by the same key.

## File Structure

- `main.py`: The command-line interface version of the application.
- `main_2.py`: The graphical user interface version of the application.
- `README.md`: Documentation for the project.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Any enhancements or bug fixes are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

