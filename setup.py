from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess

class CustomInstallCommand(install):
    gdrive_link = "https://drive.google.com/drive/folders/10Doj-bx6GhHnLNcPu3heIxltRcGA1AW6?usp=share_link"
    def run(self):
        try:
            subprocess.call(['sudo', 'apt', 'update'])
            subprocess.call(['sudo', 'apt', 'upgrade'])
        except:
            print("Faliure of apt update due to non-Ubuntu OS. Installing packages..")
        subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])
        subprocess.call(['pip3', 'install', '-e', '.'])
        # # This commented lines are for Tensorflow GPU setup.
        # # subprocess.call(['conda', 'install', '-c', 'conda-forge', 'cudatoolkit=11.8.0'])
        # # subprocess.call(['python3', '-m', 'pip', 'install', 'nvidia-cudnn-cu11==8.6.0.163'])
        # # subprocess.call(['mkdir', '-p', '$CONDA_PREFIX/etc/conda/activate.d'])
        # # subprocess.call(['echo', 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))', '>>', '$CONDA_PREFIX/etc/conda/activate.d/env_vars.sh'])
        # # subprocess.call(['echo', "'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib'", '>>', '$CONDA_PREFIX/etc/conda/activate.d/env_vars.sh'])
        # # subprocess.call(['source', '$CONDA_PREFIX/etc/conda/activate.d/env_vars.sh'])
        # # subprocess.call(['XLA_FLAGS=--xla_gpu_cuda_data_dir=/usr/lib/cuda'])
        print("**************************************")
        print("Downloading trained weights...")
        try:
            subprocess.call(['pip3', 'install', 'gdown'])
            subprocess.call(['gdown', '--fuzzy', 'https://drive.google.com/drive/folders/10Doj-bx6GhHnLNcPu3heIxltRcGA1AW6?usp=share_link', '--folder'])
            subprocess.call(['mv', 'Model_weights', 'visual_odometry/files/'])
        except:
            print("Error in downloading trained weights. Please download them manually from " + self.gdrive_link)
        print("**************************************")
        print("Successful installation!")
        print("Install tensorflow GPU from " + "https://www.tensorflow.org/install/pip")
        print("**************************************")
        install.run(self)

setup(name="visual_odometry", version="1.0", packages=find_packages(),
      cmdclass = {
          'install': CustomInstallCommand,
      })
