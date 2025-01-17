# Call Test and KPI Tool

This tool is designed to automate the process of analyzing call test data and Key Performance Indicators (KPIs) using a graphical user interface (GUI) built with Tkinter.

## Features
- **Graphical User Interface**: Built with Tkinter to provide an intuitive and interactive experience.
- **Data Processing**: Utilizes pandas for efficient data manipulation and openpyxl/xlrd for handling Excel files.
- **File Selection**: Allows users to select Quantum Info and PSAP Sim files through a file dialog.
- **Detailed Information Display**: Shows detailed information based on selected sector/timestamp combinations.
- **KPI Sections**: Provides options to view different KPI sections: Accessibility, Retainability, Traffic, and Mobility.
- **Trend Plotting**: Plots a 5-day trend for selected columns using Matplotlib.
- **Console Logging**: Displays information and KPI details in Tkinter text widgets for easy viewing.
- **Error Handling**: Displays error messages using messagebox for better user experience.
- **Output**: Saves combined data to a new Excel file for further analysis.

## Requirements

- Python 3.x
- NumPy
- Tkinter
- Pandas
- Openpyxl
- xlrd
- Matplotlib

## Usage

1. Run the script:
    ```sh
    python PSAP_SIM_KPI_Tool.py
    ```
2. The GUI will open. Click the "Click here to begin" button to start the process.

3. Select the Quantum Info and PSAP Sim Excel files when prompted.

4. The tool combines the PSAP SIM and KPI data

5. Use the radials to choose which Group of KPIs to view

4. Use the dropdown menu to select a sector/timestamp combination.

5. View detailed information and KPI sections in the console windows.

6. Use the second dropdown menu to select which KPI to view then click "Plot 5-Day Trend" to visualize the data.
    !Step 6

## Code
The source code is available in this repository for reference. While the code may not be fully functional without the necessary data, it provides insight into the tool's implementation.

## Contact
For any questions or issues, please contact:
- **Name**: Dennis Harper
- **Email**: dwharper77@gmail.com