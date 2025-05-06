import streamlit as st
import pandas as pd
import random

# Page Configuration
st.set_page_config(page_title="🎓 Student Data Generator", layout="wide")

# Title with emoji and style
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📄 Student CSV File Generator</h1>", unsafe_allow_html=True)
st.markdown("### Generate a random list of student records and download them as a CSV file.")

# Name List
names = ["Ahmed", "Ali", "Asif", "Ghuffran", "Furqan", "Hassan", "Aman", "Fiza", "Saman", 
         "Usman", "Bilal", "Umer", "Shaheer", "Mair", "Moosa", "Sahar", "Rabia", "Manal", "Subhan"]

# Generate Random Student Data
students = []
for i in range(1, 130):
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(18, 25),
        "Grade": random.choice(["A", "B", "C", "D", "E", "F"]),
        "Marks": random.randint(40, 100)
    }
    students.append(student)

df = pd.DataFrame(students)

# Display Subheader and Dataframe
st.markdown("---")
st.subheader("👨‍🎓 Generated Student Data")
st.dataframe(df, use_container_width=True)

# CSV Download Button
csv_file = df.to_csv(index=False).encode('utf-8')
st.markdown("### 📥 Download the file below:")
st.download_button("📁 Download CSV File", csv_file, "student.csv", "text/csv")

# Success Message
st.success("✅ Students Record Generated Successfully!")
