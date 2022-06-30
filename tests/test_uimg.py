from utils.uimg import text2image,add_water_mark
def test_uimg():
    img_font= "./text_font/2.ttf"
    mark_font= "./text_font/1.ttf"
    img=text2image("hahaha"*100,img_font, (250,100,100,100),img_size=(300,1000))
    img_mark=add_water_mark(img, "水印",mark_font)
    img.show()
    img_mark.show()
    assert img is not None
    assert img_mark is not None