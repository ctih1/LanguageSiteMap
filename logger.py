class Logger:
    def start() -> None:
        with open("log.txt","w") as f:
            f.write("## LOG START ##")
    def log(info, level):
        with open("log.txt","a") as f:
            f.write(f"[{level}] - {info}")