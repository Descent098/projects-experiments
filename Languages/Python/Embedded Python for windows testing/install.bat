python-files\python.exe python-files\get-pip.py
echo =================================== && echo "pip installed moving onto jupyter" && echo ===================================
python-files\python.exe -m pip install jupyterlab
python-files\python.exe -m pip install ipywidgets && python-files\python.exe -m jupyter labextension install @jupyter-widgets/jupyterlab-manager@2.0
python-files\python.exe -m pip install ipycanvas && python-files\python.exe -m jupyter labextension install @jupyter-widgets/jupyterlab-manager ipycanvas
python-files\python.exe -m pip install ipyevents && python-files\python.exe -m jupyter labextension install @jupyter-widgets/jupyterlab-manager ipyevents
python-files\python.exe -m pip install .\python-files\spark-main
python-files\python.exe -m jupyter notebook