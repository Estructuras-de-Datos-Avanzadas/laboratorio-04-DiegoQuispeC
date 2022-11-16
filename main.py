#!/usr/bin/env python
#-*- coding: utf8 -*-

from PIL import Image
from color import Color
from octree_quantizer import OctreeQuantizer


def main():
    image = Image.open('img/hallowen.jpg')
    pixels = image.load()
    width, height = image.size

    octree = OctreeQuantizer()

    # add colors to the octree
    for j in range(height):
        for i in range(width):
            octree.add_color(Color(*pixels[i, j]))

    # 256 colors for 8 bits per pixel output image
    #para 64 colores cambiar el 256 por 64
    palette = octree.make_palette(256)

    # create palette for 256 color max and save to file
    #para 64 colores cambiar el 16 po 8
    palette_image = Image.new('RGB', (16, 16))
    palette_pixels = palette_image.load()
    for i, color in enumerate(palette):
        palette_pixels[i % 16, i / 16] = (int(color.red), int(color.green), int(color.blue))
    palette_image.save('img/hallowen_palette.png')

    # agrandando la paleta 256 colores usados
    #para 64 colores cambiar el 20 por 40   en i//20,j//20
    imagen= Image.new('RGB', (320, 320))
    pixel=imagen.load()
    for i in range(320):
        for j in range(320):
            pixel[i,j]=palette_pixels[i//20,j//20]
    imagen.save('img/hallowen_paleta_agrandado.png')


    # save output image
    out_image = Image.new('RGB', (width, height))
    out_pixels = out_image.load()
    for j in range(height):
        for i in range(width):
            index = octree.get_palette_index(Color(*pixels[i, j]))
            color = palette[index]
            out_pixels[i, j] = (int(color.red), int(color.green), int(color.blue))
    out_image.save('img/hallowen_salida.png')


if __name__ == '__main__':
    main()
