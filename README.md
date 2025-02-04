# GeoScope

GeoScope is a Python-based application designed to offer a secure browsing environment by isolating internet activities from the rest of the Windows system. It achieves this by running a local HTTP server and opening URLs in an isolated subprocess environment.

## Features

- **Secure Browsing**: Isolates browsing activities from other system processes.
- **Local Server**: Utilizes a local HTTP server to serve web pages securely.
- **Port Configurability**: Allows configuration of the port to run the local server.

## Requirements

- Python 3.x
- A modern web browser
- Windows OS

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/geoscope.git
    cd geoscope
    ```

2. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

## Usage

1. Place the HTML files you wish to serve in the same directory as `geoscope.py`.

2. Run the program:

    ```bash
    python geoscope.py
    ```

3. The application will start a local server and open the specified HTML file in your default web browser.

## Security Notes

- GeoScope is intended to provide a layer of isolation for safe browsing but should not be considered a substitute for comprehensive security measures.
- Always ensure your system and Python environment are up-to-date with the latest security patches.

## Contributing

Contributions are welcome! Please submit a pull request or create an issue to discuss improvements or features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please contact [your-email@example.com](mailto:your-email@example.com).
```

Note: The provided code is a basic implementation and may not fully isolate the browsing environment as intended. Further enhancements and security measures are required for production use.