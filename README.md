# imgs.ai

**imgs.ai** is a fast, dataset-agnostic, deep visual search engine for digital art history based on neural network embeddings. It utilizes modern approximate k-NN algorithms via [Spotify's Annoy library](https://github.com/spotify/annoy) to deliver fast search results even for very large datasets in low-resource environments, and integrates the [OpenAI CLIP model](https://openai.com/blog/clip/) for text-based visual search. 

**Try it [here](https://imgs.ai) on the complete [Rijksmuseum](https://www.rijksmuseum.nl) and [Metropolitan Museum of Art](https://www.metmuseum.org) collections** ([CC0](https://creativecommons.org/publicdomain/zero/1.0/)) or sign up for an account to access more functions/datasets (institutional email address and approval required). 

imgs.ai is developed by [Fabian Offert](https://zentralwerkstatt.org), with contributions by Peter Bell and Oleg Harlamov. Get in touch at hi@imgs.ai.

## Local installation

Only MacOS and Linux environments are currently supported.

1. Download and install the [Anaconda](https://www.anaconda.com/) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (preferred) package manager.
2. Create a Python 3.8 conda environment with `conda create --yes -n imgs.ai python=3.11` and activate it with `conda activate imgs.ai`.
3. Clone or download the repository and run the [install.sh](install.sh) shell script with your preferred shell. If you would like to install with GPU support, add the following parameter: `pytorch-cuda=12.1`, where the version number is the version of CUDA you would like PyTorch to use (this depends on your GPU and the PyTorch version, see https://pytorch.org/ for more information).
4. To start imgs.ai, run the [run.sh](run.sh) shell script with your preferred shell.
5. Open a web browser and navigate to `localhost:5000` to see the interface. 
6. To access private models and use the upload function, a default user with full access is set up, username: `hi@imgs.ai`, password: `hi@imgs.ai`.

**Never run imgs.ai in a production environment unless you have adapted [config.py](config.py) and know what you are doing.**

We provide the Rijksmuseum dataset (embeddings only) for testing purposes. The dataset is trained on nearly 400,000 works in the [Rijksmuseum](https://www.rijksmuseum.nl) collection. This is a live dataset, images are pulled from the Rijksmuseum servers on request. Right-click an image to go to the source website on the Rijksmuseum servers.

## Local training (experimental)

Please see [make_model.py](app/make_model.py) to train your own model, GPU support strongly recommended.
