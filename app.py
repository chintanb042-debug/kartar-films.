import streamlit as st
import pandas as pd
import datetime

# 1. Page Configuration & Ultra-Luxury Studio Aesthetics
st.set_page_config(page_title="KARTAR FILMS - Production Engine", layout="wide", page_icon="🎬")

# Luxury Cinema Theme Styling
st.markdown("""
<style>
.stApp {
background: radial-gradient(circle, #16161a 0%, #0a0a0d 100%);
color: #f1ebd9;
font-family: 'Helvetica Neue', Arial, sans-serif;
}
h1, h2, h3, h4 {
color: #d4af37 !important;
font-family: 'Cinzel', 'Georgia', serif;
letter-spacing: 2px;
text-transform: uppercase;
}
[data-testid="stSidebar"] {
background-color: #0e0e12 !important;
border-right: 2px solid #1c1c24;
}
[data-testid="stSidebar"] .stRadio > div {
color: #c5b358 !important;
}
div.stButton > button:first-child {
background: linear-gradient(135deg, #d4af37 0%, #aa7c11 100%) !important;
color: #0a0a0d !important;
font-weight: 700 !important;
letter-spacing: 1.5px;
border-radius: 4px !important;
border: none !important;
box-shadow: 0 4px 15px rgba(212, 175, 55, 0.2);
transition: all 0.3s ease;
padding: 10px 24px !important;
}
div.stButton > button:first-child:hover {
transform: translateY(-2px);
box-shadow: 0 6px 20px rgba(212, 175, 55, 0.4);
color: #ffffff !important;
}
div[data-testid="stFileUploader"] {
background-color: #121216 !important;
border: 1px dashed #d4af37 !important;
border-radius: 8px;
padding: 15px;
}
input, textarea, select {
background-color: #121216 !important;
color: #ffffff !important;
border: 1px solid #2d2d3a !important;
border-radius: 4px !important;
}
input:focus, textarea:focus {
border-color: #d4af37 !important;
}
.luxury-card {
padding: 20px;
background-color: #121216;
border: 1px solid #1c1c24;
border-radius: 6px;
border-left: 4px solid #d4af37;
margin-bottom: 15px;
box-shadow: 0 5px 15px rgba(0,0,0,0.3);
}
</style>
""", unsafe_allow_html=True)

# 2. Initialization of Advanced Production Databases
if "users" not in st.session_state:
    st.session_state.users = {
        "kartar@26": {"name": "Main Admin", "password": "admin", "approved": True, "role": "Admin", "status": "In Executive Suite"}
    }
if "tasks" not in st.session_state: st.session_state.tasks = []
if "script_data" not in st.session_state: st.session_state.script_data = []
if "location_data" not in st.session_state: st.session_state.location_data = []
if "vehicle_data" not in st.session_state: st.session_state.vehicle_data = []
if "food_data" not in st.session_state: st.session_state.food_data = []
if "schedule_data" not in st.session_state: st.session_state.schedule_data = []
if "budget_data" not in st.session_state: st.session_state.budget_data = []
if "crew_cast" not in st.session_state: st.session_state.crew_cast = []
if "equipment" not in st.session_state: st.session_state.equipment = []

if "logged_in_user" not in st.session_state:
    st.session_state.logged_in_user = None

