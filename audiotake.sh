ffmpeg -f alsa -i plughw:CARD=U0x46d0x81b,DEV=0 -acodec libmp3lame -t 30 -strftime 1 $(date +"%Y%m%d%H%M").wav


