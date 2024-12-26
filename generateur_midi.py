import random
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, PhotoImage
from mido import MidiFile, MidiTrack, Message
from music21 import note, stream, midi, scale, pitch, interval
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from utils import generate_melody, get_scale
from scales import SCALE_MAP
#from visual_midi.visual_midi import Plotter, PrettyMIDI


def generate_midi():
    try:
        scale_name = scale_combobox.get()
        scale_type = scale_name
        key = key_combobox.get()  
        key_min = min_key_entry.get()  
        key_max = max_key_entry.get()  

        num_measures = int(measures_entry.get())
        rhythmic_generators = [
            int(rhythmic_generator_entry_1.get()), 
            int(rhythmic_generator_entry_2.get()), 
            int(rhythmic_generator_entry_3.get())
        ]

        melodic_complexity = float(melodic_complexity_entry.get()) / 100  # Conversion correcte
        print(melodic_complexity)

        
        output_file = filedialog.asksaveasfilename(
            defaultextension=".mid",
            filetypes=[("MIDI files", "*.mid"), ("All files", "*.*")]
        )

        if not output_file:
            messagebox.showinfo("Cancelled")
            return

        
        melody = generate_melody(
            scaleType=scale_type,
            key=key,
            num_measures=num_measures,
            key_min=key_min,
            key_max=key_max,
            rhythm_generators=rhythmic_generators,
            melodic_complexity=melodic_complexity
        )

        
        midi_stream = stream.Stream()
        for item in melody:
            midi_stream.append(note.Note(item["pitch"], quarterLength=item["duration"]))

        midi_file = midi.translate.music21ObjectToMidiFile(midi_stream)
        midi_file.open(output_file, "wb")
        midi_file.write()
        midi_file.close()

        messagebox.showinfo("Success", f"Midi file generated : {output_file}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occured : {e}")


# Function to add a explanation window for rhythm generators
def show_info_rhythm():
    info_window = tk.Toplevel()
    info_window.title("What Are Rhythmic Generators?")
    info_window.geometry("400x650")
    
    info_text = """
    What are rhythm generators ?

    Rhythm generators are numbers used to create rhythmic patterns by determining the intervals or cycles in a sequence. Each number represents a rhythm unit that contributes to the overall pattern. You can adjust these values to create custom rhythms.
    
    Example:
    If you enter the values 2, 3, and 5 in the boxes, the rhythm will alternate between cycles of 2 beats, 3 beats, and 5 beats. This can be useful for creating complex polyrhythmic sequences.
    
    Instructions:
    - Enter one number in each box.
    - The numbers must be integers (e.g., 2, 3, 5).
    - Experiment with different values to explore new rhythmic combinations.
    """
    
    info_label = tk.Label(info_window, text=info_text, wraplength=380, justify="left")
    info_label.pack(padx=10, pady=10)
    
    close_button = tk.Button(info_window, text="Close", command=info_window.destroy)
    close_button.pack(pady=10)

# Function to add a explanation window for melodic complexity
def show_info_melodic():
    info_window = tk.Toplevel()
    info_window.title("What is melodic complexity?")
    info_window.geometry("400x650")
    
    info_text = """
    Melodic Complexity refers to the level of variation, unpredictability, and sophistication in a melody. A melody with high melodic complexity might include a wide range of pitches, intricate rhythmic patterns, and unusual or unexpected intervals. In contrast, a simple melody is more predictable and uses fewer notes and simpler intervals.

    In this context, the scale for melodic complexity is from 0 to 100, where:

    0 represents a very simple and repetitive melody, with limited variation.
    100 represents a highly complex and varied melody, with intricate patterns and more diverse pitch movements.
    This measure helps evaluate how diverse and sophisticated the melodic structure of a piece of music is.
    """
    
    info_label = tk.Label(info_window, text=info_text, wraplength=380, justify="left")
    info_label.pack(padx=10, pady=10)
    
    close_button = tk.Button(info_window, text="Close", command=info_window.destroy)
    close_button.pack(pady=10)

def update_entry_from_slider(val):
    """Update textbox/curseur"""
    melodic_complexity_entry.delete(0, tk.END)
    melodic_complexity_entry.insert(0, val)

