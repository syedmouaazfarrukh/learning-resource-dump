import pandas as pd
import requests
import openpyxl

# Initialize an empty list to store DataFrame chunks
dfs = []

# Iterate over offsets
for offset in range(0, 9001, 1000):  # range stops at 10001 to include 10000
    print("Currently at offset:", offset)
    # URL of the data with current offset
    url = f"https://data.edmonton.ca/resource/q7ua-agfg.json?$offset={offset}"
    
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the data from the response
        data = response.json()  # Assuming the response is JSON
        
        # Read the JSON data into a pandas DataFrame
        df_chunk = pd.DataFrame(data)
        
        # Append DataFrame chunk to the list
        dfs.append(df_chunk)
        
    else:
        print(f"Failed to retrieve data for offset {offset}. Status code:", response.status_code)

# Concatenate all DataFrame chunks into a single DataFrame
result_df = pd.concat(dfs, ignore_index=True)

# Now you can work with the combined DataFrame 'result_df'
# print(result_df)  # Display the first few rows of the DataFrame


# Extracting KPI columns
# kpi_columns = ['date_created', 'month']  # Adjust this list to include the names of your KPI columns
# kpi_df = result_df[kpi_columns]

# print(kpi_df)


# Write the DataFrame to an Excel file
# excel_filename = "output.xlsx"
# result_df.to_excel(excel_filename, index=False)

# print(f"DataFrame has been written to {excel_filename}.")