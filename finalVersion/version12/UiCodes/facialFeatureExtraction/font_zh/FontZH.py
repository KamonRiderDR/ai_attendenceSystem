# 安装指令 pip install freetype-py
import freetype
import copy
import os

current_dir = os.path.dirname(__file__)
# 生成数据文件的绝对路径(在window下存在汉字路径问题，需要设置系统为utf-8编码)
font_file = os.path.join(current_dir, "fonts/msyh.ttf")

class FontZh:
    def __init__(self):
        super(FontZh, self).__init__()
        self._face = freetype.Face(font_file)
 
    def draw_text(self, image, pos, text, text_size, text_color):
        '''绘制汉字文本'''
        self._face.set_char_size(text_size * 64)
        metrics = self._face.size
        ascender = metrics.ascender/64.0
        ypos = int(ascender)
 
        # if not isinstance(text, unicode):
        #     text = text.decode('utf-8')
        #print(type(image))
        img = self.draw_string(image, pos[0], pos[1]+ypos, text, text_color)
        return img
 
    def draw_string(self, img, x_pos, y_pos, text, color):
        '''文本绘制函数'''
        prev_char = 0
        pen = freetype.Vector()
        pen.x = x_pos << 6   # div 64
        pen.y = y_pos << 6
 
        hscale = 1.0
        matrix = freetype.Matrix(int(hscale)*0x10000, int(0.2*0x10000),\
                                 int(0.0*0x10000), int(1.1*0x10000))
        cur_pen = freetype.Vector()
        pen_translate = freetype.Vector()
 
        image = copy.deepcopy(img)
        #print(type(img))
        for cur_char in text:
            self._face.set_transform(matrix, pen_translate)
 
            self._face.load_char(cur_char)
            kerning = self._face.get_kerning(prev_char, cur_char)
            pen.x += kerning.x
            slot = self._face.glyph
            bitmap = slot.bitmap
 
            cur_pen.x = pen.x
            cur_pen.y = pen.y - slot.bitmap_top * 64
            self.draw_ft_bitmap(image, bitmap, cur_pen, color)
 
            pen.x += slot.advance.x
            prev_char = cur_char
 
        return image
 
    def draw_ft_bitmap(self, img, bitmap, pen, color):
        '''位图绘制'''
        x_pos = pen.x >> 6
        y_pos = pen.y >> 6
        cols = bitmap.width
        rows = bitmap.rows
 
        glyph_pixels = bitmap.buffer
 
        for row in range(rows):
            for col in range(cols):
                if glyph_pixels[row*cols + col] != 0:
                    img[y_pos + row][x_pos + col][0] = color[0]
                    img[y_pos + row][x_pos + col][1] = color[1]
                    img[y_pos + row][x_pos + col][2] = color[2]


zh = FontZh()
