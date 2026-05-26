module.exports = {
  apps: [
    {
      name: "samruddhi-api",
      script: "backend/api_server.py",
      interpreter: "python",
      cwd: ".",
      autorestart: true,
      watch: false,
      max_restarts: 10,
      env: {
        ENVIRONMENT: "production"
      }
    }
  ]
};