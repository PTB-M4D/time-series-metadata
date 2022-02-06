#!/bin/bash
#
# This script is meant to simplify the upgrade of the various provided requirements
# files to the latest available package versions. We assume, that the script is
# either called from the project root directly or from its subfolder 'requirements'.
# All provided requirements-files are updated according to the
# specified dependencies from setup.py and the dev-requirements-files for all the
# different versions.
# The production dependencies belong into the according list 'install_requires' in
# setup.py and the development dependencies into the dev-requirements.in-file.
# Actually since at the moment we do not have production dependencies, the
# install_requires section does not get compiled into its own requirements file.
# Refer to github.com/PTB-M4D/PyDynamic for a draft how to include this compilation
# step into this script, once it gets relevant.
# For execution the script needs virtual environments, one for each of the upstream
# supported Python versions, with pip-tools installed. Those environments need to be
# placed at ../envs/time-series-metadata-PYTHONVERSION relative to the project root.
# The proper naming for the versions you find in the line starting with 'for PYVENV '
# in in this script.
# The script starts with navigating to the project root, if it was called from
# the subfolder ./requirements/.
if [ -f requirements.txt ] && [ -d ../time-series-metadata/ ] && [ -d ../requirements/]; then
    cd ..
fi

# Handle all Python versions via setup.py by cycling through the different Python
# environments and update the according two requirements files by issuing the
# according pip-tools command pip-compile from within the specific environments.
export PYTHONPATH=$PYTHONPATH:$(pwd)
for PYVENV in "7" "8" "9" "10"
do
    echo "
Compile dependencies for Python 3.$PYVENV
====================================
    "
    # Activate according Python environment.
    source ../envs/time-series-metadata-3.$PYVENV/bin/activate && \
    python -m pip install --upgrade pip pip-tools && \
    # Create dev-requirements...txt from dev-requirements...in.
    python -m piptools compile --upgrade requirements/dev-requirements.in \
    --output-file requirements/dev-requirements-py3$PYVENV.txt && \
    deactivate
done
