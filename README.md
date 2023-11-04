# Image Search Demo
Search images in PDF files using text.

## Data
You can find the test PDF file in `data folder` of this repo to test the app.

## Install requirements
If you want to run this demos locally you need to install all the requirements.
```bash
pip install -r requitements.txt
```

## Start the demo
To run the demos locally run the following code.
```bash
cd app
python demo.py
```

You can set a specific port by setting the environment variable `GRADIO_SERVER_PORT`.

## Build Docker image
To build the Docker image just use the following cmd. In this case we called the image `image_search_demo` but you can call it however you want.
```bash
docker build -t image_search_demo .
```

## Run the Docker image
To run the Docker image call the following cmd:

```bash
docker run --rm -p 7860:7860 image_search_demo
```

If you defined another port in the Dockerfile do not forget to pass that as container port in the `docker run`.