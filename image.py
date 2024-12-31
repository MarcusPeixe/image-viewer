#!/bin/python3.12

from PIL import Image
import argparse
import math
import time
import sys
import os

dither_palette = [
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,
    0,   0,   0,   0,   0,  95,   0,   0, 135,   0,   0, 175,
    0,   0, 215,   0,   0, 255,   0,  95,   0,   0,  95,  95,
    0,  95, 135,   0,  95, 175,   0,  95, 215,   0,  95, 255,
    0, 135,   0,   0, 135,  95,   0, 135, 135,   0, 135, 175,
    0, 135, 215,   0, 135, 255,   0, 175,   0,   0, 175,  95,
    0, 175, 135,   0, 175, 175,   0, 175, 215,   0, 175, 255,
    0, 215,   0,   0, 215,  95,   0, 215, 135,   0, 215, 175,
    0, 215, 215,   0, 215, 255,   0, 255,   0,   0, 255,  95,
    0, 255, 135,   0, 255, 175,   0, 255, 215,   0, 255, 255,
   95,   0,   0,  95,   0,  95,  95,   0, 135,  95,   0, 175,
   95,   0, 215,  95,   0, 255,  95,  95,   0,  95,  95,  95,
   95,  95, 135,  95,  95, 175,  95,  95, 215,  95,  95, 255,
   95, 135,   0,  95, 135,  95,  95, 135, 135,  95, 135, 175,
   95, 135, 215,  95, 135, 255,  95, 175,   0,  95, 175,  95,
   95, 175, 135,  95, 175, 175,  95, 175, 215,  95, 175, 255,
   95, 215,   0,  95, 215,  95,  95, 215, 135,  95, 215, 175,
   95, 215, 215,  95, 215, 255,  95, 255,   0,  95, 255,  95,
   95, 255, 135,  95, 255, 175,  95, 255, 215,  95, 255, 255,
  135,   0,   0, 135,   0,  95, 135,   0, 135, 135,   0, 175,
  135,   0, 215, 135,   0, 255, 135,  95,   0, 135,  95,  95,
  135,  95, 135, 135,  95, 175, 135,  95, 215, 135,  95, 255,
  135, 135,   0, 135, 135,  95, 135, 135, 135, 135, 135, 175,
  135, 135, 215, 135, 135, 255, 135, 175,   0, 135, 175,  95,
  135, 175, 135, 135, 175, 175, 135, 175, 215, 135, 175, 255,
  135, 215,   0, 135, 215,  95, 135, 215, 135, 135, 215, 175,
  135, 215, 215, 135, 215, 255, 135, 255,   0, 135, 255,  95,
  135, 255, 135, 135, 255, 175, 135, 255, 215, 135, 255, 255,
  175,   0,   0, 175,   0,  95, 175,   0, 135, 175,   0, 175,
  175,   0, 215, 175,   0, 255, 175,  95,   0, 175,  95,  95,
  175,  95, 135, 175,  95, 175, 175,  95, 215, 175,  95, 255,
  175, 135,   0, 175, 135,  95, 175, 135, 135, 175, 135, 175,
  175, 135, 215, 175, 135, 255, 175, 175,   0, 175, 175,  95,
  175, 175, 135, 175, 175, 175, 175, 175, 215, 175, 175, 255,
  175, 215,   0, 175, 215,  95, 175, 215, 135, 175, 215, 175,
  175, 215, 215, 175, 215, 255, 175, 255,   0, 175, 255,  95,
  175, 255, 135, 175, 255, 175, 175, 255, 215, 175, 255, 255,
  215,   0,   0, 215,   0,  95, 215,   0, 135, 215,   0, 175,
  215,   0, 215, 215,   0, 255, 215,  95,   0, 215,  95,  95,
  215,  95, 135, 215,  95, 175, 215,  95, 215, 215,  95, 255,
  215, 135,   0, 215, 135,  95, 215, 135, 135, 215, 135, 175,
  215, 135, 215, 215, 135, 255, 215, 175,   0, 215, 175,  95,
  215, 175, 135, 215, 175, 175, 215, 175, 215, 215, 175, 255,
  215, 215,   0, 215, 215,  95, 215, 215, 135, 215, 215, 175,
  215, 215, 215, 215, 215, 255, 215, 255,   0, 215, 255,  95,
  215, 255, 135, 215, 255, 175, 215, 255, 215, 215, 255, 255,
  255,   0,   0, 255,   0,  95, 255,   0, 135, 255,   0, 175,
  255,   0, 215, 255,   0, 255, 255,  95,   0, 255,  95,  95,
  255,  95, 135, 255,  95, 175, 255,  95, 215, 255,  95, 255,
  255, 135,   0, 255, 135,  95, 255, 135, 135, 255, 135, 175,
  255, 135, 215, 255, 135, 255, 255, 175,   0, 255, 175,  95,
  255, 175, 135, 255, 175, 175, 255, 175, 215, 255, 175, 255,
  255, 215,   0, 255, 215,  95, 255, 215, 135, 255, 215, 175,
  255, 215, 215, 255, 215, 255, 255, 255,   0, 255, 255,  95,
  255, 255, 135, 255, 255, 175, 255, 255, 215, 255, 255, 255,
    8,   8,   8,  18,  18,  18,  28,  28,  28,  38,  38,  38,
   48,  48,  48,  58,  58,  58,  68,  68,  68,  78,  78,  78,
   88,  88,  88,  98,  98,  98, 108, 108, 108, 118, 118, 118,
  128, 128, 128, 138, 138, 138, 148, 148, 148, 158, 158, 158,
  168, 168, 168, 178, 178, 178, 188, 188, 188, 198, 198, 198,
  208, 208, 208, 218, 218, 218, 228, 228, 228, 238, 238, 238,
]


