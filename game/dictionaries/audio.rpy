define config.default_music_volume = 0.5

init python:

    renpy.music.set_volume(1.0, channel="voice")
    renpy.music.set_volume(0.5, channel="music")
    renpy.music.set_volume(0.5, channel="music1")
    renpy.music.set_volume(0.7, channel="sound")
    renpy.music.register_channel("music1", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("fire", mixer="sound", loop=True)
    renpy.music.register_channel("alarmquiet", mixer="sound", loop=True)

    def audio_crossFade(fadeTime, music):
        oldChannel = None
        newChannel = None
        if renpy.music.get_playing(channel="music") is not None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = "music"
            newChannel = "music1"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is not None:
            oldChannel = "music1"
            newChannel = "music"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="music1") is None:
            oldChannel = None
            newChannel = "music"
            
        if oldChannel is not None:
            renpy.music.stop(channel= oldChannel, fadeout=fadeTime)
            
        if newChannel is not None:
            renpy.music.play(music, channel=newChannel, loop=None,fadein=fadeTime)

    def sfx_crossFade(fadeTime, sound):
        oldChannel = None
        newChannel = None
        if renpy.music.get_playing(channel="sound") is not None and renpy.music.get_playing(channel="alarmquiet") is None:
            oldChannel = "sound"
            newChannel = "alarmquiet"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="alarmquiet") is not None:
            oldChannel = "alarmquiet"
            newChannel = "sound"
        elif renpy.music.get_playing(channel="music") is None and renpy.music.get_playing(channel="alarmquiet") is None:
            oldChannel = None
            newChannel = "sound"
            
        if oldChannel is not None:
            renpy.music.stop(channel= oldChannel, fadeout=fadeTime)
            
        if newChannel is not None:
            renpy.music.play(sound, channel=newChannel, loop=None,fadein=fadeTime)
