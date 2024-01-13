# Flask Admin Dashboard for E-Learning Questions Management

This Flask project is an Admin Dashboard designed to efficiently manage questions for an E-Learning website. The frontend is built using Bootstrap, and the backend leverages Flask. Dynamic content is seamlessly updated through AJAX, enhancing user experience and optimizing resource utilization. MongoDB is used as the database to store and manage data.

## Features

- **Bootstrap Frontend**: A responsive and user-friendly frontend built on Bootstrap for easy navigation and a modern look.
  
- **Flask Backend**: Utilizes the Flask framework to handle server-side operations and interact with the MongoDB database.

- **AJAX Integration**: Dynamically updates content without reloading the entire page, providing a smoother user experience.

- **MongoDB Database**: Manages and stores data efficiently in a MongoDB database.

## Getting Started

1. **Prerequisites**:

    - Make sure you have Python installed on your system.

    - Install Flask and required dependencies:

        ```bash
        pip install -r requirements.txt
        ```

    - Install MongoDB and start the MongoDB service.

2. **Configuration**:

    - Open `app.py` and add your MongoDB connection details:

        ```python
        app.config["MONGODB_SETTINGS"] = {
            "host": "mongodb://localhost:27017/your_database_name",
        }
        ```

3. **Run the App**:

    ```bash
    python app.py
    ```

    The app will be accessible at `http://localhost:5000`.

## Usage

1. Open the dashboard in your web browser.

2. Navigate through the different sections to manage questions efficiently.

3. Use AJAX-powered features for a seamless user experience.

## Contributing

Contributions are welcome! If you have suggestions, bug reports, or want to contribute new features, please open an issue or a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

For questions or inquiries, feel free to contact the project maintainer:

- Muhammad Nadeem

---

Thank you for using this Flask Admin Dashboard for E-Learning Questions Management. We hope it streamlines your workflow in managing questions effectively.
