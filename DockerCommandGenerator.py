# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 12:55:19 2023

@author: richardd
"""

import requests
import subprocess
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def search_image_tags(image_name):
    try:
        url = f"https://hub.docker.com/v2/repositories/{image_name}/tags"
        response = requests.get(url)
        response.raise_for_status()
        tags = response.json()["results"]
        return [tag["name"] for tag in tags]
    except requests.exceptions.RequestException:
        return []

def generate_docker_run_command():
    #uzivatelske vstupy
    container_name = container_name_entry.get()
    image_name = image_name_entry.get()
    image_version = version_combobox.get()
    env_vars = dict(env_vars_listbox.get(0, tk.END))
    ports = ports_listbox.get(0, tk.END)
    volumes = volumes_listbox.get(0, tk.END)

    # generovani docker run commandu
    command = ['docker', 'run', '-it', '--name', container_name]

    # pridani enviromental values
    for key, value in env_vars.items():
        command.extend(['-e', f'{key}={value}'])

    # pridani port biddings
    for port in ports:
        command.extend(['-p', f'{port}'])

    # pridani volume mappings
    for volume in volumes:
        command.extend(['-v', f'{volume}'])

    command.append(f'{image_name}:{image_version}')

    # print vygenerovaneho commandu docker run
    generated_command_label.config(text='Generated Docker run command:')
    command_output.config(state=tk.NORMAL)
    command_output.delete(1.0, tk.END)
    command_output.insert(tk.END, ' '.join(command))
    command_output.config(state=tk.DISABLED)

def update_image_versions(*args):
    selected_image = image_name_entry.get()
    tags = search_image_tags(selected_image)
    version_combobox['values'] = tags

def show_error(message):
    messagebox.showerror('Error', message)

# Create the main window
window = tk.Tk()
window.title('Docker Run Command Generator')

# vytvoreni Labels a fields pro uzivatelsky vstup
container_name_label = tk.Label(window, text='Container Name:')
container_name_label.pack()
container_name_entry = tk.Entry(window)
container_name_entry.pack()

image_name_label = tk.Label(window, text='Image Name:')
image_name_label.pack()
image_name_entry = tk.Entry(window)
image_name_entry.pack()
image_name_entry.bind('<FocusOut>', update_image_versions)

image_version_label = tk.Label(window, text='Image Version:')
image_version_label.pack()
version_combobox = ttk.Combobox(window, state='readonly')
version_combobox.pack()

# vytvoreni labels framu a listboxu pro enviromental values
env_vars_label = tk.Label(window, text='Environment Variables:')
env_vars_label.pack()

env_vars_frame = tk.Frame(window)
env_vars_frame.pack()

env_vars_listbox = tk.Listbox(env_vars_frame)
env_vars_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

env_vars_scrollbar = tk.Scrollbar(env_vars_frame)
env_vars_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

env_vars_listbox.config(yscrollcommand=env_vars_scrollbar.set)
env_vars_scrollbar.config(command=env_vars_listbox.yview)

env_key_entry = tk.Entry(window)
env_key_entry.pack()

env_value_entry = tk.Entry(window)
env_value_entry.pack()

def add_env_var():
    key = env_key_entry.get()
    value = env_value_entry.get()
    if not key or not value:
        show_error('Please enter a key and value for the environment variable.')
        return
    env_vars_listbox.insert(tk.END, (key, value))
    env_key_entry.delete(0, tk.END)
    env_value_entry.delete(0, tk.END)

def remove_env_var():
    selected_indices = env_vars_listbox.curselection()
    for index in reversed(selected_indices):
        env_vars_listbox.delete(index)

add_env_var_button = tk.Button(window, text='Add Env Var', command=add_env_var)
add_env_var_button.pack()
remove_env_var_button = tk.Button(window, text='Remove Env Var', command=remove_env_var)
remove_env_var_button.pack()

# Create port bindings section
ports_label = tk.Label(window, text='Port Bindings:')
ports_label.pack()

ports_frame = tk.Frame(window)
ports_frame.pack()

ports_listbox = tk.Listbox(ports_frame, selectmode=tk.MULTIPLE)
ports_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

ports_scrollbar = tk.Scrollbar(ports_frame)
ports_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

ports_listbox.config(yscrollcommand=ports_scrollbar.set)
ports_scrollbar.config(command=ports_listbox.yview)

ports_entry = tk.Entry(window)
ports_entry.pack()

def add_port():
    port = ports_entry.get()
    if not port:
        show_error('Please enter a port number.')
        return
    ports_listbox.insert(tk.END, port)
    ports_entry.delete(0, tk.END)

def remove_port():
    selected_indices = ports_listbox.curselection()
    for index in reversed(selected_indices):
        ports_listbox.delete(index)

add_port_button = tk.Button(window, text='Add Port', command=add_port)
add_port_button.pack()
remove_port_button = tk.Button(window, text='Remove Port', command=remove_port)
remove_port_button.pack()

# vytvoreni sekce pro volume mapping
volumes_label = tk.Label(window, text='Volume Mappings:')
volumes_label.pack()

volumes_frame = tk.Frame(window)
volumes_frame.pack()

volumes_listbox = tk.Listbox(volumes_frame, selectmode=tk.MULTIPLE)
volumes_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

volumes_scrollbar = tk.Scrollbar(volumes_frame)
volumes_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

volumes_listbox.config(yscrollcommand=volumes_scrollbar.set)
volumes_scrollbar.config(command=volumes_listbox.yview)

volumes_entry = tk.Entry(window)
volumes_entry.pack()

def add_volume():
    volume = volumes_entry.get()
    if not volume:
        show_error('Please enter a volume mapping.')
        return
    volumes_listbox.insert(tk.END, volume)
    volumes_entry.delete(0, tk.END)

def remove_volume():
    selected_indices = volumes_listbox.curselection()
    for index in reversed(selected_indices):
        volumes_listbox.delete(index)

add_volume_button = tk.Button(window, text='Add Volume', command=add_volume)
add_volume_button.pack()
remove_volume_button = tk.Button(window, text='Remove Volume', command=remove_volume)
remove_volume_button.pack()

# Button pro vygenerovani commandu 
generate_button = tk.Button(window, text='Generate Command', command=generate_docker_run_command)
generate_button.pack()

# vytvoreni labelu pro generovani commandu
generated_command_label = tk.Label(window, text='')
generated_command_label.pack()

command_output = tk.Text(window, height=5, state=tk.DISABLED)
command_output.pack()

# rozjeti gui v loopu MAIN
window.mainloop()