# --- 3. CINEMA THEATER INTRO ---
if "intro_done" not in st.session_state:
    theater_html = """<iframe src="https://assets.mixkit.co/active_storage/sfx/2568/2568-84.wav" allow="autoplay" style="display:none" id="iframeAudio"></iframe><audio autoplay><source src="https://assets.mixkit.co/active_storage/sfx/2568/2568-84.wav" type="audio/wav"></audio><div class="theater-stage"><div class="spotlight"></div><div class="camera-zoom-container"><p class="sub-text">CHINTAN TRIVEDI PRESENTS</p><h1 class="main-cinema-title">KARTAR</h1><h2 class="sub-cinema-title">FILMS</h2><div class="projector-beam"></div></div></div><style>.theater-stage {position: relative;background: radial-gradient(circle at center, #1a0f0f 0%, #050303 100%) !important;height: 55vh;display: flex;flex-direction: column;justify-content: center;align-items: center;overflow: hidden;border: 3px solid #d4af37;border-radius: 12px;box-shadow: 0 15px 35px rgba(0,0,0,0.9);margin-bottom: 25px;}.spotlight {position: absolute;top: 50%;left: 50%;transform: translate(-50%, -50%);width: 400px;height: 400px;background: radial-gradient(circle, rgba(212,175,55,0.15) 0%, rgba(0,0,0,0) 70%);pointer-events: none;}.camera-zoom-container {text-align: center;animation: cameraZoomIn 4s cubic-bezier(0.25, 1, 0.5, 1) forwards;perspective: 1000px;}.sub-text {color: #a8a8af !important;font-family: 'Arial', sans-serif;font-size: 14px;letter-spacing: 8px;margin-bottom: 5px;text-transform: uppercase;}.main-cinema-title {color: #d4af37 !important;font-family: 'Impact', 'Arial Black', sans-serif !important;font-size: 105px !important;font-weight: 900 !important;letter-spacing: 6px !important;margin: 0 !important;line-height: 0.9 !important;text-shadow: 0px 0px 20px rgba(212, 175, 55, 0.6), 0px 10px 30px rgba(0,0,0,0.8);}.sub-cinema-title {color: #f1ebd9 !important;font-family: 'Georgia', serif !important;font-size: 45px !important;font-weight: 300 !important;letter-spacing: 22px !important;margin: 10px 0 0 0 !important;padding-left: 20px;text-transform: uppercase;text-shadow: 0px 5px 15px rgba(0,0,0,0.7);}.projector-beam {position: absolute;top: -100px;left: 50%;transform: translateX(-50%);width: 600px;height: 600px;background: radial-gradient(ellipse at top, rgba(255,255,255,0.03) 0%, rgba(255,255,255,0) 60%);pointer-events: none;}@keyframes cameraZoomIn {0% {transform: scale(0.3) translateZ(-500px);filter: blur(10px);opacity: 0;}50% {filter: blur(2px);opacity: 1;}100% {transform: scale(1) translateZ(0);filter: blur(0px);opacity: 1;}}</style>"""
    st.markdown(theater_html, unsafe_allow_html=True)
    st.write("")
    if st.button("OPEN KARTAR PRODUCTION ENGINE", use_container_width=True):
        st.session_state.intro_done = True
        st.rerun()
    st.stop()

# --- 4. SECURE STUDIO PORTAL LOGIN ---
if st.session_state.logged_in_user is None:
    col1, col2, col3 = st.columns([1, 1.8, 1])
    with col2:
        st.markdown("<h2 style='text-align: center; font-size: 26px;'>🎬 STUDIO EXECUTIVE LOGON</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #8a8a93; font-size:12px; margin-top:-15px; letter-spacing: 3px;'>CHINTAN TRIVEDI ARCHITECTURE</p>", unsafe_allow_html=True)
        st.write("")
        
        tab1, tab2 = st.tabs(["🔒 Executive Access", "📝 Crew Credentials Request"])
        
        with tab1:
            username = st.text_input("Executive Secure ID / Username:")
            password = st.text_input("Passkey:", type="password")
            if st.button("Authenticate & Boot Dashboard", use_container_width=True):
                if username in st.session_state.users:
                    user_info = st.session_state.users[username]
                    if user_info["password"] == password:
                        if user_info["approved"]:
                            st.session_state.logged_in_user = username
                            st.success("Identity Verified. Loading Mainframe...")
                            st.rerun()
                        else: st.error("Access Suspended: Account status set to Unapproved/Rejected.")
                    else: st.error("Authentication Failure: Incorrect Passkey.")
                else: st.error("Identity Record Absent from Server Room.")
                    
        with tab2:
            reg_uid = st.text_input("Requested Unique Studio ID:")
            reg_name = st.text_input("Full Official Name:")
            reg_pass = st.text_input("Assign Secret Passkey:", type="password")
            if st.button("Transmit Credentials to Admin Vault", use_container_width=True):
                if reg_uid and reg_name and reg_pass:
                    st.session_state.users[reg_uid] = {
                        "name": reg_name, "password": reg_pass, "approved": False, "role": "Team", "status": "Awaiting System Induction"
                    }
                    st.success("Transmission Complete. Awaiting System Administrator clearance.")

