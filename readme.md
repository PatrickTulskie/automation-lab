![Automation Lab](documentation/img/logo.png)

A Docker-based environment to host various automation and productivity tools, including [n8n](https://n8n.io), [Jupyter Notebook](https://jupyter.org), and [Open-WebUI](https://github.com/open-webui/open-webui).

---

## Prerequisites

1. **Docker**: Ensure Docker and Docker Compose are installed on your system.

   Install Docker:
   https://docs.docker.com/get-docker/

   Install Docker Compose:
   https://docs.docker.com/compose/install/

   Install Ollama:
   https://ollama.com

2. Local File Paths: You don't have to use these paths, but you will need to update the `docker-compose.yml` file if you choose to use different paths.

    ```bash
    mkdir ~/.n8n # This is where n8n will store its data and configuration so it is persisted if the container is removed
    mkdir -p ~/Code/jupyter-notebooks # This is where Jupyter Notebook will store its notebooks
    ```

## Getting Started

1. **Clone Repository**: Clone the repository to your local machine.

    ```bash
    git clone https://github.com/patricktulskie/automation-lab.git
    cd automation-lab
    ```
2. **Start Services**: Start the Docker services.

    ```bash
    docker compose up -d
    ```

3. **Access Services**: Access the services in your browser.

    Once the environment is running, access the dashboard to easily navigate to all tools:

    * Dashboard: http://localhost:9000
    * n8n: http://localhost:5678
    * Jupyter Notebook: http://localhost:8888
    * Open-WebUI: http://localhost:3000

4. **Stop Services**: Stop the Docker services and remove containers.

    ```bash
    docker compose down
    ```

5. **Update Services**: Update the Docker services.

    ```bash
    docker compose pull
    docker compose up -d
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
