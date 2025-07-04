# Color Contrast
# What is most readable? What you think and I think are probably different.
#
# converted to PyQt6 from
# From https://stackoverflow.com/questions/3116260/given-a-background-color-how-to-get-a-foreground-color-that-makes-it-readable-o
#

import sys

from PyQt6.QtGui import QColor
class MostReadableColor():
    def getLuminance(self, color):
        """ get color luminance.

        Convert color RGB values to gamma adjusted normalized rgb values
        then combine them using sRGB constants (rounded to 4 places).
        """
        r, g, b, a = QColor(color).getRgb()
        l = ((r/255)**2.2)*0.2126 + ((g/255)**2.2)*0.7151 + \
            ((b/255)**2.2)*0.0721
        return(l)

    def getContrastRation(self, color1, color2):
        l1 = self.getLuminance(color1)
        l2 = self.getLuminance(color2)
        cr = (l1 + .05)/(l2+.05) if l1 > l2 else (l2+.05)/(l1 + .05)
        return(cr)

    def getMostReadable(self, color):
        cr = []
        for c in QColor.colorNames():
            if c == 'transparent':
                continue
            cr.append([self.getContrastRation(color, c), c])
        sorted_cr = sorted(cr, reverse=True)
        return(sorted_cr[0][1])

def main():
    if len(sys.argv) != 2:
        print("usage: MostReadableColor color_name (ex: 'red')")
    else:
        mrc = MostReadableColor()
        best_contrast_color = mrc.getMostReadable(sys.argv[1])
        print(f"{best_contrast_color}")

if __name__ == "__main__":
    main()
