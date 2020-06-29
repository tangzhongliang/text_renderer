import subprocess
import os
import numpy as np
from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext

"""
Run setup with the following command:
```
python setupGpuWrapper.py build_ext --inplace
```
"""

# Determine current directory of this setup file to find our module
CUR_DIR = os.path.dirname(__file__)
# Use pkg-config to determine library locations and include locations
#opencv_libs_str = '-L/usr/local/opencv4/lib -lopencv_cudastereo -lopencv_shape -lopencv_cudabgsegm -lopencv_dnn -lopencv_ml -lopencv_videostab -lopencv_stitching -lopencv_cudafeatures2d -lopencv_cudaobjdetect -lopencv_superres -lopencv_cudaoptflow -lopencv_cudalegacy -lopencv_calib3d -lopencv_features2d -lopencv_highgui -lopencv_cudacodec -lopencv_videoio -lopencv_imgcodecs -lopencv_cudawarping -lopencv_video -lopencv_objdetect -lopencv_flann -lopencv_photo -lopencv_cudaimgproc -lopencv_cudafilters -lopencv_imgproc -lopencv_cudaarithm -lopencv_core -lopencv_cudev'
#opencv_incs_str = '-I/usr/local/opencv4/include/opencv4 -I/usr/local/include'

opencv_libs_str = subprocess.check_output("pkg-config --libs opencv4".split()).decode()
opencv_incs_str = subprocess.check_output("pkg-config --cflags opencv4".split()).decode()

# Parse into usable format for Extension call
opencv_libs = [str(lib) for lib in opencv_libs_str.strip().split()]
opencv_incs = [str(inc) for inc in opencv_incs_str.strip().split()]
print([np.get_include()] + opencv_incs)
print(opencv_libs)
extensions = [
    Extension('GpuWrapper',
              sources=[os.path.join(CUR_DIR, 'GpuWrapper.pyx')],
              language='c++',
              include_dirs=[np.get_include()] + opencv_incs,
              extra_link_args=opencv_libs)
]

setup(
    cmdclass={'build_ext': build_ext},
    name="GpuWrapper",
    ext_modules=cythonize(extensions)
)
