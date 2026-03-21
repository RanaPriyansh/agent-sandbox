from setuptools import setup
setup(
    name="agent-sandbox",
    version="0.1.0",
    py_modules=["agent_sandbox"],
    install_requires=["pywasm>=0.1", "docker>=6.0", "pydantic>=2.0"],
    python_requires=">=3.9",
)
