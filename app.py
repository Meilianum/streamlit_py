
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Set up the app configuration with icon
st.set_page_config(page_title="Data Sweeper", layout='wide', 
                   page_icon="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq-3U9WNUn2cV4pq3orOtb6L-A3nLVqJ31zQ&s")  # Using URL for the icon
# Alternatively, you can use a local file like this:
# st.set_page_config(page_title="Data Sweeper", layout='wide', page_icon="images/icon.png")

st.title(" Data Sweaper")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRq-3U9WNUn2cV4pq3orOtb6L-A3nLVqJ31zQ&s")
st.write("Transform your file between CSV and Excel format with built-in data cleaning & visualization.")

# File uploader
Upload_files = st.file_uploader("Upload your files (CSV, Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if Upload_files:
    for file in Upload_files:
        file_ext = os.path.splitext(file.name)[-1].lower()  # Correct file extension handling

        # Read the file based on its extension
        if file_ext == ".csv":
            df = pd.read_csv(file)  # Corrected the method name to read_csv
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)  # Corrected the method name to read_excel
        else:
            st.error(f"Unsupported file type: {file_ext}")
            continue  # Skip unsupported files

        # Display info about the file
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {file.size / 1024:.2f} KB")
        st.write("Preview of the DataFrame:")
        st.dataframe(df.head())

        # Data cleaning options
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQjvc_JjPjNct_BQCxzn7DKFXkrOroEWORH-Q&s")
        st.subheader("Data Cleaning Options")

        # Option to clean data
        if st.checkbox(f"Clean Data for {file.name}"):

            # Create two columns using st.columns()
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)  # Remove duplicates from the dataframe
                    st.write("Duplicates removed!")

            with col2:
                if st.button(f"Fix missing values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns  # Select numeric columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())  # Fill missing values with mean
                    st.write("Missing values have been filled!")
           
    
        st.subheader("Select Columns to Convert")
        
        columns = st.multiselect(f"Choose columns for {file.name}", df.columns, default=df.columns)  # Fixed the syntax here
        df = df[columns]  # Filter the dataframe to only include the selected columns
       
        # Create some visualization
         
        st.subheader("Data Visualization")
       
        if st.checkbox(f"Show visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:, :2])  # Plot the first two numeric columns

        # Convert the file (CSV or Excel)
        st.image("data:image/jpeg;base64,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")
        st.subheader("Convert Option")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")  # Corrected file extension
                mime_type = "text/csv"
                buffer.seek(0)
            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")  # Corrected file extension
                mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                buffer.seek(0)

            # Download button
            st.download_button(
                label=f"Download {file.name} as {conversion_type}",
                data=buffer,
                file_name=file_name,
                mime=mime_type
            )

        st.success("All files processed!")

        # Image to add to the Streamlit app with responsive container width
     
        st.success("Thanks for watching")