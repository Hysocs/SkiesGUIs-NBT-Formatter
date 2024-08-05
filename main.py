import re
import json
import tkinter as tk
from tkinter import scrolledtext, Toplevel, Label

def parse_command(command):
    # Regular expressions to match parts of the command
    display_name_re = r'Name:\'({.+?})\''
    lore_re = r'Lore:\[(.+?)\]'
    skullowner_id_re = r'Id:\[I;([\d,-]+)\]'
    textures_re = r'Value:"(.+?)"'

    # Find matches
    display_name_match = re.search(display_name_re, command)
    lore_match = re.search(lore_re, command)
    skullowner_id_match = re.search(skullowner_id_re, command)
    textures_match = re.search(textures_re, command)
    
    # Extract and format data
    display_name = display_name_match.group(1) if display_name_match else ''
    lore = lore_match.group(1).split(',') if lore_match else []
    lore = [lore_part.replace('\'', '"') for lore_part in lore]
    skullowner_id = [int(i) for i in skullowner_id_match.group(1).split(',')] if skullowner_id_match else []
    textures = textures_match.group(1) if textures_match else ''
    
    # Create the JSON structure
    data = {
        "nbt": {
            "display": {
                "Name": display_name,
                "Lore": lore
            },
            "SkullOwner": {
                "Id": skullowner_id,
                "Properties": {
                    "textures": [
                        {
                            "Value": textures
                        }
                    ]
                }
            }
        }
    }
    
    return data

def convert_command():
    command = command_entry.get().strip()
    json_data = parse_command(command)
    
    # Convert to JSON string and remove the enclosing brackets
    json_str = json.dumps(json_data, indent=2)
    json_str = json_str[1:-1].strip()
    
    # Display the formatted JSON in the output text box
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, json_str)

def show_tooltip(event):
    global tooltip
    tooltip = Toplevel(root)
    tooltip.wm_overrideredirect(True)
    tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
    label = Label(tooltip, text=(
        "How to use this tool:\n"
        "1. Go to the website https://minecraft-heads.com\n"
        "2. Find a head you want to use.\n"
        "3. Set the version to 1.20.\n"
        "4. Set the command type to 'server'.\n"
        "5. Copy the 'give' command provided by the site.\n"
        "6. Paste the command in the input box.\n"
        "7. Press 'Convert to JSON' to get the formatted JSON output."
    ), bg="#2e2e2e", fg="#dcdcdc", borderwidth=1, relief="solid", padx=10, pady=10, wraplength=300, justify="left")
    label.pack()

def hide_tooltip(event):
    global tooltip
    if tooltip:
        tooltip.destroy()
        tooltip = None

# Create the main window
root = tk.Tk()
root.title("SkiesGUIs NBT Formatter")

# Set dark theme colors
bg_color = "#2e2e2e"
fg_color = "#dcdcdc"
input_bg_color = "#3e3e3e"
input_fg_color = "#ffffff"

root.configure(bg=bg_color)

# Create and place the widgets
tk.Label(root, text="Enter Minecraft Command:", bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=10, pady=10, sticky="w")

command_entry = tk.Entry(root, width=100, bg=input_bg_color, fg=input_fg_color)
command_entry.grid(row=1, column=0, padx=10, pady=10, sticky="we")

info_button = tk.Label(root, text="?", bg=input_bg_color, fg=input_fg_color, font=("Helvetica", 12, "bold"), cursor="hand2")
info_button.grid(row=1, column=1, padx=5, pady=10, sticky="w")
info_button.bind("<Enter>", show_tooltip)
info_button.bind("<Leave>", hide_tooltip)

tk.Label(root, text="JSON Output:", bg=bg_color, fg=fg_color).grid(row=2, column=0, padx=10, pady=10, sticky="w")

output_text = scrolledtext.ScrolledText(root, width=100, height=20, bg=input_bg_color, fg=input_fg_color)
output_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert to JSON", command=convert_command, bg=input_bg_color, fg=input_fg_color)
convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="we")

# Configure column to expand with the window
root.grid_columnconfigure(0, weight=1)

# Initialize the tooltip variable
tooltip = None

# Start the GUI event loop
root.mainloop()
