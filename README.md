A python program to randomly generate music based on the Twelve-tone technique. This uses the [Pyknon music library](https://github.com/kroger/pyknon). Since it's small I added it here for convenience and in case I make any changes to it. 

As of now it only generates ~4 measures of music for up to four instruments by randomy selecting four prime rows and slamming them together. Since atonal music sounds really random anyway I figured this would be a good exercise in trying to write a program that randomly composes music. 

Depending on your MIDI synthesis capabilities this will likely sound bad to really bad. 

<b>TODO:</b><br>
Add rests for rhythmic variations<br>
Rewrite algorithm to keep a running total of measure length <br>
Add logic to get the other 36 scales, retrograde, inverted, retrograde-inverted<br>
Generate a fixed number of measures<br>
Make it more sophisticated overall <br>

<br>
<b>Future/Maybe:</b><br>
Allow control over scales to be used.<br>
Add dynamic variations<br>
Create example song, I plan on recreating the MIDI in a proper DAW so the above suggestion I might not ever implement<br>
Write music library, someday... 

