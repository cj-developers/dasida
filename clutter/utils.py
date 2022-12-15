# Write env_file
def write_env_file(env_dict: dict, filename: str = ".env"):
    """Write env_file.
    
    [NOTE]
    This is for docker swarm's env_file.
    
    Args:
        env_dict (dict): Environemnt variables. e.g., {"key_1": "value_1", "key_2": "value_2"}
        filename (str, optional): Defaults to ".env".
    """
    lines = []
    for k, v in env_dict.items():
        lines.append("=".join([k, str(v)]))
    with open(filename, "w") as f:
        f.write("\n".join(lines))


# Read env_file
def read_env_file(filename: str = ".env"):
    """Read env_file.
    
    [NOTE]
    This is for docker swarm's env_file. 

    Args:
        filename (str, optional): Defaults to ".env".

    Returns:
        dict: env_file
    """
    with open(filename, "r") as f:
        env_text = f.read()
    env = dict()
    for line in env_text.split("\n"):
        k, v = line.split("=", 1)
        env.update({k: v})
    return env
