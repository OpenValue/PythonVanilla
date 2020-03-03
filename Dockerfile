FROM continuumio/miniconda3

WORKDIR /src
COPY . .
RUN conda env create -f environment.yml -p .conda \
&& conda clean --all -f -y

ENTRYPOINT ["./entrypoint.sh"]
