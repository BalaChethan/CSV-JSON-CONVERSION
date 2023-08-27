import pandas as pd
import json

# Function to convert CSV to JSON
def csv_to_json(input_csv_path, output_json_path):
    # Load CSV into a Pandas DataFrame
    df = pd.read_csv(input_csv_path)
    
    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records', lines=True)
    
    # Write JSON data to output file
    with open(output_json_path, 'w') as json_file:
        json_file.write(json_data)

# Main function
def main():
    input_csv_path = 'input.csv'  # Replace with your CSV file path
    output_json_path = 'output.json'  # Replace with desired output JSON file path
    
    csv_to_json(input_csv_path, output_json_path)
    
    print("CSV to JSON conversion completed.")

if __name__ == "__main__":
    main()
