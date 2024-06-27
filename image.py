#!/bin/python3.11

from PIL import Image
import argparse
import math
import time
import sys
import os


palette = [
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
  pixel      : str
  term_size  : tuple[int, int]
  img_file   : list[str]
  rotate     : str
  flip       : str
  size       : str
  resampling : str
  color      : str
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
    "-c", "--color", choices=["normal", "dither"], default="normal",
    help="Specify the rendering color mode"
  )
  parser.add_argument(
    "-r", "--rotate", choices=["0", "90", "180", "270"], default="0",
    help="Rotate image (in 90 degree increments)"
  )
  parser.add_argument(
    "-f", "--flip", choices=["no", "h", "v"], default="no",
    help="Flip image (horizontally or vertically)"
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
    "-m", "--resampling", choices=["nearest", "box", "bilinear", "hamming",
    "bicubic", "lanczos"],
    default="lanczos",
    help="Resampling mode to use when resizing the image"
  )
  parser.add_argument(
    "-p", "--pixel", choices=["half", "single", "double"], default="half",
    help="Specify the size, in characters, of each pixel"
  )
  parser.add_argument(
    "-t", "--time", type=float, default=0,
    help="Specify the delay, in seconds, between each image being printed"
  )
  return parser.parse_args(argv[1:])


def calc_pixel_shape(pixel: str) -> tuple[tuple[int, int], str]:
  if pixel == "single":
    return ((1, 1,), " ")
  if pixel == "double":
    return ((2, 1,), "  ")
  elif pixel == "half":
    return ((1, 2,), "▀")


def calc_screen_size(term_size: tuple[int, int]) -> tuple[int, int]:
  if term_size is not None:
    return term_size
  else:
    W, H = os.get_terminal_size()
    return (W, H - 2)


def calc_size(
  size_mode   : str,
  screen_size : tuple[int, int],
  image_size  : tuple[int, int],
  pixel_size  : tuple[int, int]
):
  W, H = screen_size
  w, h = image_size
  w *= 2
  pixel_w, pixel_h = pixel_size
  if size_mode == "fill":
    newsize = (W // pixel_w,
    H * pixel_h)
  else:
    if size_mode == "height":
      ratio = min(W / w, H / h)
    elif size_mode == "width":
      ratio = W / w
    elif size_mode == "orig":
      ratio = 1
    newsize = (
      math.floor(w * ratio // pixel_w),
      math.floor(h * ratio * pixel_h)
    )
  return newsize


def apply_transforms(
  im       : Image.Image,
  newsize  : tuple[int, int],
  rotation : int | None,
  flip     : int | None,
  sampling : int
) -> Image.Image:
  im = im.convert("RGB")
  if rotation is not None:
    im = im.transpose(rotation)
  if flip is not None:
    im = im.transpose(flip)
  im = im.resize(newsize, sampling)
  return im


def render_dithered(
  im      : Image.Image,
  newsize : tuple[int, int],
  pixel_c : str,
  p_img   : Image
):
  out = ""
  im = im.quantize(palette=p_img, dither=Image.Dither.FLOYDSTEINBERG)
  for i in range(newsize[1]):
    for j in range(newsize[0]):
      p = im.getpixel((j, i))
      p = 16 if p < 16 else p
      out += f"\033[48;5;{p}m{pixel_c}"
    out += "\033[m\n"
  return out


def render_dithered_subpixel(
  im      : Image.Image,
  newsize : tuple[int, int],
  pixel_c : str,
  p_img   : Image
):
  out = ""
  im = im.quantize(palette=p_img, dither=Image.Dither.FLOYDSTEINBERG)
  for i in range(newsize[1] // 2):
    for j in range(newsize[0]):
      p1 = im.getpixel((j, i * 2))
      p2 = im.getpixel((j, i * 2 + 1))
      p1 = 16 if p1 < 16 else p1
      p2 = 16 if p2 < 16 else p2
      out += f"\033[38;5;{p1};48;5;{p2}m{pixel_c}"
    out += "\033[m\n"
  return out


def render_normal(
  im      : Image.Image,
  newsize : tuple[int, int],
  pixel_c : str,
  _       : Image
):
  out = ""
  for i in range(newsize[1]):
    for j in range(newsize[0]):
      r, g, b = im.getpixel((j, i))
      out += f"\033[48;2;{r};{g};{b}m{pixel_c}"
    out += "\033[m\n"
  return out


def render_normal_subpixel(
  im      : Image.Image,
  newsize : tuple[int, int],
  pixel_c : str,
  _       : Image
):
  out = ""
  for i in range(newsize[1] // 2):
    for j in range(newsize[0]):
      r1, g1, b1 = im.getpixel((j, i * 2))
      r2, g2, b2 = im.getpixel((j, i * 2 + 1))
      out += f"\033[38;2;{r1};{g1};{b1};48;2;{r2};{g2};{b2}m{pixel_c}"
    out += "\033[m\n"
  return out


def render(
  pixel_shape     : tuple[tuple[int, int], str],
  img_file        : str,
  size_mode       : str,
  screen_size     : tuple[int, int],
  rotation        : int | None,
  flip            : int | None,
  sampling        : int,
  render_function : callable,
  p_img           : Image.Image,
  multiple        : bool,
  delay           : float,
):
  pixel_size, pixel_c = pixel_shape
  try:
    im = Image.open(img_file)
  except Exception:
    print(f"Error! Could not open file '{img_file}'")
    return 1
  
  newsize = calc_size(size_mode, screen_size, im.size, pixel_size)
  im = apply_transforms(im, newsize, rotation, flip, sampling)

  out = render_function(im, newsize, pixel_c, p_img)

  if multiple:
    print(f"{img_file}:")
  print(out, end="")

  if delay > 0:
    time.sleep(delay)

  return 0


def main(argv: list[str]) -> int:
  options = parse_args(argv)  

  pixel_shape = calc_pixel_shape(options.pixel)
  screen_size = calc_screen_size(options.term_size)

  p_img = Image.new("P", (16, 16))
  p_img.putpalette(palette)
  status = 0

  rotation = rotation_modes [options.rotate]
  flip     = flip_modes     [options.flip]
  sampling = sampling_modes [options.resampling]

  match (options.color, pixel_shape[0][1]):
    case ("normal", 1):
      render_function = render_normal
    case ("normal", 2):
      render_function = render_normal_subpixel
    case ("dither", 1):
      render_function = render_dithered
    case ("dither", 2):
      render_function = render_dithered_subpixel

  status = 0
  for img_file in options.img_file:
    result = render(
      pixel_shape,
      img_file,
      options.size,
      screen_size,
      rotation,
      flip,
      sampling,
      render_function,
      p_img,
      len(options.img_file) > 1,
      options.time,
    )
    status = max(status, result)
  
  return status


if __name__ == "__main__":
  sys.exit(main(sys.argv))

