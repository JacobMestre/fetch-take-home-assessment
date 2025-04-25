This is a FastAPI web service that processes receipts and calculates points based on predefined rules. 


## Requirements
- Docker


## Running the application

1. Build the Docker image using the command: 
docker build -t receipt-processor

2. Run the container using the command:
docker run -p 8000:8000 receipt-processor


3. Access the API documentation at: 
http://localhost:8000/docs




## API Endpoints

- **POST /receipts/process**: Submit a receipt and returns the ID assigned to the receipt.
- **GET /receipts/{id}/points**: Returns the points awarded for a receipt.

## Notes
- No additional Docker configuration is needed.
- Data is stored in memory and resets when the application stops.
