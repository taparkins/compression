from PIL import Image, ImageFile

QTC_FORMAT = 'qtc'
QTC_DESCRIPTION = 'Custom Quad-Tree based compression image format'
class QtcImageFile(ImageFile.ImageFile):

    def _open(self):
        pass

def _build_tree(channel_image):
    pass

def _save(image, file_pointer, _filename):
    y_image, cb_image, cr_image = image.convert('YCbCr').split()

    y_tree = _build_tree(y_image)
    cb_tree = _build_tree(cb_image)
    cr_tree = _build_tree(cr_image)


