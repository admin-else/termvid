#!/usr/bin/env python3
from PIL import Image
from moviepy.editor import VideoFileClip
import time
import shutil
import argparse


def pilimg2ascii_art(img, color=True):
    blocks = " ░▒▓█"
    terminal_size = shutil.get_terminal_size()
    new_width = terminal_size.columns - 1
    img = img.resize((new_width, terminal_size.lines))

    if color:
        new_pixels = [f"\033[38;2;{r:03};{g:03};{b:03}m█" for r, g, b in img.getdata()]
    else:
        img = img.convert("L")

        new_pixels = [
            blocks[pixel // 63] for pixel in img.getdata()
        ]  # int(255 / len(blocks)) = 63
    new_pixels = "".join(new_pixels)

    if color:
        new_width *= 20

    ascii_image = [
        new_pixels[index : index + new_width]
        for index in range(0, len(new_pixels), new_width)
    ]
    ascii_image = "\n".join(ascii_image)

    return ascii_image


def main():
    parser = argparse.ArgumentParser(description="Video player for the terminal.")
    parser.add_argument("file", help="File to process")
    parser.add_argument("-m", "--monochrome", action="store_true", help="Disable color.")
    parser.add_argument("-l", "--loop", action="store_true", help="Enable looping.")

    args = parser.parse_args()

    first = True
    try:
        clip = VideoFileClip(args.file)
    except Exception as e:
        print(e)
        exit(1)

    print("\033[1m")
    while args.loop or first:
        first = False
        for frame in clip.iter_frames():
            start_time = time.perf_counter()
            art = pilimg2ascii_art(Image.fromarray(frame), not args.monochrome)
            print("\033[2J\033[3J\033[H")
            print(art)
            wait_time = 1 / clip.fps - (time.perf_counter() - start_time)

            if wait_time > 0:
                time.sleep(wait_time)

    print("\033[2J\033[3J\033[H")

if __name__=="__main__":
    main()
