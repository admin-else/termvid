#!/bin/python3
from PIL import Image, ImageSequence
from moviepy.editor import VideoFileClip
import time
import shutil

blocks = " ░▒▓█"

def pilimg2ascii_art(img):
  terminal_size = shutil.get_terminal_size()
  new_width = terminal_size.columns - 1
  img = img.convert("L")
  img = img.resize((new_width, terminal_size.lines))

  
  new_pixels = [blocks[pixel // 63] for pixel in img.getdata()] # int(255 / len(blocks)) = 63
  new_pixels = "".join(new_pixels)
  
  ascii_image = [
      new_pixels[index : index + new_width]
      for index in range(0, len(new_pixels), new_width)
  ]
  ascii_image = "\n".join(ascii_image)
  
  return ascii_image

def pilimg2ascii_art_color(img):
    terminal_size = shutil.get_terminal_size()
    new_width = terminal_size.columns - 1
    img = img.resize((new_width, terminal_size.lines))

    new_pixels = [f"\033[38;2;{r:03};{g:03};{b:03}m█" for r, g, b in img.getdata()]
    new_pixels = "".join(new_pixels)

    new_width *= 20 # be 20 pixel make 1 color
    new_pixels_count = len(new_pixels)
    ascii_image = [
        new_pixels[index : index + new_width]
        for index in range(0, new_pixels_count, new_width)
    ]
    ascii_image = "\n".join(ascii_image)
    return ascii_image

def main():
  clip = VideoFileClip("rick.mp4")
  
  print("\033[1m") # bold
  try:
    for frame in clip.iter_frames():
      frame.audio.preview()
      start_time = time.time()
      art = pilimg2ascii_art_color(Image.fromarray(frame))
      print("\033[2J\033[3J\033[H")
      print(art)
      wait_time = 1 / clip.fps - (time.time() - start_time)
      
      if wait_time > 0:
        time.sleep(wait_time)

  except KeyboardInterrupt:
    pass
  
  print("\033[2J\033[3J\033[H")


main()
