
## Accessing Jureca

```bash
ssh <user>@jureca.fz-juelich.de
```

## Training materials

```bash
cd /p/project/training1922/arbor
```

## Getting a Jupyter notebook running

### 1) configure jupyter environment for this user

```
cd $HOME
mkdir HPC4NS
cd HPC4NS
mkdir -p ~/.local/share/jupyter/kernels/
cp -r /p/project/training1922/arbor/ .
cp -r /p/project/training1922/arbor/requirements/venv_arbor/  ~/.local/share/jupyter/kernels/
```

### 2) open and run notebook in browser

Open `https://jupyter-jsc.fz-juelich.de` locally on your computer, login, and configure the session (Jureca login node).

On the left, go to folder `HPC4NS-->arbor-->{demo,handson}` and double click and run the notebook, e.g. `demo_ring_network.ipynb` or `solution_ring_network.ipynb`.
