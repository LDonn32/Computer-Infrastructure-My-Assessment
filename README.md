# Computer-Infrastructure-My-Assessment
My assessment for the module Computer Infrastructure for the HDip of Data Analytics in ATU Galway Mayo. Winter 2025/2026. 

# Contact Details.

Author: Laura Donnelly.

Student ID: G00472977.

Email: G00472977@atu.ie.

# Setting up environment.

Use bash in the terminal to follow the below steps.

``git clone https://github.com/LDonn32/Computer-Infrastructure-My-Assessment.git``

``cd Computer-Infrastructure-My-Assessment``

Install packages, most noteably yFinance.

``pip install -r requirements.txt``

Create directories for the data and the plots.

``mkdir -p data plots``

See [www.geeksforgeeks.org](https://www.geeksforgeeks.org/linux-unix/mkdir-command-in-linux-with-examples/) for more details on the mkdir command.

Making the script from Assignment 3 executable.

``chmod a+x faang.py``

This allows the script to be run directly from the terminal.

Run the script.

``./faang.py``

This downloaded the FAANG stock data using YFinance. It saves a timestamped CSV file in the data folder and creates and saves a plot in the plots folder.


For assignment 4 and running GitHub Actions take the below steps to enable the workflow:

- Clone the repository.

- Ensure Actions are enabled in the GitHub repository settings.

- Push to the main branch.

The workflow file is found at: 
.github/workflows/faang.yml
