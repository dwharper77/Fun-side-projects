# KPI Tool

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
![KPI1](https://github.com/user-attachments/assets/26cfae3f-dca6-4cb5-9f56-5f97d3216c90)

4. Select the Quantum Info and PSAP Sim Excel files when prompted.
![KPI2](https://github.com/user-attachments/assets/d1b49b3e-d514-466c-9a04-e1201016de8f)

5. The tool combines the PSAP SIM and KPI data.
![KPI3](https://github.com/user-attachments/assets/784f881f-13f1-4aa9-aa8d-8f9e0896387d)

6. Use the radials to choose which Group of KPIs to view.

7. Use the dropdown menu to select a sector/timestamp combination.

7 View detailed information and KPI sections in the console windows.
![KPI4](https://github.com/user-attachments/assets/d55ec29a-6bb7-47fe-b7ce-524dbb01ed7e)

8. Use the second dropdown menu to select which KPI to view then click "Plot 5-Day Trend" to visualize the data.
![KPI5](https://github.com/user-attachments/assets/2918cd9e-894f-4deb-8288-b62ed3cacf22)


## Code
The source code is available in this repository for reference. While the code may not be fully functional without the necessary data, it provides insight into the tool's implementation.

## Contact
For any questions or issues, please contact:
- **Name**: Dennis Harper
- **Email**: dwharper77@gmail.com
