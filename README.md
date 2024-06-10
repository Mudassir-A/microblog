# **MicroBlog**

This is a Python Flask web application for creating and managing a microblog. It leverages MongoDB for data storage and utilizes the PyMongo library for database interaction. Flask serves as the web framework, providing a robust foundation for the application.

## **Features:**

- **Create New Blogs:** Users can add new articles to their microblog.
- **Display Recent Blogs:** The application displays a list of recent blog entries with their creation dates.

## **Technologies:**

- Python
- Flask (web framework)
- PyMongo (MongoDB interaction)
- Flask-dotenv (environment variable management)

## **Installation:**

### 1. **Prerequisites:**
   - Ensure you have Python (>=3.7) and pip (package installer) installed. Install them if necessary.
   - Download and install MongoDB from their official website: [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)

### 2. **Clone the Repository:**
   ```bash
   git clone https://github.com/Mudassir-A/microblog.git
   cd microblog
   ```

### 3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### 4. **Environment Setup:**
   - Create a file named `.env` in the project's root directory.
   - Add the following lines to `.env`, replacing placeholders with your actual values:

     ```
     MONGODB_URI=mongodb://localhost:27017/microblog  # Replace with your MongoDB connection string
     ```

   - Create another file named `.flaskenv` for development-specific configurations (optional):

     ```
     FLASK_ENV=development  # Or 'production' for live deployment
     ```

## **Running the Application:**

### 1. **Development Mode:**
   ```bash
   source .flaskenv  # Activate the virtual environment (if using)
   flask run
   ```

### 2. **Production Mode (Optional):**
   Set up a production server (e.g., Gunicorn, uWSGI) and configure it to use the application instance and environment variables. Refer to Flask documentation for details.

## **Usage:**

1. Open `http://127.0.0.1:5000/` (or the appropriate URL for your server) in your web browser.
2. Create new blog entries (implementation details will depend on your specific design choices).
3. The application will display a list of recently created blogs with their respective dates.

## **Additional Notes:**

- This README provides a general structure. You'll likely need to modify it based on your project's specific implementation.
- Consider including more detailed instructions for users (e.g., how to create new blog entries, using forms, etc.).
- You can enhance the project by adding features like user authentication, image/video uploads, comments, and more.
- For production deployment, refer to Flask and MongoDB documentation on best practices for security, scalability, and monitoring.
