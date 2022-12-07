FROM ubi9
ADD prom-target.py /
ENTRYPOINT ["/prom-target.py"]
