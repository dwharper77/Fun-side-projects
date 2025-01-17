import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
import openpyxl
import xlrd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CallTestKPIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Call Test and KPI Tool")
        self.root.configure(bg="black")
        self.root.geometry("1200x600")  # Adjusts the window size to accommodate the third console window
        
        self.start_button = tk.Button(root, text="Click here to begin", command=self.start_process, bg="black", fg="light green")
        self.start_button.pack(pady=10)
        
        self.dropdown_label = tk.Label(root, text="Select Sector/Timestamp Combo:", bg="black", fg="light green")
        self.dropdown_label.pack(pady=5)
        
        self.combo_var = tk.StringVar()
        self.combo_dropdown = ttk.Combobox(root, textvariable=self.combo_var)
        self.combo_dropdown.pack(pady=5)
        self.combo_dropdown.bind("<<ComboboxSelected>>", self.display_info)  # Bind the selection event to display_info
        
        # Creates a frame for the radio buttons under the first combo box
        self.radio_buttons_frame = tk.Frame(root, bg="black")
        self.radio_buttons_frame.pack(fill=tk.X, pady=10)
        
        # Creates radio buttons for selecting sections to display
        self.section_var = tk.StringVar(value="Accessibility")
        
        # Defines KPI sections
        sections = ["Accessibility", "Retainability", "Traffic", "Mobility"]
        
        for section in sections:
            radio_button = tk.Radiobutton(self.radio_buttons_frame, text=section, variable=self.section_var, value=section,
                                          bg="black", fg="light green", selectcolor="black",
                                          command=self.update_section_info)
            radio_button.pack(side=tk.LEFT, padx=5)

        # Defines the size of the left console window
        self.info_console = tk.Text(root, bg="black", fg="light green", insertbackground="light green", height=8, width=56)  # Reduced by 20%
        self.info_console.pack(expand=True, fill='both', side=tk.LEFT)
        
        # Defines the size of the right console window
        self.section_console = tk.Text(root, bg="black", fg="light green", insertbackground="light green", height=8, width=56)  # Reduced by 20%
        self.section_console.pack(expand=True, fill='both', side=tk.LEFT)

        # Creates a frame for the bottom controls (second dropdown and button)
        self.bottom_controls_frame = tk.Frame(root, bg="black")
        self.bottom_controls_frame.pack(fill=tk.X, pady=10)
        
        # Creates a dropdown menu for selecting columns to plot
        self.plot_column_var = tk.StringVar()
        self.plot_column_dropdown = ttk.Combobox(self.bottom_controls_frame, textvariable=self.plot_column_var)
        self.plot_column_dropdown.pack(side=tk.LEFT, padx=5)
        
        # Button to plot the selected column
        self.plot_button = tk.Button(self.bottom_controls_frame, text="Plot 5-Day Trend", command=self.plot_trend, bg="black", fg="light green")
        self.plot_button.pack(side=tk.LEFT, padx=5)
        

    def start_process(self):
        try:
            # Prompt user to Open Quantum KPI info
            quantum_info_file = filedialog.askopenfilename(title="Open Quantum Info.xlsx", filetypes=[("Excel files", "*.xlsx")])
            if not quantum_info_file:
                raise FileNotFoundError("No Quantum Info file selected.")
            # Prompt user to open PSAP SIM info
            psap_sim_file = filedialog.askopenfilename(title="Open PSAP Sim.xls", filetypes=[("Excel files", "*.xls")])
            if not psap_sim_file:
                raise FileNotFoundError("No PSAP Sim file selected.")
            
            # Load the Quantum Info.xlsx file with headers in the second row (index 1)
            quantum_info = pd.read_excel(quantum_info_file, sheet_name='Combined Data', engine='openpyxl', header=[1])

            # Rename 'Unnamed' columns to their correct names
            quantum_info.columns = [col if 'Unnamed' not in col else 'Time' for col in quantum_info.columns]

            # Rename the second 'Time' column to avoid duplication
            if quantum_info.columns.duplicated().any():
                quantum_info.columns = [f"{col}_2" if col == 'Time' and i > 0 else col for i, col in enumerate(quantum_info.columns)]

            # Load the PSAP Sim.xls file
            psap_sim = pd.read_excel(psap_sim_file, sheet_name='raptor', engine='xlrd')

            # Parse the 'Time' column in the Quantum file to extract the date and hour
            quantum_info['DateHour'] = pd.to_datetime(quantum_info['Time']).dt.strftime('%Y-%m-%d %H')

            # Convert the detailed timestamp in the PSAP Sim file to match the date and hour format of the Quantum file
            psap_sim['DateHour'] = pd.to_datetime(psap_sim['Call Timestamp'], format='%d-%b-%y %I:%M:%S %p %Z').dt.strftime('%Y-%m-%d %H')

            # Ensure the AD column is treated as a separate column without a header
            quantum_info['SectorID'] = quantum_info.iloc[:, 29]  # Assuming AD is the 30th column (0-indexed)

            # Merge the data from the PSAP Sim file with the corresponding Sector ID in the Quantum file
            merged_data = pd.merge(psap_sim, quantum_info, left_on='Setup UTRAN Cell ID', right_on='SectorID', how='inner')

            # Further merge the data based on the timestamp
            final_combined_data = merged_data[merged_data['DateHour_x'] == merged_data['DateHour_y']]

            # Remove duplicate columns after merging
            final_combined_data = final_combined_data.loc[:, ~final_combined_data.columns.duplicated()]

            # Save the combined data to a new Excel file
            final_combined_data.to_excel('Combined_Data.xlsx', index=False)

            # Update dropdown menu with unique Setup UTRAN Cell ID/Call Timestamp combos
            unique_combos = final_combined_data[['Setup UTRAN Cell ID', 'Call Timestamp']].drop_duplicates()
            unique_combos['Combo'] = unique_combos['Setup UTRAN Cell ID'].astype(str) + ' / ' + unique_combos['Call Timestamp'].astype(str)
            
            self.combo_dropdown['values'] = unique_combos['Combo'].tolist()
            self.combo_dropdown.current(0)  # Set default to the first option
            
            # Store final combined data for later use
            self.final_combined_data = final_combined_data
            
            # Update plot column dropdown with column headers from Quantum Info DataFrame (excluding 'Time' and 'SectorID')
            plot_columns = [col for col in quantum_info.columns if col not in ['Time', 'SectorID']]
            self.plot_column_dropdown['values'] = plot_columns
            self.plot_column_dropdown.current(0)  # Set default to the first option
            
            messagebox.showinfo("Success", "Data combined successfully and saved to Combined_Data.xlsx")

            # Store quantum info data for secondary option use
            self.quantum_info = quantum_info

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def display_info(self, event=None):
        selected_combo = self.combo_var.get()
        
        if not selected_combo:
            messagebox.showwarning("No Combo Selected", "Please select a combo from the dropdown menu.")
            return
        
        setup_utran_cell_id, call_timestamp = selected_combo.split(' / ')
        
        filtered_data = self.final_combined_data[
            (self.final_combined_data['Setup UTRAN Cell ID'].astype(str) == setup_utran_cell_id) &
            (self.final_combined_data['Call Timestamp'].astype(str) == call_timestamp)
        ]
        
        display_text = ""
        
        # Define the columns to display
        columns_to_display = ['Call Timestamp', 'Validation_Results', 'Class Of Service Met?', 'Distance to serving sector Validated ', 'Radius/Distance (meters)', 'POS Method Used', 'Uncertainity (meters)', 'Confidence Code']
        
        for col in columns_to_display:
            if col in filtered_data.columns:
                display_text += f"{col}: {filtered_data[col].values[0]}\n"
            else:
                display_text += f"{col}: Column not found\n"
        
        self.info_console.delete(1.0, tk.END)
        self.info_console.insert(tk.END, display_text)
        
        # Update section info based on selected section
        self.update_section_info()

    def update_section_info(self):
        section = self.section_var.get()
        selected_combo = self.combo_var.get()
        
        if not selected_combo:
            messagebox.showwarning("No Combo Selected", "Please select a combo from the dropdown menu.")
            return
        
        setup_utran_cell_id, _ = selected_combo.split(' / ')
        
        # Filter data to include all rows with the matching first portion of the combo
        filtered_data = self.final_combined_data[self.final_combined_data['Setup UTRAN Cell ID'].astype(str) == setup_utran_cell_id]
        
        # Remove duplicate timestamps
        filtered_data = filtered_data.drop_duplicates(subset=['Call Timestamp'])
        
        if section == "Accessibility":
            columns = list(self.final_combined_data.columns[44:52])
        elif section == "Retainability":
            columns = list(self.final_combined_data.columns[52:58])
        elif section == "Traffic":
            columns = list(self.final_combined_data.columns[59:62])
        elif section == "Mobility":
            columns = list(self.final_combined_data.columns[63:70])
        
        section_text = ""
        for index, row in filtered_data.iterrows():
            section_text += f"Timestamp: {row['Call Timestamp']}\n"
            for col in columns:
                section_text += f"{col}: {row[col]}\n"
            section_text += "\n"
        
        self.section_console.delete(1.0, tk.END)
        self.section_console.insert(tk.END, section_text)



    def plot_trend(self):
        selected_column = self.plot_column_var.get()
        
        if not selected_column:
            messagebox.showwarning("No Column Selected", "Please select a column from the dropdown menu.")
            return
        
        # Ensure 'Time' column exists in the DataFrame
        if 'Time' not in self.quantum_info.columns:
            messagebox.showerror("Error", "'Time' column not found in the data.")
            return
        
        # Extract the sector info from the selected combo option
        selected_combo = self.combo_var.get()
        if not selected_combo:
            messagebox.showwarning("No Combo Selected", "Please select a combo from the dropdown menu.")
            return
        
        setup_utran_cell_id, call_timestamp = selected_combo.split(' / ')
        
        # Filter the quantum_info DataFrame to include only rows with the matching sector info
        sector_info = self.quantum_info[self.quantum_info['SectorID'] == setup_utran_cell_id]
        
        # Extract the last 5 days of data for the selected sector
        last_5_days_data = sector_info[['Time', selected_column]].replace('-', pd.NA).dropna()
        
        if last_5_days_data.empty:
            messagebox.showwarning("No Data", "No data available for the selected column.")
            print("Empty DataFrame after initial processing")
            print(last_5_days_data)
            return
        
        # Convert the selected column to numeric, forcing errors to NaN
        last_5_days_data[selected_column] = pd.to_numeric(last_5_days_data[selected_column], errors='coerce')
        
        # Drop rows with NaN values in the selected column
        last_5_days_data = last_5_days_data.dropna(subset=[selected_column])
        
        # Log the data to verify conversion
        print("Data after conversion to numeric and dropping NaNs")
        print(last_5_days_data)
        
        # Extract the last 5 days of data
        last_5_days_data['Date'] = pd.to_datetime(last_5_days_data['Time']).dt.date
        last_5_days_data['Hour'] = pd.to_datetime(last_5_days_data['Time']).dt.hour
        last_5_days = last_5_days_data[last_5_days_data['Date'] >= (last_5_days_data['Date'].max() - pd.Timedelta(days=4))]
        
        # Filter to include only hours 3, 11, and 19
        filtered_hours = [3, 11, 19]
        last_5_days = last_5_days[last_5_days['Hour'].isin(filtered_hours)]
        
        # Add this print statement to inspect the filtered data
        print("Filtered data for the last 5 days and selected hours:")
        print(last_5_days)  # Add this line 
        
        # Determine the y-axis limit based on the data type
        y_max = last_5_days[selected_column].max()
        if pd.isna(y_max) or np.isinf(y_max):
            messagebox.showerror("Error", "Axis limits cannot be NaN or Inf")
            print("Axis limits cannot be NaN or Inf")  # Log error in IDE
            return
        
        if y_max <= 1:
            y_max = 1  # Percentage data
        else:
            y_max = y_max * 1.1  # Scale slightly above the max value
        
        # Plot the data as line graph with black background and lighter colors for lines and font
        fig, ax = plt.subplots(figsize=(15, 6))  # Adjust figsize for a wider graph
        
        fig.patch.set_facecolor('black')
        ax.set_facecolor('black')
        
        # Sort the data by Date and Hour to ensure correct plotting order
        last_5_days = last_5_days.sort_values(by=['Date', 'Hour'])
        
        # Create a list of x-tick positions and labels for hours only
        tick_positions = []
        tick_labels = []
        
        for i, (date, group) in enumerate(last_5_days.groupby('Date')):
            for hour in filtered_hours:
                tick_positions.append(i * len(filtered_hours) + filtered_hours.index(hour))
                tick_labels.append(f'{hour}:00')
        
        # Plot the data as line graph with lighter colors for lines and font
        ax.plot(tick_positions[:len(last_5_days)], last_5_days[selected_column].values[:len(tick_positions)], marker='o', color='lightgreen')
        
        ax.set_xlabel('Hour of Day', color='lightgreen')
        ax.set_ylabel(selected_column, color='lightgreen')
        ax.set_title(f'5-Day Trend for {selected_column}', color='lightgreen')
        ax.set_ylim(0, y_max)
        
        # Set x-ticks and labels for hours only with lighter colors for font
        ax.set_xticks(tick_positions[:len(last_5_days)])
        ax.set_xticklabels(tick_labels[:len(last_5_days)], rotation=0, ha='center', color='lightgreen')
        
        # Set y-ticks with lighter colors for font
        ax.tick_params(axis='y', colors='lightgreen')
        
        # Add vertical lines and labels for each day with lighter colors for lines and font
        for i, date in enumerate(sorted(last_5_days['Date'].unique())):
            ax.axvline(x=i * len(filtered_hours), color='gray', linestyle='--')
            ax.text(i * len(filtered_hours), y_max * 1.05, str(date), rotation=0, ha='center', va='bottom', color='lightgreen')
        
        # Display the plot in a new window or update existing plot window
        if hasattr(self, 'plot_window') and self.plot_window.winfo_exists():
            self.plot_window.destroy()
            
        self.plot_window = tk.Toplevel(self.root)
        self.plot_window.title(f'5-Day Trend for {selected_column}')
        
        canvas = FigureCanvasTkAgg(fig, master=self.plot_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    
    
if __name__ == "__main__":
    root = tk.Tk()
    app = CallTestKPIApp(root)
    root.mainloop()
