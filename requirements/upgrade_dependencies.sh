#!/bin/bash
#
# This script is meant to simplify the upgrade of the various provided requirements
# files to the latest available package versions. We assume, that the script is
# either called from the project root directly or from its subfolder 'requirements'.
# All provided requirements-files are updated according to the
# specified dependencies from setup.py and the dev-requirements-files for all the
# different versions.
# The production dependencies belong into the according list 'install_requires' in
# setup.py and the development dependencies into the various dev-requirements.in-files.
# For execution the script needs virtual environments, one for each of the upstream
# supported Python versions, with pip-tools installed. Those environments need to be
# placed at ../envs/time-series-metadata-PYTHONVERSION relative to the project root.
# The proper naming for the versions you find in the line starting with 'for PYVENV '
# in in this script.
# Since pip-tools did not work as convenient for Python 3.5 and there were
# conflicts for some of the newer package versions this case is handled separately.
# The script starts with navigating to the project root, if it was called from
# the subfolder ./requirements/.
if [ -f requirements.txt ] && [ -d ../time-series-metadata/ ] && [ -d ../requirements/]; then
    cd ..
fi

# Handle Python 3.5 via requirements.in.
# Activate according Python environment.
source ../envs/time-series-metadata-3.5/bin/activate && \
pip install --upgrade pip pip-tools && \
# Create dev-requirements...txt from dev-requirements...in.
pip-compile --upgrade requirements/dev-requirements-py35.in --output-file \
 requirements/dev-requirements-py35.txt && \
pip-sync requirements/dev-requirements-py35.txt && \
deactivate

# Handle all other Python versions via setup.py by cycling through the different Python
# environments and update the according two requirements files by issuing the
# according pip-tools command pip-compile from within the specific environments.
export PYTHONPATH=$PYTHONPATH:$(pwd)
for PYVENV in "6" "7" "8"
do
    # Activate according Python environment.
    source ../envs/time-series-metadata-3.$PYVENV/bin/activate && \
    pip install --upgrade pip pip-tools && \
    # Create dev-requirements...txt from dev-requirements...in.
    pip-compile --upgrade requirements/dev-requirements.in --output-file \
    requirements/dev-requirements-py3$PYVENV.txt && \
    pip-sync requirements/dev-requirements-py3$PYVENV.txt && \
    deactivate
done
