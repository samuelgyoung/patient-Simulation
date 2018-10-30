FROM alpine:3.5
RUN apk add --update python py-pip 
RUN apk --update add --virtual scipy-runtime python py-pip \
    && apk add --virtual scipy-build \
        build-base python-dev openblas-dev freetype-dev pkgconfig gfortran \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && pip install --no-cache-dir numpy \ 
    && pip install --no-cache-dir matplotlib \
    && pip install --no-cache-dir scipy \
    && apk del scipy-build \
    && apk add --virtual scipy-runtime \
        freetype libgfortran libgcc libpng  libstdc++ musl openblas tcl tk \
	&& rm -rf /var/cache/apk/*
COPY requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt
COPY app.py /src
COPY patientSimBin  /src/patientSimBin
CMD python /src/app.py
