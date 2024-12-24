import functools
import itertools
import sympy
import random
from music21 import scale, pitch, interval

from scales import SCALE_MAP

def get_scale(scale_name):
    if scale_name not in SCALE_MAP:
        raise ValueError(f"Scale '{scale_name}' is not defined.")
    return SCALE_MAP[scale_name]

def set2ls(s, stop):
    converted = sorted(list(s)) + [stop]
    return [y - x for x, y in zip(converted, converted[1:])]

def synchronize(*generators, convert_set2ls=True):
    cp = functools.reduce(lambda x, y: x * y, generators)  # common_product
    gen = (set(range(0, cp, generator)) for generator in generators)
    union = set().union(*gen)
    return set2ls(union, cp) if convert_set2ls else union

def fractionize(*generators):
    def mk_fractionized_gen(generator, major, stop):
        new_gen = set(range(0, generator * major, generator))
        gen = (set([el + (major * counter) for el in new_gen]) for counter in range(major - generator + 1))
        return set().union(*gen)
    major = max(generators)
    stop = pow(major, 2)
    gen = (mk_fractionized_gen(generator, major, stop) for generator in filter(lambda x: x < major, generators))
    return set2ls(set().union(*gen, set(range(0, stop, major))), stop)



def evolving_structure(melody, rhythm_pattern, music_scale, min_pitch, max_pitch, complexity_factor):
    for beat_duration in rhythm_pattern:
        if random.random() <= complexity_factor:
            # As complexity increases, pick a note farther from the tonic
            random_pitch = random.choice([
                p for p in music_scale.pitches
                if min_pitch.midi <= p.midi <= max_pitch.midi
            ])
            melody.append({"pitch": random_pitch, "duration": beat_duration})
            #complexity_factor += 0.05 
        #else:
            #melody.append({"pitch": None, "duration": beat_duration})
    return melody



def generate_melody(
    scaleType,
    key,
    num_measures,
    key_min,
    key_max,
    rhythm_generators,
    melodic_complexity
):
    if scaleType not in SCALE_MAP:
        raise ValueError(f"Scale '{scaleType}' is not recognized.")

    music_scale = SCALE_MAP[scaleType]  

    try:
        tonic = pitch.Pitch(key)
    except Exception as e:
        raise ValueError(f"Invalid key '{key}'. Error: {e}")

    try:
        transposed_pitches = [
            tonic.transpose(interval.Interval(noteStart=music_scale.pitches[0], noteEnd=p))
            for p in music_scale.pitches 
        ]
    except Exception as e:
        raise ValueError(f"Error transposing scale to key '{key}': {e}")

    music_scale = scale.ConcreteScale(pitches=transposed_pitches)


    min_pitch = pitch.Pitch(key_min)
    max_pitch = pitch.Pitch(key_max)

    if min_pitch.midi > max_pitch.midi:
        raise ValueError("key_min must be lower than or equal to key_max.")

    rhythmic_pattern = synchronize(*rhythm_generators)

    melody = []

    melody = evolving_structure(melody, rhythmic_pattern, music_scale, min_pitch, max_pitch, melodic_complexity)

    return melody



