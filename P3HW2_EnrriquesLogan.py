# Logan Enrriques
# P3HW2
# 10/5/2026
# Calculate employees weekly paycheck, including if they worked overtime

import streamlit as st

# Make a title on our Ui
st.title("Weekly Paycheck Calculator")

# Get employee name
name = st.text_input("Enter employee name:")

# Get number of hours worked
hours_worked = st.number_input("Enter hours worked for on week:")

# Get regular pay rate
reg_pay_rate = st.number_input("Enter base pay rate:")

# If statement for HAVING OVERTIME
if hours_worked > 40:

    OT_hours = hours_worked - 40
    OT_pay = OT_hours * (reg_pay_rate * 1.5)
    reg_pay = reg_pay_rate * 40
    gross_pay = OT_pay + reg_pay
    
else:
    OT_hours = 0
    OT_pay = 0
    reg_pay = hours_worked * reg_pay_rate
    gross_pay = OT_pay + reg_pay

# Display results
st.write(f"Employee name: {name}")
st.write()
st.write(f"Hours Worked: {hours_worked}")
st.write(f"Pay Rate: $: {reg_pay_rate:.2f}")
st.write(f"Overtime Hours: {OT_hours:.2f}")
st.write(f"Overtime Pay: ${OT_pay:.2f}")
st.write(f"RegHour Pay: ${reg_pay:.2f}")
st.write(f"Gross Pay: ${gross_pay:.2f}")