#!/usr/bin/env python

import time

import pycozmo

with pycozmo.connect() as cli:

    lights = [
        pycozmo.lights.red_light,
        pycozmo.lights.green_light,
        pycozmo.lights.blue_light,
        pycozmo.lights.white_light,
        pycozmo.lights.off_light,
    ]

    while 1:
        for light in lights:
            cli.set_all_backpack_lights(light)
            cli.set_head_angle(angle=0.6)
            time.sleep(1)
            # A 22 kHz, 16-bit, mono file is required.
            cli.play_audio("test.wav")
            cli.wait_for(pycozmo.event.EvtAudioCompleted)
            cli.set_head_angle(angle=0.0)
            time.sleep(1)

