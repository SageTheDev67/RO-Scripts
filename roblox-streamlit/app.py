import streamlit as st
import os
import json
import pyperclip

# --- Page Config ---
st.set_page_config(page_title="RO Scripts", layout="centered")
st.title("RO Scripts")
st.markdown("Educational Roblox Lua scripts only — moderated content.")

# --- Load metadata ---
metadata_path = os.path.join("scripts", "metadata.json")
if os.path.exists(metadata_path):
    with open(metadata_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)
else:
    metadata = {}

# --- List scripts ---
script_folder = "scripts"
all_scripts = [f for f in os.listdir(script_folder) if f.endswith(".lua")]

# --- Search ---
search_query = st.text_input("Search scripts (by name, author, category)")
filtered_scripts = [
    s for s in all_scripts
    if search_query.lower() in s.lower()
    or search_query.lower() in metadata.get(s, {}).get("author", "").lower()
    or search_query.lower() in metadata.get(s, {}).get("category", "").lower()
] if search_query else all_scripts

if filtered_scripts:
    script_choice = st.selectbox("Select a script to view", filtered_scripts)
    
    script_path = os.path.join(script_folder, script_choice)
    with open(script_path, "r", encoding="utf-8") as file:
        code = file.read()
    
    st.subheader(script_choice)
    
    info = metadata.get(script_choice, {})
    st.markdown(f"**Author:** {info.get('author','Unknown')}  \n**Category:** {info.get('category','Unknown')}  \n**Description:** {info.get('description','No description')}")
    
    st.code(code, language="lua")
    
    # Download button
    st.download_button(
        label="Download Script",
        data=code,
        file_name=script_choice,
        mime="text/plain"
    )
    
    # Copy to clipboard button
    if st.button("Copy to Clipboard"):
        pyperclip.copy(code)
        st.success("Copied!")
else:
    st.warning("No scripts found or match your search.")

script_folder = "scripts"

if not os.path.exists(script_folder):
    st.error("The scripts folder is missing! Please create a 'scripts/' folder with .lua files.")
    st.stop()

all_scripts = [f for f in os.listdir(script_folder) if f.endswith(".lua")]

