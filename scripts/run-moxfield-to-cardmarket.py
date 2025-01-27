import os
import sys

# Add the scripts directory to the Python path
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)

# Now we can import from the same directory
from moxfield_to_cardmarket import convert_list

def main():
    # Define paths relative to the script location
    project_root = os.path.dirname(script_dir)
    input_file = os.path.join(project_root, 'moxfield-list.txt')
    output_file = os.path.join(project_root, 'cardmarket-list.txt')
    expansions_file = os.path.join(project_root, 'library', 'expansions.csv')

    try:
        # Ensure input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file not found at {input_file}")
            print("Please create 'moxfield-list.txt' with your card list.")
            return

        # Run the conversion
        convert_list(input_file, output_file, expansions_file)
        print(f"Successfully converted Moxfield list to Cardmarket format!")
        print(f"Output saved to: {output_file}")

    except Exception as e:
        print(f"Error during conversion: {str(e)}")

if __name__ == "__main__":
    main()