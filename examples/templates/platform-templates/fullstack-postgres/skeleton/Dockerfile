FROM nginx:stable-alpine

LABEL app="${{ values.component_id }}"
LABEL owner="${{ values.owner }}"
LABEL generated_by="backstage-fullstack-postgres-golden-path"

COPY frontend/ /usr/share/nginx/html/

EXPOSE 80

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD wget -qO- http://localhost/ || exit 1

CMD ["nginx", "-g", "daemon off;"]
