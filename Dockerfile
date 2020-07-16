FROM alpine:latest
RUN apk add --no-cache cifs-utils ca-certificates
COPY ./chartmuseum /usr/local/bin/chartmuseum
RUN ln -s /usr/local/bin/chartmuseum
RUN chmod +x /usr/local/bin/chartmuseum
USER 1000:1000
ENTRYPOINT ["/chartmuseum"]
