import os
import csv

def load_expansion_mappings(expansions_file):
    """Load expansion name mappings from CSV file."""
    mappings = {}
    try:
        with open(expansions_file, 'r', encoding='utf-8') as f:
            # Use semicolon as delimiter
            reader = csv.reader(f, delimiter=';')
            # Skip header row
            next(reader)
            for row in reader:
                if len(row) >= 2:
                    # First column is the set code, second is Cardmarket name
                    set_code = row[0].strip()
                    cardmarket_name = row[1].strip()
                    
                    # Only add mapping if set_code is not empty
                    if set_code:
                        mappings[set_code] = cardmarket_name
                    
                    # Debug print
                    print(f"Added mapping: {set_code} -> {cardmarket_name}")
                    
    except Exception as e:
        print(f"Warning: Could not load expansion mappings: {str(e)}")
        print(f"Current mappings: {mappings}")
    return mappings

def clean_card_entry(line, expansion_mappings):
    """Clean and format a card entry line."""
    try:
        # Split the line into quantity and card info
        quantity, card_info = line.strip().split(' ', 1)
        
        # Extract card name and set code
        if ' (' in card_info:
            # Split on the last occurrence of ' ('
            card_name, set_info = card_info.rsplit(' (', 1)
            # Clean up the set code by removing parentheses and card number
            set_code = set_info.split(' ')[0].rstrip(')')
            
            # Look up the set name in our mappings
            cardmarket_name = expansion_mappings.get(set_code, set_code)
            
            # Debug print
            print(f"Processing: {set_code} -> {cardmarket_name}")
            
            # Format for Cardmarket with exactly one set of parentheses
            return f"{quantity} {card_name} ({cardmarket_name})"
        else:
            return f"{quantity} {card_info}"
    except Exception as e:
        print(f"Warning: Could not parse line '{line}': {str(e)}")
        return line

def convert_list(input_file, output_file, expansions_file):
    """Convert a Moxfield list to Cardmarket format."""
    try:
        # First, load the expansion mappings
        print("Loading expansion mappings...")
        expansion_mappings = load_expansion_mappings(expansions_file)
        print(f"Loaded {len(expansion_mappings)} expansion mappings")
        
        # Then process the input file
        print("\nProcessing card list...")
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        # Clean each line
        cleaned_lines = []
        for line in lines:
            if line.strip():
                cleaned_line = clean_card_entry(line, expansion_mappings)
                cleaned_lines.append(cleaned_line)
        
        # Write the output
        print("\nWriting output file...")
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write('\n'.join(cleaned_lines))
            
        print("Conversion complete!")
            
    except FileNotFoundError:
        print(f"Error: Could not find input file {input_file}")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")

if __name__ == "__main__":
    # Define paths relative to the script location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    input_file = os.path.join(project_root, 'moxfield-list.txt')
    output_file = os.path.join(project_root, 'cardmarket-list.txt')
    expansions_file = os.path.join(project_root, 'library', 'expansions.csv')
    
    convert_list(input_file, output_file, expansions_file)