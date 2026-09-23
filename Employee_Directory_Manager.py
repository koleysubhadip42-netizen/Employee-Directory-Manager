import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Employee Directory Manager",
    page_icon="👨‍💼",
    layout="wide"
)

# Initialize Session State for maintaining employee directory across interactions
if 'employee_directory' not in st.session_state:
    st.session_state.employee_directory = {
        'E101': ('Subhadip Koley', 'Software Engineer', '06/06/2006', '27/08/2020', '50k'),
        'E102': ('Rahul Podder', 'Machine Learning Engineer', '17/11/2005', '06/05/2017', '90k'),
        'E103': ('Surya Samanta', 'Information Technology', '27/12/2006', '12/11/2023', '30k'),
        'E104': ('Sudipta Das', 'AI Engineer', '22/12/2005', '30/06/2022', '40k')
    }

directory = st.session_state.employee_directory

# Sidebar Menu
st.sidebar.title("Directory Menu")
choice = st.sidebar.radio(
    "Choose Action:",
    (
        "View All Employees",
        "Add Employee",
        "Search Employee",
        "Update Employee",
        "Delete Employee"
    )
)

st.title("👨‍💼 Employee Directory Manager")
st.markdown("---")

# 1. View All Employees (Read)
if choice == "View All Employees":
    st.subheader(" All Employee Records")
    if not directory:
        st.info("Directory is empty.")
    else:
        # Convert dictionary to table format for display
        data = []
        for emp_id, details in directory.items():
            data.append({
                "Employee ID": emp_id,
                "Name": details[0],
                "Role": details[1],
                "Birthdate": details[2],
                "Joining Date": details[3],
                "Salary": details[4]
            })
        st.table(data)

# 2. Add Employee (Create)
elif choice == "Add Employee":
    st.subheader("Add New Employee")
    with st.form("add_form"):
        emp_id = st.input_id = st.text_input("Enter Employee ID (e.g., E105)").strip()
        name = st.text_input("Enter Employee Name").strip()
        role = st.text_input("Enter Role/Designation").strip()
        dob = st.text_input("Enter Birthdate (DD-MM-YYYY)").strip()
        doj = st.text_input("Enter Joining Date (DD-MM-YYYY)").strip()
        salary = st.text_input("Enter Salary").strip()
        
        submitted = st.form_submit_button("Add Employee")
        if submitted:
            if not emp_id or not name:
                st.error("Error: Employee ID and Name cannot be empty!")
            elif emp_id in directory:
                st.error(f"Error: Employee ID '{emp_id}' already exists!")
            else:
                directory[emp_id] = (name, role, dob, doj, salary)
                st.success(f"Success: Employee {name} added successfully!")

# 3. Search Employee by ID (Read)
elif choice == "Search Employee":
    st.subheader(" Search Employee Record")
    search_id = st.text_input("Enter Employee ID to search:").strip()
    if st.button("Search"):
        if search_id in directory:
            name, role, dob, doj, salary = directory[search_id]
            st.success(f"Record Found for ID: {search_id}")
            st.markdown(f"""
            - **Name:** {name}
            - **Role:** {role}
            - **Birthdate:** {dob}
            - **Joining Date:** {doj}
            - **Salary:** {salary}
            """)
        else:
            st.error("Error: Employee ID not found.")

# 4. Update Employee (Update)
elif choice == "Update Employee":
    st.subheader(" Update Employee Record")
    update_id = st.text_input("Enter Employee ID to Update:").strip()
    
    if update_id:
        if update_id not in directory:
            st.error('Error: Enter a Valid Employee ID')
        else:
            curr_name, curr_role, curr_dob, curr_doj, curr_salary = directory[update_id]
            st.info(f"Updating Record for ID: {update_id}")
            
            with st.form("update_form"):
                name = st.text_input(f"New Name", value=curr_name).strip()
                role = st.text_input(f"New Role", value=curr_role).strip()
                dob = st.text_input(f"New Birthdate", value=curr_dob).strip()
                doj = st.text_input(f"New Joining Date", value=curr_doj).strip()
                salary = st.text_input(f"New Salary", value=curr_salary).strip()
                
                update_submitted = st.form_submit_button("Update Employee")
                if update_submitted:
                    directory[update_id] = (name, role, dob, doj, salary)
                    st.success('Success: Employee Updated Successfully!')

# 5. Delete Employee (Delete)
elif choice == "Delete Employee":
    st.subheader(" Delete Employee Record")
    delete_id = st.text_input("Enter Employee ID to Delete:").strip()
    
    if st.button("Delete"):
        if delete_id in directory:
            deleted_emp = directory.pop(delete_id)
            st.success(f"Success: Employee {deleted_emp[0]} removed from your directory!")
        else:
            st.error('Error: Employee not found in your directory')
