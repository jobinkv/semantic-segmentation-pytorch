from __future__ import print_function

from setuptools import find_packages, setup


def get_long_description():
    with open('README.md') as f:
        long_description = f.read()

    try:
        import github2pypi

        return github2pypi.replace_url(
            slug='IanTaehoonYoo/semantic-segmentation-pytorch', content=long_description
        )
    except Exception:
        return long_description

setup(name="torch_seg_models",
      version="0.1.7",
      description="Semantic Segmentation with Pytorch",
      long_description=get_long_description(),
      long_description_content_type='text/markdown',
      author="Jobin k.V.",
      author_email='kwjobin@gmail.com',
      platforms=["any"],
      license="MIT",
      url="https://github.com/jobinkv/semantic-segmentation-pytorch.git",
      packages=find_packages(exclude=["segmentation/test/dataset"]),
      install_requires=[
            "torch>=1.5.0",
            "torchvision>=0.5.0",
            "tensorboardX>=2.0"
            "opencv-python",
            "tqdm"],
      extras_require={
            "tensorflow": ["tensorflow"], #this is to provide backbone models.
      },
      classifiers=['License :: OSI Approved :: MIT License']
)
