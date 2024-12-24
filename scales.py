from music21 import scale, interval, pitch

SCALE_MAP = {
    # Gammes majeures
    "Major (Ionian)": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('E'),
        pitch.Pitch('F'), pitch.Pitch('G'), pitch.Pitch('A'), pitch.Pitch('B')
    ]),
    "Major Bebop": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('E'),
        pitch.Pitch('F'), pitch.Pitch('G'), pitch.Pitch('A'),
        pitch.Pitch('Bb'), pitch.Pitch('B')
    ]),
    "Major Bulgarian": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('E'),
        pitch.Pitch('F'), pitch.Pitch('F#'), pitch.Pitch('G'),
        pitch.Pitch('A'), pitch.Pitch('B')
    ]),
    "Major Hexatonic": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('E'),
        pitch.Pitch('G'), pitch.Pitch('A'), pitch.Pitch('B')
    ]),
    "Major Pentatonic": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('E'),
        pitch.Pitch('G'), pitch.Pitch('A')
    ]),
    "Major Persian": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('E'),
        pitch.Pitch('F'), pitch.Pitch('G#'), pitch.Pitch('A'), pitch.Pitch('B')
    ]),
    "Major Polymode": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('E'),
        pitch.Pitch('F#'), pitch.Pitch('G'), pitch.Pitch('A'), pitch.Pitch('Bb')
    ]),

    # Gammes mineures
    "Minor Harmonic": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('Eb'),
        pitch.Pitch('F'), pitch.Pitch('G'), pitch.Pitch('Ab'), pitch.Pitch('B')
    ]),
    "Minor Hungarian": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('Eb'),
        pitch.Pitch('F#'), pitch.Pitch('G'), pitch.Pitch('Ab'), pitch.Pitch('B')
    ]),
    "Minor Melodic": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('Eb'),
        pitch.Pitch('F'), pitch.Pitch('G'), pitch.Pitch('A'), pitch.Pitch('B')
    ]),
    "Minor Natural (Aeolian)": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('Eb'),
        pitch.Pitch('F'), pitch.Pitch('G'), pitch.Pitch('Ab'), pitch.Pitch('Bb')
    ]),
    "Minor Neapolitan": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('Db'), pitch.Pitch('Eb'),
        pitch.Pitch('F'), pitch.Pitch('G'), pitch.Pitch('Ab'), pitch.Pitch('B')
    ]),
    "Minor Pentatonic": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('Eb'), pitch.Pitch('F'),
        pitch.Pitch('G'), pitch.Pitch('Bb')
    ]),
    "Minor Polymode": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('Eb'),
        pitch.Pitch('F#'), pitch.Pitch('G'), pitch.Pitch('Ab'), pitch.Pitch('Bb')
    ]),
    "Minor Romanian": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('Eb'),
        pitch.Pitch('F#'), pitch.Pitch('G'), pitch.Pitch('A'), pitch.Pitch('B')
    ]),

    # Gammes autres
    "Other Arabic": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('Eb'),
        pitch.Pitch('F#'), pitch.Pitch('G'), pitch.Pitch('Ab'), pitch.Pitch('B')
    ]),
    "Other Bebop Dominant": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('E'),
        pitch.Pitch('F'), pitch.Pitch('G'), pitch.Pitch('A'), pitch.Pitch('Bb')
    ]),
    "Other Blues": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('Eb'), pitch.Pitch('F'),
        pitch.Pitch('Gb'), pitch.Pitch('G'), pitch.Pitch('Bb')
    ]),
    "Other Blues Nonatonic": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('D#'), pitch.Pitch('E'),
        pitch.Pitch('F'), pitch.Pitch('G'), pitch.Pitch('A'), pitch.Pitch('Bb'), pitch.Pitch('B')
    ]),
    "Other Diminished": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('Eb'),
        pitch.Pitch('F'), pitch.Pitch('F#'), pitch.Pitch('G#'),
        pitch.Pitch('A'), pitch.Pitch('B')
    ]),
    "Other Egyptian": scale.ConcreteScale(pitches=[
        pitch.Pitch('C'), pitch.Pitch('D'), pitch.Pitch('F'),
        pitch.Pitch('G'), pitch.Pitch('A'), pitch.Pitch('Bb')
    ]),
    # Ajoutez les autres gammes ici de manière similaire...
}