available_modes = [
  "half",
  "half-dither",
  "single",
  "single-dither",
  "double",
  "double-dither",
  "braille",
]


rotation_modes = {
  "0"   : None,
  "90"  : Image.ROTATE_90,
  "180" : Image.ROTATE_180,
  "270" : Image.ROTATE_270,
}


flip_modes = {
  "no" : None,
  "h"  : Image.FLIP_LEFT_RIGHT,
  "v"  : Image.FLIP_TOP_BOTTOM,
}


sampling_modes = {
  "nearest"  : Image.Resampling.NEAREST,
  "box"      : Image.Resampling.BOX,
  "bilinear" : Image.Resampling.BILINEAR,
  "hamming"  : Image.Resampling.HAMMING,
  "bicubic"  : Image.Resampling.BICUBIC,
  "lanczos"  : Image.Resampling.LANCZOS,
}


class Options:
  img_file   : list[str]
  flip       : str
  mode       : str
  resampling : str
  rotate     : str
  size       : str
  term_size  : tuple[int, int]
  char_size  : tuple[float, float]
  time       : float


def parse_args(argv: list[str]) -> Options:
  parser = argparse.ArgumentParser(
    description="Display images on the terminal"
  )
  parser.add_argument(
    "img_file", nargs="+",
    help="The image(s) to be displayed"
  )
  parser.add_argument(
    "-f", "--flip", choices=["no", "h", "v"], default="no",
    help="Flip image (horizontally or vertically)"
  )
  parser.add_argument(
    "-m", "--mode", choices=available_modes, default=available_modes[0],
    help="Specify how the image should be rendered"
  )
  parser.add_argument(
    "-p", "--resampling", choices=["nearest", "box", "bilinear", "hamming",
    "bicubic", "lanczos"],
    default="lanczos",
    help="Resampling mode to use when resizing the image"
  )
  parser.add_argument(
    "-r", "--rotate", choices=["0", "90", "180", "270"], default="0",
    help="Rotate image (in 90 degree increments)"
  )
  parser.add_argument(
    "-s", "--size", choices=["height", "width", "orig", "fill"],
    default="height",
    help="Specify the size calculation mode"
  )
  parser.add_argument(
    "-S", "--term-size", nargs=2, type=int,
    help="Specify the size of the terminal manually"
  )
  parser.add_argument(
    "-c", "--char-size", nargs=2, type=float, default=(5, 11),
    help="Specify the proportions of each character"
  )
  parser.add_argument(
    "-t", "--time", type=float, default=0,
    help="Specify the delay, in seconds, between each image being printed"
  )
  return parser.parse_args(argv[1:])


def calc_rendering_mode(mode: str) -> tuple[tuple[int, int], tuple]:  
  modes = {
    "half": (
      (1, 2), (do_nothing,      newline_ansi, render_half)),
    "half-dither": (
      (1, 2), (dither_image,    newline_ansi, render_half_dithered)),
    "single": (
      (1, 1), (do_nothing,      newline_ansi, render_single)),
    "single-dither": (
      (1, 1), (dither_image,    newline_ansi, render_single_dithered)),
    "double": (
      (.5, 1), (do_nothing,     newline_ansi, render_single)),
    "double-dither": (
      (.5, 1), (dither_image,   newline_ansi, render_single_dithered)),
    "braille": (
      (2, 8), (dither_bw_image, newline_ansi, render_braille)),
  }
  return modes[mode]


def calc_screen_size(term_size: tuple[int, int]) -> tuple[int, int]:
  if term_size is not None:
    return term_size
  else:
    W, H = os.get_terminal_size()
    return (W, H - 2)


def normalize_char_size(
  char_size: tuple[float, float]
) -> tuple[float, float]:
  w, h = char_size
  den = min(w, h)
  return w / den, h / den


def calc_size(
  size_mode   : str,
  screen_size : tuple[int, int],
  image_size  : tuple[int, int],
  pixel_size  : tuple[int, int],
  char_size   : tuple[float, float],
) -> tuple[int, int]:
  sw, sh = screen_size
  iw, ih = image_size
  pw, ph = pixel_size
  
  # Terminal characters are approx. twice as tall as they are wide
  cw, ch = char_size
  iw *= ch
  ih *= cw

  match size_mode:
    case "fill":
      nw, nh = sw, sh
    case "orig":
      nw, nh = iw, ih
    case "height":
      ratio = min(sw / iw, sh / ih)
      nw, nh = iw * ratio, ih * ratio
    case "width":
      ratio = sw / iw
      nw, nh = iw * ratio, ih * ratio
  
  nw = math.floor(math.floor(nw) * pw)
  nh = math.floor(math.floor(nh) * ph)

  return nw, nh