# --- 5. SYSTEM CONSOLE CORE (AUTHENTICATED SESSIONS) ---
else:
    uid = st.session_state.logged_in_user
    current_user = st.session_state.users[uid]
    
    st.sidebar.markdown("<h2 style='text-align:center; font-size:20px; color:#d4af37;'>KARTAR FILMS</h2>", unsafe_allow_html=True)
    st.sidebar.markdown("<p style='text-align:center; color:#8a8a93; font-size:11px; margin-top:-20px; letter-spacing:4px;'>CHINTAN TRIVEDI</p>", unsafe_allow_html=True)
    st.sidebar.write("---")
    
    modules = [
        "Executive Dashboard", "Script Suite room", "Location Scout Room", 
        "Fleet & Logistics Control", "Catering Allocation", "Master Shooting Schedule", 
        "Capital Expense Spreadsheet", "Talent & Crew Registry", "Hardware Assets Inventory"
    ]
    if current_user["role"] == "Admin":
        modules.insert(1, "🛡️ System Admin Vault")
        
    choice = st.sidebar.radio("CORE COMMAND CHANNELS:", modules)
    
    st.sidebar.write("---")
    with st.sidebar.expander("🔐 Security Protocols"):
        new_pass = st.text_input("Modify My Secret Passkey:", type="password")
        if st.button("Override Passkey"):
            if new_pass:
                st.session_state.users[uid]["password"] = new_pass
                st.success("Passkey record updated successfully.")
                
    if st.sidebar.button("Terminate Session", use_container_width=True):
        st.session_state.logged_in_user = None
        st.rerun()

    # --- MODULE 1: EXECUTIVE DASHBOARD ---
    if choice == "Executive Dashboard":
        st.header("🎛️ Studio Command Dashboard")
        st.subheader("Transmit Live Field Action Status")
        live_stat = st.text_input("Current Operational Focus Vector:", value=current_user["status"])
        if st.button("Broadcast Status Across Grid"):
            st.session_state.users[uid]["status"] = live_stat
            st.success("Operational telemetry broadcasted live.")
            
        st.write("---")
        st.subheader("🟢 Live Network Fleet & Crew Tracking Grid")
        for u, inf in st.session_state.users.items():
            if inf["approved"]:
                st.markdown(f"""
                <div class='luxury-card'>
                    <span style='color:#d4af37; font-weight:bold;'>👤 Profile:</span> {inf['name']} ({u}) | 💼 <strong>Role Assignment:</strong> {inf['role']}<br/>
                    📡 <strong>Live Action Log:</strong> {inf['status']}
                </div>
                """, unsafe_allow_html=True)
                
        st.write("---")
        st.subheader("📋 Enforced Directives & Assigned Tasks")
        my_tasks = [t for t in st.session_state.tasks if t["Assigned Operative"] == uid or current_user["role"] == "Admin"]
        if my_tasks:
            st.table(pd.DataFrame(my_tasks))
        else: st.info("No external operational tasks mapped to your ID profile.")

    # --- MODULE 2: SYSTEM ADMIN VAULT ---
    elif choice == "🛡️ System Admin Vault":
        st.header("🛡️ Supreme System Admin Vault Controls")
        st.subheader("🔑 Registration Clearances Matrix")
        for u, inf in list(st.session_state.users.items()):
            if u != "kartar@26":
                col_a, col_b, col_c = st.columns([2, 1, 1])
                with col_a:
                    st.write(f"*Operator Identity:* {inf['name']} ({u}) | *Status:* {'CLEAR / ACTIVE' if inf['approved'] else 'BLOCKED / PENDING'}")
                with col_b:
                    if not inf["approved"]:
                        if st.button(f"✅ Approve Profile ({u})"):
                            st.session_state.users[u]["approved"] = True
                            st.rerun()
                    else:
                        if st.button(f"🚫 Reject/Suspend ({u})"):
                            st.session_state.users[u]["approved"] = False
                            st.rerun()
                with col_c:
                    if st.button(f"🗑️ Purge From Matrix ({u})"):
                        del st.session_state.users[u]
                        st.rerun()
                        
        st.write("---")
        st.subheader("🎯 Deploy Critical Field Tasks")
        t_title = st.text_input("Mission Operational Directive Label Name:")
        crew_options = [u for u, inf in st.session_state.users.items() if inf["approved"]]
        t_crew = st.selectbox("Select Target Operative:", crew_options)
        t_deadline = st.date_input("Target Execution Window Deadline:")
        if st.button("Deploy Directive File"):
            st.session_state.tasks.append({
                "Directive Objective": t_title, "Assigned Operative": t_crew, "Deadline Window": str(t_deadline), "Enforced By": "Main Admin"
            })
            st.success(f"Directive routed to operative {t_crew} successfully.")

    # --- MODULE 3: SCRIPT SUITE ROOM ---
    elif choice == "Script Suite room":
        st.header("📝 Creative Script Suite Room & Asset Ledger")
        with st.form("script_form"):
            sec = st.selectbox("Script Phase Index Node:", ["Idea Phase", "Plot Core Layout", "Character Matrix Outline", "Script Drafting Pipeline", "Final Locked Master Script"])
            title = st.text_input("Project Phase Sequence Header Title:")
            content = st.text_area("Primary Text Corpus Lines:")
            uploaded_script_file = st.file_uploader("📂 Upload Script Document / Treatment Files (PDF, DOCX, TXT):", type=["pdf", "docx", "txt"])
            
            if st.form_submit_button("Commit Script Vector"):
                file_status = uploaded_script_file.name if uploaded_script_file else "No File Attached"
                st.session_state.script_data.append({
                    "Phase": sec, "Title Header": title, "Script Excerpt": content, "Attached Asset": file_status, "Author Code": uid
                })
                st.success("Creative content logged securely inside the script room matrix.")
        st.write("---")
        st.subheader("🗄️ Locked Creative Script Room Logs")
        if st.session_state.script_data: st.dataframe(pd.DataFrame(st.session_state.script_data), use_container_width=True)

    # --- MODULE 4: LOCATION SCOUT ROOM ---
    elif choice == "Location Scout Room":
        st.header("📍 Tactical Location Scout Recce Controls")
        with st.form("loc_form"):
            l_name = st.text_input("Target Location Spot Code Identifier:")
            l_in = st.time_input("Clock In Entry Timestamp:")
            l_out = st.time_input("Clock Out Exit Timestamp:")
            l_det = st.text_area("Environmental Infrastructure Notes:")
            uploaded_loc_file = st.file_uploader("📂 Upload Location Blueprint Schematics / Site Photos:", type=["jpg", "png", "pdf"])
            if st.form_submit_button("Archive Location Record"):
                loc_file_status = uploaded_loc_file.name if uploaded_loc_file else "No File Attached"
                st.session_state.location_data.append({
                    "Venue Identifier": l_name, "Entry Clock": str(l_in), "Exit Clock": str(l_out), "Attached Media Asset": loc_file_status, "Logs Summary": l_det, "Logged By User": uid
                })
                st.success("Location telemetry vector saved.")
        st.write("---")
        st.subheader("📋 Verified Studio Location Intelligence Database")
        if st.session_state.location_data: st.table(pd.DataFrame(st.session_state.location_data))

    # --- MODULE 5: FLEET & LOGISTICS CONTROL ---
    elif choice == "Fleet & Logistics Control":
        st.header("🚚 Fleet Logistics & Asset Transport Dispatch Matrix")
        with st.form("v_form"):
            v_type = st.selectbox("Fleet Resource Strategic Deployment Allocation Mode:", ["On-Shoot Heavy Production Rig Use (Camera/Light Trucks)", "Transit/Travel Only Fleet Lines"])
            v_num = st.text_input("Vehicle Licensing Code / Asset Plate Identifier:")
            v_time = st.text_input("Operational Fleet Window Interval (e.g., 04:00 AM - 22:00 PM):")
            uploaded_fleet_file = st.file_uploader("📂 Upload Transport Bills / Driver License Verification Records:", type=["jpg", "pdf", "png"])
            if st.form_submit_button("Authorize Fleet Allocation"):
                fleet_file_status = uploaded_fleet_file.name if uploaded_fleet_file else "No File Attached"
                st.session_state.vehicle_data.append({"Allocation Mode": v_type, "Asset Plate Code": v_num, "Timeline Matrix": v_time, "Verification File": fleet_file_status})
                st.success("Resource successfully dispatched to fleet manifest array.")
        st.write("---")
        st.subheader("📋 Active Fleet Distribution Ledger")
        if st.session_state.vehicle_data: st.table(pd.DataFrame(st.session_state.vehicle_data))

    # --- MODULE 6: CATERING ALLOCATION ---
    elif choice == "Catering Allocation":
        st.header("🍽️ Provisions, Catering & Field Mess Logistics Matrix")
        with st.form("food_form"):
            f_slot = st.selectbox("Meal Production Allocation Slot Block:", ["Morning Breakfast Routine", "Afternoon Main Lunch Block", "Evening Break Snacks Line", "Night Shift Survival Dinner"])
            f_count = st.number_input("Headcount Package Specifications Volume (Total Units):", min_value=1, step=1)
            f_notes = st.text_input("Dietary Profiles / Menu Allocation Notes:")
            uploaded_food_file = st.file_uploader("📂 Upload Catering Invoice / Vendor Price Lists:", type=["pdf", "jpg", "png"])
            if st.form_submit_button("Authorize Food Manifest Order"):
                food_file_status = uploaded_food_file.name if uploaded_food_file else "No File Attached"
                st.session_state.food_data.append({"Slot": f_slot, "Total Headcount Packs": f_count, "Config Settings": f_notes, "Invoice Documentation": food_file_status})
                st.success("Food production orders allocated safely.")
        st.write("---")
        st.subheader("📋 Daily Kitchen Mess Logistics Ledger Sheet")
        if st.session_state.food_data: st.table(pd.DataFrame(st.session_state.food_data))

        # --- MODULE 7: MASTER SHOOTING SCHEDULE ---
    elif choice == "Master Shooting Schedule":
        st.header("📅 Studio Production Master Call Sheet Timeline Schedule Grid")
        with st.form("sched_form"):
            s_scene = st.text_input("Target Scene Key Index Identifier (e.g., Scene 09 / Take 04):")
            s_time = st.text_input("Operational Timeline Execution Window (e.g., 05:00 AM Sharp Call Time):")
            s_loc = st.text_input("Allocated Venue Spot Field Name:")
            uploaded_sched_file = st.file_uploader("📂 Upload Full Day Script Breakdown / Director Call Sheet PDF Layout:", type=["pdf", "png", "jpg"])
            if st.form_submit_button("Commit Sequence to Master Timeline Grid"):
                sched_file_status = uploaded_sched_file.name if uploaded_sched_file else "No File Attached"
                st.session_state.schedule_data.append({"Scene Block Key": s_scene, "Strict Schedule Timeline": s_time, "Target Venue Area": s_loc, "Full Reference Document": sched_file_status})
                st.success("Master schedule grid recalibrated successfully.")
        st.write("---")
        st.subheader("🖨️ Official Master Project Call Sheet Matrix")
        if st.session_state.schedule_data: st.table(pd.DataFrame(st.session_state.schedule_data))

    # --- MODULE 8: CAPITAL EXPENSE SPREADSHEET ---
    elif choice == "Capital Expense Spreadsheet":
        st.header("💰 Studio Resource Capital Allocation Ledger & Expense Sheet")
        with st.form("budget_form"):
            b_item = st.text_input("Expenditure Line Item Node Description:")
            b_cost = st.number_input("Direct Financial Cost Evaluation Value (INR Financial Value Amount):", min_value=0.0)
            uploaded_budget_file = st.file_uploader("📂 Upload Vendor Receipts / Expense Voucher Documentation Files:", type=["pdf", "png", "jpg", "xlsx"])
            if st.form_submit_button("Commit Debit Row to Account Ledger"):
                budget_file_status = uploaded_budget_file.name if uploaded_budget_file else "No Voucher File"
                st.session_state.budget_data.append({"Line Item Node": b_item, "Financial Allocation Value": f"₹{b_cost:,}", "Voucher File Token": budget_file_status})
                st.success("Financial asset row securely committed to ledger logs framework tracking.")
        st.write("---")
        st.subheader("📋 Live Studio Financial Statement Balances Framework")
        if st.session_state.budget_data: st.table(pd.DataFrame(st.session_state.budget_data))

    # --- MODULE 9: TALENT & CREW REGISTRY ---
    elif choice == "Talent & Crew Registry":
        st.header("👥 On-Screen Talents (Cast) & Technical Crew Master Registry Manifest")
        with st.form("crew_form"):
            cc_name = st.text_input("Full Registered Profile Legal Name:")
            cc_role = st.text_input("Allocated Departmental Function Role (e.g., Director of Photography, Cast Lead):")
            cc_con = st.text_input("Secure Direct Comms Mobile Contact Line:")
            uploaded_crew_file = st.file_uploader("📂 Upload Talent Contract Signed Agreements / Actor NDA Documents (PDF):", type=["pdf"])
            if st.form_submit_button("Commit Identity Profile to Studio Manifest"):
                crew_file_status = uploaded_crew_file.name if uploaded_crew_file else "No NDA Attached"
                st.session_state.crew_cast.append({"Legal Name": cc_name, "Assigned Function Role": cc_role, "Direct Comms Link": cc_con, "Contract Documentation File": crew_file_status})
                st.success("Operator personnel profile verified and appended to manifest database.")
        st.write("---")
        st.subheader("📋 Project Active Operational Personnel Manifest Registry Array")
        if st.session_state.crew_cast: st.table(pd.DataFrame(st.session_state.crew_cast))

    # --- MODULE 10: HARDWARE ASSETS INVENTORY ---
    elif choice == "Hardware Assets Inventory":
        st.header("🎥 Optics, Heavy Machinery Rigging & Technical Equipment Inventory")
        with st.form("eq_form"):
            eq_name = st.text_input("Hardware Gear Nomenclature Name / Model Unit Specification:")
            eq_dept = st.selectbox("Parent Deployment Asset Fleet Wing:", ["Optics & Camera Matrix Fleet", "Lighting Grid Rigging Array", "Sound Interface Transceiver Systems", "Grip & Movie Stabilization Framing Units"])
            uploaded_eq_file = st.file_uploader("📂 Upload Asset Insurance Documents / Gear Rental Receipts:", type=["pdf", "jpg", "png"])
            if st.form_submit_button("Check-In Asset to Warehouse Matrix"):
                eq_file_status = uploaded_eq_file.name if uploaded_eq_file else "No Insurance File"
                st.session_state.equipment.append({"Asset Unit Nomenclature": eq_name, "Deployment Wing Setup": eq_dept, "Asset File Log": eq_file_status})
                st.success("Asset tracking instance active inside terminal room matrix.")
        st.write("---")
        st.subheader("📋 Active Studio Hardware Inventory Array Ledger")
        if st.session_state.equipment: st.table(pd.DataFrame(st.session_state.equipment))
