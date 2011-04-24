# $ sudo apt-get install fluidsynth
# $ sudo pip install mingus
#
# Download ChoriumRevA and unpack in this folder:
# http://www.hammersound.com/cgi-bin/soundlink.pl?action=view_download_page;ID=733;SoundFont_Location_Selected=Download%20USA;SoundFont_Filename_Selected=ChoriumRevA.rar
# (this is a webpage, don't try wget)

from random import shuffle

from mingus.midi import fluidsynth
from mingus.core import chords
from mingus.containers import Bar, Track
from mingus.containers.Instrument import MidiInstrument

fluidsynth.init("ChoriumRevA/ChoriumRevA.SF2", "alsa")

tr = lambda note: chords.triad(note, "C")

# that's stupid
# http://www.youtube.com/watch?v=5pidokakU4I

prg = [tr("C"), tr("G"), tr("A"), tr("F")]

bars = []

for chord in prg:
    b = Bar()
    b.place_notes(chord, 4)

    bars.append(b)

t = Track()


for b in bars:
    t.add_bar(b)
    

instrs = list(enumerate(MidiInstrument.names))
shuffle(instrs)

for i, name in instrs:
    print i, name
    fluidsynth.set_instrument(1, i)
        
    fluidsynth.play_Track(t)


