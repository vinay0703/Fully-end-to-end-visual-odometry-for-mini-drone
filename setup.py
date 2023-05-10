from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class CustomInstallCommand(install):
    def run(self):
        subprocess.call(['sudo', 'apt', 'update'])
        subprocess.call(['sudo', 'apt', 'upgrade'])
        subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])
        subprocess.call(['pip3', 'install', '-e', '.'])
        # subprocess.call(['conda', 'install', '-c', 'conda-forge', 'cudatoolkit=11.8.0'])
        # subprocess.call(['python3', '-m', 'pip', 'install', 'nvidia-cudnn-cu11==8.6.0.163'])
        # subprocess.call(['mkdir', '-p', '$CONDA_PREFIX/etc/conda/activate.d'])
        # subprocess.call(['echo', 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))', '>>', '$CONDA_PREFIX/etc/conda/activate.d/env_vars.sh'])
        # subprocess.call(['echo', "'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib'", '>>', '$CONDA_PREFIX/etc/conda/activate.d/env_vars.sh'])
        # subprocess.call(['source', '$CONDA_PREFIX/etc/conda/activate.d/env_vars.sh'])
        # subprocess.call(['XLA_FLAGS=--xla_gpu_cuda_data_dir=/usr/lib/cuda'])
        print("Successful installation!")
        print("Install tensorflow GPU from " + "https://www.tensorflow.org/install/pip")
        install.run(self)

setup(name="visual_odometry", version="1.0", packages=find_packages(),
      cmdclass = {
          'install': CustomInstallCommand,
      })
