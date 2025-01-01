### README: Car Number Plate Recognition System

---

#### **Project Overview**
This project is a car number plate recognition system developed using Python, PHP, and MySQL. It leverages Haar Cascade classifiers for detecting car number plates, processes the information, and integrates with a database to manage car details. The system supports automatic retrieval of registered car information, new car registration, and a monthly pass feature.

---

#### **Features**
- **Automatic Detection:**
  - Detects car number plates using Haar Cascade files and OpenCV.
  - Automatically fetches details of registered cars from the database.

- **New Car Registration:**
  - Allows new cars to register themselves directly into the system.

- **Monthly Pass Management:**
  - Offers a feature for car owners to subscribe to a monthly pass.

- **Database Integration:**
  - Uses PHP and MySQL for seamless backend connectivity and data storage.

---

#### **Technologies Used**
- **Programming Languages:** Python, PHP
- **Database:** MySQL
- **Libraries/Frameworks:** OpenCV, Haar Cascade
- **Other Tools:** XAMPP or any PHP server environment

---

#### **System Requirements**
- Python 3.x
- PHP 7.x or higher
- MySQL 5.x or higher
- Required Python Libraries: OpenCV, NumPy
- A local or hosted server environment (e.g., XAMPP, WAMP)

---

#### **Setup Instructions**
1. **Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Set Up the Database:**
   - Import the provided SQL file (`database.sql`) into your MySQL server.
   - Update the database credentials in the PHP connection file.

3. **Install Python Dependencies:**
   ```bash
   pip install opencv-python numpy
   ```

4. **Run the Application:**
   - Start the PHP server.
   - Execute the Python script for number plate recognition.
   - Access the interface through the server URL.

---

#### **Usage**
- Run the Python script to start detecting car number plates.
- The system will fetch the car details if the number is registered.
- For new registrations, use the registration interface.
- Manage monthly passes directly from the system.

---

#### **Future Enhancements**
- Integration with cloud-based databases.
- Support for multiple languages.
- Enhanced detection using deep learning models like YOLO.

---

#### **Contributors**
- [Your Name]  
- [Your Team/Organization]  

---

Feel free to contribute to this project or provide feedback to enhance its functionality!
