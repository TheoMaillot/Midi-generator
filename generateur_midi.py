import random
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from mido import MidiFile, MidiTrack, Message
from music21 import note, stream, midi, scale, pitch, interval

from utils import generate_melody, get_scale
from scales import SCALE_MAP


def generate_midi():
    try:
        scale_name = scale_combobox.get()
        scale_type = scale_name
        key = key_entry.get()  
        key_min = min_key_entry.get()  
        key_max = max_key_entry.get()  

        num_measures = int(measures_entry.get())
        rhythmic_generators = list(map(int, rhythmic_generators_entry.get().split(",")))
        melodic_complexity = float(melodic_complexity_entry.get())

        
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


def display_notes(melody):
    canvas.delete("all")
    note_height = 10  
    note_spacing = 20  
    time_scale = 100  

    for i, item in enumerate(melody):
        pitch = item["pitch"].midi 
        duration = item["duration"]

        if pitch is not None:
            y = 127 - pitch 
            x_start = i * time_scale
            x_end = x_start + duration * time_scale

            
            canvas.create_rectangle(x_start, y, x_end, y + note_height, fill="green", outline="black")
        else:
            
            x_start = i * time_scale
            x_end = x_start + duration * time_scale
            canvas.create_line(x_start, 50, x_end, 50, fill="red", dash=(4, 2))


# fenetre principale
root = tk.Tk()
root.title("Generateur MIDI")


params_frame = tk.LabelFrame(root, text="Parametres de la Melodie", padx=10, pady=10)
params_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# scale
scale_label = tk.Label(params_frame, text="Selectionner une gamme :")
scale_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
scale_combobox = ttk.Combobox(params_frame, values=list(SCALE_MAP.keys()))
scale_combobox.grid(row=0, column=1, padx=5, pady=5)
scale_combobox.set("Major (Ionian)")

# (key)
key_label = tk.Label(params_frame, text="Tonalite (Key) :")
key_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
key_entry = tk.Entry(params_frame)
key_entry.grid(row=1, column=1, padx=5, pady=5)
key_entry.insert(0, "C5")

# Hauteur minimale (key_min)
min_key_label = tk.Label(params_frame, text="Note minimale (Key Min) :")
min_key_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
min_key_entry = tk.Entry(params_frame)
min_key_entry.grid(row=2, column=1, padx=5, pady=5)
min_key_entry.insert(0, "C4")

# Hauteur maximale (key_max)
max_key_label = tk.Label(params_frame, text="Note maximale (Key Max) :")
max_key_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
max_key_entry = tk.Entry(params_frame)
max_key_entry.grid(row=3, column=1, padx=5, pady=5)
max_key_entry.insert(0, "C6")

# Nombre de mesures
measures_label = tk.Label(params_frame, text="Nombre de mesures :")
measures_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
measures_entry = tk.Entry(params_frame)
measures_entry.grid(row=4, column=1, padx=5, pady=5)
measures_entry.insert(0, "8")

#rythmique
rhythmic_generators_label = tk.Label(params_frame, text="Generateurs rythmiques (separes par des virgules) :")
rhythmic_generators_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
rhythmic_generators_entry = tk.Entry(params_frame)
rhythmic_generators_entry.grid(row=5, column=1, padx=5, pady=5)
rhythmic_generators_entry.insert(0, "2,3,5")

# melody complexity
melodic_complexity_label = tk.Label(params_frame, text="Complexite melodique (0-1) :")
melodic_complexity_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
melodic_complexity_entry = tk.Entry(params_frame)
melodic_complexity_entry.grid(row=6, column=1, padx=5, pady=5)
melodic_complexity_entry.insert(0, "0.5")

# Cadre pour les boutons
buttons_frame = tk.Frame(root)
buttons_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Bouton pour afficher les notes
display_button = tk.Button(buttons_frame, text="Afficher les Notes", command=lambda: display_notes([]))
display_button.grid(row=0, column=0, padx=5, pady=5)

# Midi genertion button
generate_button = tk.Button(buttons_frame, text="Generer un fichier MIDI", command=generate_midi)
generate_button.grid(row=1, column=0, padx=5, pady=5)

# Canevas pour la visualisation des notes
canvas = tk.Canvas(root, width=800, height=400, bg="white")
canvas.grid(row=2, column=0, padx=10, pady=10)



# Executer la boucle principale
root.mainloop()
