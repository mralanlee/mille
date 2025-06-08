import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [sveltekit()],
  server: {
    proxy: {
      // Proxy API requests to Go backend during development
      '/api': {
        target: 'http://localhost:8080',
        changeOrigin: true
      }
    }
  }
});