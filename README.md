## 📚 `library.py` Readme

This Python script simulates a simple, text-based library interface, allowing a user to "access" information about a few pre-defined "books."

-----

### ✨ Features

  * **Welcome Message:** Greets the user upon startup.
  * **Interactive Menu:** Provides options to continue or exit the application.
  * **Book Access:** Allows the user to select one of three books to view its description.
  * **Pre-defined Books:** Includes descriptions for "math," "hindi," and "java."
  * **Exit Function:** A function to gracefully terminate the script.

-----

### 🚀 Getting Started

#### Prerequisites

To run this script, you need a local installation of **Python 3**.

#### Execution

1.  Save the provided code as a file named `library.py`.

2.  Open your terminal or command prompt.

3.  Navigate to the directory where you saved the file.

4.  Run the script using the following command:

    ```bash
    python library.py
    ```

-----

### 📖 Usage

1.  The script will start and prompt you with:
    ```
    Welcome user!!!
    press 1 to continue
    press 2 to exit
    enter your choice :
    ```
2.  **To proceed**, enter `1`. **To quit**, enter `2`.
3.  After choosing to continue, you will be prompted to select a book:
    ```
    which book do you want to acess :
    ```
4.  Enter the corresponding **number** for the book you want to access:
      * Enter **`3`** for the **math** book.
      * Enter **`4`** for the **hindi** book.
      * Enter **`5`** for the **java** book.
5.  The script will display a short and a long description for the chosen book.
6.  The menu will appear again, allowing you to choose to continue (which will prompt you for a book choice again) or exit.

-----

### 💻 Code Overview

The script is structured with a main function and conditional logic:

  * **`run()` function:** Handles the initial menu loop for continuing or exiting the program. It returns `True` if the user chooses to continue.
  * **Book Selection:** The variable `book` captures user input for the desired book.
  * **Conditional Descriptions:** A series of `if/elif` statements check the value of `book` (`"3"`, `"4"`, or `"5"`) to print the specific title and description for "math," "hindi," or "java," respectively.
      * *Note: There is a slight redundancy in the book title prints (e.g., if `book == "3"` prints "here's is your math book," and then the `elif` block for `book == "3"` prints the description). The second `run()` call allows the user to repeat the process.*

-----

### 🛠️ Known Issues / Limitations

  * The book names (`"math"`, `"hindi"`, `"java"`) are not used in the input prompt; the user must enter the corresponding **number** (`"3"`, `"4"`, or `"5"`).
  * The input validation is minimal: entering a non-integer for the initial choice or any value other than `"3"`, `"4"`, or `"5"` for the book choice may cause unexpected behavior or simply exit the book selection without showing a description.
  * The book index names in `book_no` (`("math", "hindi", "java")`) are unused in the main logic.
