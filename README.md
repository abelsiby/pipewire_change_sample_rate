
# Change DAC output sample rates

A simple python script that creates /client.conf.d/client-hifi.conf and /pipewire.conf.d/pipewire-hifi.conf files in ~/.config/pipewire/ directory
Once the script is run and the sample rates are passed, pipewire will match the sample rate of output dac to that of the audio file.

Run:

`git clone git@github.com:abelsiby/pipewire_change_sample_rate.git && cd ~/pipewire_change_sample_rate` 

*(assuming you are running the terminal from the home directory)

`python change_sample_rate.py`

In the screenshot below, I have set the default sample rate as 44100 and selects sample rates from allow rates if any of the sample rates passed are available for the audio file (below I passed 32000, 48000, 96000, 192000 and 384000)

![alt text](<Screenshot From 2025-04-12 21-06-07.png>)


Restart pipewire service after running the python script to reflect the changes

`systemctl restart --user pipewire.service pipewire-pulse.service`

You can delete the git folder as it is no longer required

`rm -rf pipewire_change_sample_rate`
