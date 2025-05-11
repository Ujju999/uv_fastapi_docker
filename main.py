from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def main():
    return "hello from new project"

if __name__ == "__main__":
    main()