def update_slider_from_entry():
    """Update Curseur/TextBox"""
    try:
        val = int(melodic_complexity_entry.get())
        if 0 <= val <= 100:
            melodic_complexity_slider.set(val)
        else:
            melodic_complexity_entry.delete(0, tk.END)
            melodic_complexity_entry.insert(0, "0")  # Si la valeur est hors de la plage, on remet 0
    except ValueError:
        melodic_complexity_entry.delete(0, tk.END)
        melodic_complexity_entry.insert(0, "0")  # Si la valeur n'est pas un nombre, on remet 0


# fenetre principale
root = ttk.Window(themename="solar") 
root.title("MIDI generator")
root.geometry("640x470")


params_frame = tk.LabelFrame(root, text="Melody parameters", padx=10, pady=10)
params_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# scale
scale_label = tk.Label(params_frame, text="Choose a scale :")
scale_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
scale_combobox = ttk.Combobox(params_frame, values=list(SCALE_MAP.keys()))
scale_combobox.grid(row=0, column=1, padx=5, pady=5)
scale_combobox.set("Major (Ionian)")

# (key)
key_label = tk.Label(params_frame, text="Key :")
key_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
key_combobox = ttk.Combobox(params_frame, values=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"])
key_combobox.grid(row=1, column=1, padx=5, pady=5)

# Hauteur minimale (key_min)
min_key_label = tk.Label(params_frame, text="Min key :")
min_key_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
min_key_entry = tk.Entry(params_frame)
min_key_entry.grid(row=2, column=1, padx=5, pady=5)
min_key_entry.insert(0, "C4")

# Hauteur maximale (key_max)
max_key_label = tk.Label(params_frame, text="Max key :")
max_key_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
max_key_entry = tk.Entry(params_frame)
max_key_entry.grid(row=3, column=1, padx=5, pady=5)
max_key_entry.insert(0, "C6")

# Nombre de mesures
measures_label = tk.Label(params_frame, text="Number of times :")
measures_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
measures_entry = tk.Entry(params_frame)
measures_entry.grid(row=4, column=1, padx=5, pady=5)
measures_entry.insert(0, "4")

#rythmique
rhythmic_generators_label = tk.Label(params_frame, text="Rhythm generators :")
rhythmic_generators_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
rhythmic_generators_frame = tk.Frame(params_frame)
rhythmic_generators_frame.grid(row=5, column=1, padx=5, pady=5, sticky="w")
rhythmic_generator_entry_1 = tk.Entry(rhythmic_generators_frame, width=4)
rhythmic_generator_entry_1.grid(row=0, column=1, padx=2)
rhythmic_generator_entry_2 = tk.Entry(rhythmic_generators_frame, width=4)
rhythmic_generator_entry_2.grid(row=0, column=2, padx=2)
rhythmic_generator_entry_3 = tk.Entry(rhythmic_generators_frame, width=4)
rhythmic_generator_entry_3.grid(row=0, column=3, padx=2)
# Button "?" 
info_button_rhythm = tk.Button(params_frame, text="?", command=show_info_rhythm, width=2)
info_button_rhythm.grid(row=5, column=3, padx=5, pady=5, sticky="w")


# melody complexity
melodic_complexity_label = tk.Label(params_frame, text="Melodic complexity (0-100) :")
melodic_complexity_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
    # Curseur horizontal (Scale)
melodic_complexity_slider = tk.Scale(params_frame, from_=0, to=100, orient="horizontal", command=update_entry_from_slider)
melodic_complexity_slider.grid(row=6, column=1, padx=5, pady=5, sticky="ew")
melodic_complexity_slider.set(100)
melodic_complexity_entry = tk.Entry(params_frame, width=5)
melodic_complexity_entry.grid(row=6, column=2, padx=5, pady=5)
melodic_complexity_entry.insert(0, "100")
    # Update textbox/curseur
melodic_complexity_entry.bind("<FocusOut>", lambda event: update_slider_from_entry())
    #explanation
info_button_melodic = tk.Button(params_frame, text="?", command=show_info_melodic, width=2)
info_button_melodic.grid(row=6, column=3, padx=5, pady=5, sticky="w")

# Cadre pour les boutons
buttons_frame = tk.Frame(root)
buttons_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


# Midi genertion button
generate_button = tk.Button(buttons_frame, text="Export midi file", command=generate_midi)
generate_button.grid(row=1, column=0, padx=5, pady=5)




# Executer la boucle principale
root.mainloop()
