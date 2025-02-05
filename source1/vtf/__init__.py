import os
import platform

NO_BPY = int(os.environ.get('NO_BPY', '0'))


class UnsupportedOS(Exception):
    pass


def is_vtflib_supported():
    platform_name = platform.system()

    if platform_name == "Windows":
        return True
    elif platform_name == "Linux":
        return True
    elif platform_name == "Darwin":  # Thanks to Teodoso Lujan who compiled me a version of VTFLib
        return True
    else:
        return False


if is_vtflib_supported() and not NO_BPY:
    from .import_vtf import import_texture
    from .export_vtf import export_texture
    from .cubemap_to_envmap import load_skybox_texture, SkyboxException
else:

    class SkyboxException(Exception):
        pass


    def import_texture(name, file_object, update=False):
        return


    def load_skybox_texture(skyname):
        return


    def export_texture(blender_texture, path, image_format=None, filter_mode=None):
        pass
