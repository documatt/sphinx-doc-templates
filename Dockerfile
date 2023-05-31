FROM sphinxdoc/sphinx-latexpdf:5.3.0 as base

WORKDIR /docs
ADD requirements/ requirements/
RUN pip3 install -r requirements/extensions.txt