def apply_transforms(
  im       : Image.Image,
  rotation : int | None,
  flip     : int | None,
) -> Image.Image:
  im = im.convert("RGB")
  if rotation is not None:
    im = im.transpose(rotation)
  if flip is not None:
    im = im.transpose(flip)
  return im


def newline_ansi() -> str:
  return "\033[m\n"


def dither_image(im: Image.Image) -> Image.Image:
  p_img = Image.new("P", (16, 16))
  p_img.putpalette(dither_palette)
  return im.quantize(palette=p_img, dither=Image.Dither.FLOYDSTEINBERG)


def dither_bw_image(im: Image.Image) -> Image.Image:
  p_img = Image.new("P", (2, 1))
  p_img.putpalette([
      0,   0,   0,
    255, 255, 255,
  ])
  return im.quantize(palette=p_img, dither=Image.Dither.FLOYDSTEINBERG)


def do_nothing(im: Image.Image) -> Image.Image:
  return im


def render_half(
  im : Image.Image,
  i  : int,
  j  : int,
) -> str:
  r1, g1, b1 = im.getpixel((j, i))
  r2, g2, b2 = im.getpixel((j, i + 1))
  return f"\033[38;2;{r1};{g1};{b1};48;2;{r2};{g2};{b2}m▀"


def render_half_dithered(
  im : Image.Image,
  i  : int,
  j  : int,
) -> str:
  p1 = im.getpixel((j, i))
  p2 = im.getpixel((j, i + 1))
  p1 = 16 if p1 < 16 else p1
  p2 = 16 if p2 < 16 else p2
  return f"\033[38;5;{p1};48;5;{p2}m▀"


def render_single(
  im : Image.Image,
  i  : int,
  j  : int,
) -> str:
  r, g, b = im.getpixel((j, i))
  return f"\033[48;2;{r};{g};{b}m "


def render_single_dithered(
  im : Image.Image,
  i  : int,
  j  : int,
) -> str:
  p = im.getpixel((j, i))
  p = 16 if p < 16 else p
  return f"\033[48;5;{p}m "


def render_braille(
  im : Image.Image,
  i  : int,
  j  : int,
) -> str:
  p1 = im.getpixel((j, i)) == 1
  p2 = im.getpixel((j, i + 1)) == 1
  p3 = im.getpixel((j, i + 2)) == 1
  p4 = im.getpixel((j + 1, i)) == 1
  p5 = im.getpixel((j + 1, i + 1)) == 1
  p6 = im.getpixel((j + 1, i + 2)) == 1
  p7 = im.getpixel((j, i + 3)) == 1
  p8 = im.getpixel((j + 1, i + 3)) == 1
  return "\033[1m" + chr(
    0x2800 +
    (p1 << 0) +
    (p2 << 1) +
    (p3 << 2) +
    (p4 << 3) +
    (p5 << 4) +
    (p6 << 5) +
    (p7 << 6) +
    (p8 << 7)
  )


def render(
  img_file     : str,
  pixel_size   : tuple[int, int],
  size_mode    : str,
  screen_size  : tuple[int, int],
  char_size    : tuple[float, float],
  rotation     : int | None,
  flip         : int | None,
  sampling     : int,
  render_funcs : tuple[callable, callable, callable],
  multiple     : bool,
  delay        : float,
) -> int:
  try:
    im = Image.open(img_file)
  except Exception:
    print(f"Error! Could not open file '{img_file}'")
    return 1
  
  im = apply_transforms(im, rotation, flip)
  newsize = calc_size(size_mode, screen_size, im.size, pixel_size, char_size)
  im = im.resize(newsize, sampling)

  init, line, loop = render_funcs
  im = init(im)
  out = ""
  for i in range(round(newsize[1] / pixel_size[1])):
    for j in range(round(newsize[0] / pixel_size[0])):
      pi = i * pixel_size[1]
      pj = j * pixel_size[0]
      out += loop(im, pi, pj)
    out += line()

  if multiple:
    print(f"{img_file}:")
  print(out, end="")

  if delay > 0:
    time.sleep(delay)

  return 0


def main(argv: list[str]) -> int:
  options = parse_args(argv)  

  pixel_size, render_function = calc_rendering_mode(options.mode)
  screen_size = calc_screen_size(options.term_size)
  char_size = normalize_char_size(options.char_size)

  status = 0

  rotation = rotation_modes [options.rotate]
  flip     = flip_modes     [options.flip]
  sampling = sampling_modes [options.resampling]

  status = 0
  for img_file in options.img_file:
    result = render(
      img_file,
      pixel_size,
      options.size,
      screen_size,
      char_size,
      rotation,
      flip,
      sampling,
      render_function,
      len(options.img_file) > 1,
      options.time,
    )
    status = max(status, result)
  
  return status


if __name__ == "__main__":
  sys.exit(main(sys.argv))

