FROM continuumio/miniconda3

WORKDIR /src
COPY . .
RUN conda env create -f environment.yml -p .conda \
&& conda clean --all -f -y

ENTRYPOINT ["./entrypoint.sh"]
#/bin/bash -c "export PATH=/opt/conda/envs/$(head -1 /src/environment.yml | cut -d' ' -f2)/bin:$PATH \
           #       && source activate $(head -1 /src/environment.yml | cut -d' ' -f2) \
           #       && ./entrypoint.sh"
