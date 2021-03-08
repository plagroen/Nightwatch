# Nightwatch

**CAVEAT EMPTOR**
-----------------
This project is not even in its infancy, it's still only being conceived. <br/>
The chances of this ever coming to fruition are slim, at best. Be advised that any effort you may put in will likely be in vain. <br/>
That said, any contributions and/or suggestions are welcome.

Overview
--------
Nightwatch is intended to be an unobtrusive device to aid with supervisory/care-taking tasks in the night-time. 
Think parents of young children, or people taking care of a person with a disease, old-age, disabilities or a mental disorder.

Primary function of Nightwatch
- Give a soft glow to the room when one of the caregiver comes out of bed. <br/>
Softly enough not to wake any bed/roommates, but bright enough for the care giver to safely navigate the room. <br/>
*No more banged toes, no more grumpy partners!*

Secondary functions are:
- Alarmclock w. optional wake-up light
- Alarm triggerd by external sensors, e.g. a motionsensor or second Nightwatch going off in the room of the person receiving care.

Tertiary functions are:
- Party mode (changing colors, music)
- Oh-la-la mode (soft pulsating red glow, Ravel's Bolero on repeat)
- Drift off gently mode (light dimming ever so slowly, soft music or white noise fading away)

Quaternary function:
- Alarm triggerd by remote signal via internet, e.g. a second Nightwatch going off in the home of the person receiving care.
This applies mainly when the person receiving care still lives somewhat independently but not too distant (e.g. elderly parent in the same village, prone to falling or uneasy at night)
Requires some way to distinguish between false alarm ('taking a wee') and actual alarm (confusion/walkabout, falling). 
Perhaps include microphone for direct Nightwatch-to-Nightwatch voice connection?


Hardware
--------
Nightwatch will consist of a raspberry pi zero W, with PIR sensor, NEOPixels, DAC & Speaker, lightsensor, 433 MHz receiver in a 3D printed enclosure.

Software
--------
Nightwatch will reside mainly under the bed. 
As a user interface, Nightwatch will run a webserver so it can be controlled from any smartphone on the network.
The user interface will be optionally password protected to prevent abuse/pranks

This Github project hosts the software.
