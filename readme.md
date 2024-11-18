Steps

1.Install dependencies:
pip install -r requirements.txt

2.Prepare the datasets: Run the preprocessing script:
python scripts/preprocess.py

3.Train the model:
python main.py --mode train

4.Test the model: After training, test it using:
python main.py --mode test --checkpoint outputs/checkpoints/latest_model.pth