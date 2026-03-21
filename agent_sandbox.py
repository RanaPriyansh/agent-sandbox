class Sandbox:
    def __init__(self, max_cpu=1.0, max_memory="512MB", allow_network=True, allow_filesystem=False):
        self.limits = {"cpu": max_cpu, "memory": max_memory}
        self.capabilities = {"network": allow_network, "filesystem": allow_filesystem}

    def run(self, code, input_data=None):
        return {"output": "Sandboxed execution", "error": None}
