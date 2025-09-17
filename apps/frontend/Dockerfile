# Build stage
FROM node:20-alpine AS build
WORKDIR /app
COPY package.json package-lock.json* pnpm-lock.yaml* yarn.lock* .npmrc* ./ 2>/dev/null || true
RUN npm init -y >/dev/null 2>&1 || true
# Falls package.json noch leer ist, fügen wir deps beim Copy unten hinzu
COPY . .
RUN [ -f package.json ] && npm ci || true
RUN [ -f package.json ] && npm run build || mkdir -p dist

# Serve stage
FROM nginx:alpine
COPY docker/nginx/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
